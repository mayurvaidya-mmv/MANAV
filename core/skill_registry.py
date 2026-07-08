"""
core/skill_registry.py

Dynamic skill registry with auto-discovery.
Maintains the index of all available skills (hand-written + auto-generated).
"""

import os
import json
import importlib.util
from pathlib import Path
from typing import Dict, List, Optional


class SkillRegistry:
    """
    Discovers, loads, and manages all skills in the system.
    Maintains skill_manifest.json as the source of truth.
    """
    
    SKILLS_DIR = Path(__file__).parent.parent / "skills"
    MANIFEST_FILE = SKILLS_DIR / "skill_manifest.json"
    
    def __init__(self):
        self._skills = {}  # {name: skill_instance}
        self._manifest = {}  # {name: metadata_dict}
        self._load_manifest()
        self._auto_discover()
        self._save_manifest()  # ADD THIS LINE — save manifest after discovery
    
    def _load_manifest(self):
        """Load skill_manifest.json if it exists."""
        if self.MANIFEST_FILE.exists():
            with open(self.MANIFEST_FILE, 'r') as f:
                self._manifest = json.load(f)
        else:
            self._manifest = {}
    
    def _auto_discover(self):
        """
        Scan skills/ directory for .py files.
        Load any class that inherits from BaseSkill.
        Instantiate and register it.
        """
        if not self.SKILLS_DIR.exists():
            print(f"[SkillRegistry] Skills directory not found: {self.SKILLS_DIR}")
            return
        
        for file_path in self.SKILLS_DIR.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            if file_path.name == "skill_manifest.json":
                continue
            
            self._load_skill_from_file(file_path)
    
    def _load_skill_from_file(self, file_path: Path):
        """
        Dynamically import a Python file and instantiate any BaseSkill subclasses.
        """
        try:
            spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Import BaseSkill so we can check inheritance
            from skills.base_skill import BaseSkill
            
            # Find all classes in the module that inherit from BaseSkill
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and issubclass(obj, BaseSkill) and obj is not BaseSkill:
                    try:
                        skill_instance = obj()
                        skill_name = skill_instance.SKILL_NAME or name.lower()
                        
                        self._skills[skill_name] = skill_instance
                        
                        # If metadata not in manifest, extract from skill
                        if skill_name not in self._manifest:
                            self._manifest[skill_name] = {
                                "class": obj.__name__,
                                "file": file_path.name,
                                "description": skill_instance.SKILL_DESCRIPTION or "",
                                "supported_intents": skill_instance.SUPPORTED_INTENTS or [],
                                "supported_tasks": skill_instance.SUPPORTED_TASKS or [],
                                "required_inputs": skill_instance.REQUIRED_INPUTS or [],
                                "output_type": skill_instance.OUTPUT_TYPE or "dict",
                                "auto_generated": False,
                                "version": "1.0"
                            }
                        
                        print(f"[SkillRegistry] Loaded skill: {skill_name}")
                    except Exception as e:
                        print(f"[SkillRegistry] Failed to instantiate {name}: {e}")
        
        except Exception as e:
            print(f"[SkillRegistry] Failed to load {file_path.name}: {e}")
    
    def register_dynamic(self, skill_class, metadata: dict) -> bool:
        """
        Register a dynamically generated skill.
        - Instantiate the skill
        - Write its code to disk
        - Update manifest
        - Save manifest to disk
        """
        try:
            # Instantiate
            skill_instance = skill_class()
            skill_name = metadata.get("name")
            
            # Register in memory
            self._skills[skill_name] = skill_instance
            self._manifest[skill_name] = metadata
            
            # Write the skill class to a file
            generated_file = self.SKILLS_DIR / f"{skill_name}_generated.py"
            self._write_skill_to_file(skill_class, generated_file)
            
            # Update manifest on disk
            self._save_manifest()
            
            print(f"[SkillRegistry] Registered dynamic skill: {skill_name}")
            return True
        
        except Exception as e:
            print(f"[SkillRegistry] Failed to register dynamic skill: {e}")
            return False
    
    def _write_skill_to_file(self, skill_class, file_path: Path):
        """Write the skill class definition to a Python file."""
        import inspect
        source_code = inspect.getsource(skill_class)
        with open(file_path, 'w') as f:
            f.write(source_code)
    
    def _save_manifest(self):
        """Write manifest to skill_manifest.json."""
        try:
            with open(self.MANIFEST_FILE, 'w') as f:
                json.dump(self._manifest, f, indent=2)
        except Exception as e:
            print(f"[SkillRegistry] Failed to save manifest: {e}")
    
    def list_all(self) -> Dict:
        """Return metadata for all registered skills."""
        return self._manifest
    
    def get_by_task(self, task_type: str):
        """Find a skill that can handle this task type."""
        for skill_name, metadata in self._manifest.items():
            if task_type in metadata.get("supported_tasks", []):
                return self._skills.get(skill_name)
        return None
    
    def get_by_intent(self, intent_name: str):
        """Find a skill that handles this intent."""
        for skill_name, metadata in self._manifest.items():
            if intent_name in metadata.get("supported_intents", []):
                return self._skills.get(skill_name)
        return None
    
    def get_skill(self, skill_name: str):
        """Get a specific skill by name."""
        return self._skills.get(skill_name)
    
    def skill_exists(self, skill_name: str) -> bool:
        """Check if a skill is registered."""
        return skill_name in self._skills
    
    def get_metadata(self, skill_name: str) -> Optional[dict]:
        """Get metadata for a specific skill."""
        return self._manifest.get(skill_name)