"""
brain/meta_agent.py

Generates new skills autonomously.
Called when the system encounters a task it can't do.
Uses LM Studio to generate skill code.
"""

import json
import time
from datetime import datetime


class MetaAgent:
    """
    Auto-generates skills when the system encounters unknown intents/tasks.
    """
    
    SKILL_TEMPLATE = '''
from skills.base_skill import BaseSkill


class {CLASS_NAME}(BaseSkill):
    """Auto-generated skill."""
    
    SKILL_NAME = "{SKILL_NAME}"
    SKILL_DESCRIPTION = "{SKILL_DESCRIPTION}"
    SUPPORTED_INTENTS = {SUPPORTED_INTENTS}
    SUPPORTED_TASKS = {SUPPORTED_TASKS}
    REQUIRED_INPUTS = {REQUIRED_INPUTS}
    OUTPUT_TYPE = "{OUTPUT_TYPE}"
    
    def __init__(self):
        pass
    
    def execute(self, plan: dict):
        """Execute the skill."""
        task = plan.get("task")
        arguments = plan.get("arguments", {})
        
        # TODO: Implement task handling
        # This is a placeholder. The actual implementation should be generated.
        
        if task == "{DEFAULT_TASK}":
            # Handle {DEFAULT_TASK}
            result = self._execute_{DEFAULT_TASK_LOWER}(arguments)
            return result
        
        return {{"error": f"Unknown task: {{task}}"}}
    
    def _execute_{DEFAULT_TASK_LOWER}(self, arguments: dict):
        """Implementation for {DEFAULT_TASK}."""
        # TODO: Implement
        return {{"status": "not_implemented"}}
'''
    
    def __init__(self, llm_service, skill_registry):
        """
        Args:
            llm_service: your LM Studio wrapper (must have query() method)
            skill_registry: SkillRegistry instance
        """
        self.llm = llm_service
        self.skill_registry = skill_registry
    
    def generate_skill(self, intent, request, skill_registry):
        """
        Generate a new skill for a given intent + request.
        
        Returns:
            dict with keys:
                - class_definition: str of Python code
                - metadata: dict with skill metadata
                - instance: instantiated skill (or None if generation failed)
            OR None if generation failed
        """
        
        print(f"\n[Meta-Agent] 🤖 Generating skill for: {intent.name}")
        print(f"[Meta-Agent] Request: '{request}'")
        
        try:
            # Step 1: Ask LLM for skill description
            skill_description = self._describe_needed_skill(intent, request)
            print(f"[Meta-Agent] Skill description: {skill_description}")
            
            # Step 2: Generate skill code
            skill_code = self._generate_skill_code(intent, skill_description, request)
            print(f"[Meta-Agent] Generated {len(skill_code)} characters of Python code")
            
            # Step 3: Build metadata
            metadata = self._build_metadata(intent, skill_description)
            print(f"[Meta-Agent] Metadata: {metadata['name']}")
            
            # Step 4: Instantiate and sanity check
            try:
                skill_instance = self._instantiate_skill(skill_code)
                print(f"[Meta-Agent] ✓ Skill instantiated and passed sanity check")
            except Exception as e:
                print(f"[Meta-Agent] ✗ Sanity check failed: {e}")
                return None
            
            return {
                "class_definition": skill_code,
                "metadata": metadata,
                "instance": skill_instance
            }
        
        except Exception as e:
            print(f"[Meta-Agent] ✗ Generation failed: {e}")
            return None
    
    def _describe_needed_skill(self, intent, request: str) -> str:
        """Ask LLM what kind of skill is needed."""
        
        available_skills = self.skill_registry.list_all()
        
        prompt = f"""You are an AI that designs software skills for MANAS.

User's request: {request}
Intent detected: {intent.name}

Already available skills:
{json.dumps(available_skills, indent=2)}

Based on this request and the available skills, describe a NEW skill that would be needed to handle it.

Description format:
- Name: [short name, snake_case]
- Description: [one-liner of what it does]
- Tasks it handles: [list of task types, like CREATE_FILE, READ_FILE, etc.]
- Inputs: [list of required input parameters]
- Output: [what it returns]

Be concise. Focus on what's missing."""
        
        response = self.llm.query(prompt)
        return response
    
    def _generate_skill_code(self, intent, description: str, request: str) -> str:
        """Generate the actual Python code for the skill."""
        
        prompt = f"""You are an expert Python developer generating skill classes for MANAS.

Skill to generate:
{description}

User's original request:
{request}

IMPORTANT RULES:
1. The class MUST inherit from BaseSkill
2. Set these class attributes:
   - SKILL_NAME: str, short name
   - SKILL_DESCRIPTION: str, what it does
   - SUPPORTED_INTENTS: list, e.g. ["ACTION"]
   - SUPPORTED_TASKS: list, e.g. ["CREATE_FILE", "READ_FILE"]
   - REQUIRED_INPUTS: list, e.g. ["path", "content"]
   - OUTPUT_TYPE: str, e.g. "dict"

3. Implement execute(plan: dict) method
   - plan["task"] = the task to execute
   - plan["arguments"] = dict of inputs
   - Return a dict with status

4. Add error handling

5. Add helpful comments

Generate ONLY the Python code. Start with imports and end with the class.
Do NOT include explanations, just code."""
        
        response = self.llm.query(prompt)
        return response
    
    def _build_metadata(self, intent, description: str) -> dict:
        """Extract metadata from the skill description."""
        
        # Parse the description to extract details
        # In a simple version, we just fill in template data
        
        skill_name = f"auto_skill_{int(time.time())}"
        
        return {
            "name": skill_name,
            "description": description[:300],
            "supported_intents": [intent.name],
            "supported_tasks": ["AUTO_GENERATED_TASK"],  # TODO: parse from description
            "required_inputs": [],
            "output_type": "dict",
            "auto_generated": True,
            "generated_timestamp": datetime.now().isoformat(),
            "generated_by": "meta_agent_v1",
            "approval_status": "pending"
        }
    
    def _instantiate_skill(self, skill_code: str):
        """
        Safely instantiate the generated skill code.
        
        Creates a temporary namespace and executes the code.
        Returns the instantiated skill object.
        """
        
        # Create a safe namespace for the generated code
        from skills.base_skill import BaseSkill
        
        namespace = {
            "BaseSkill": BaseSkill,
            "__builtins__": {
                "dict": dict,
                "list": list,
                "str": str,
                "int": int,
                "float": float,
                "bool": bool,
                "len": len,
                "range": range,
                "Exception": Exception,
                "NotImplementedError": NotImplementedError,
            }
        }
        
        # Execute the code
        try:
            exec(skill_code, namespace)
        except SyntaxError as e:
            raise Exception(f"Generated skill has syntax errors: {e}")
        except Exception as e:
            raise Exception(f"Failed to execute generated skill code: {e}")
        
        # Find the class that inherits from BaseSkill
        skill_instance = None
        for name, obj in namespace.items():
            if isinstance(obj, type) and issubclass(obj, BaseSkill) and obj is not BaseSkill:
                try:
                    skill_instance = obj()
                    return skill_instance
                except Exception as e:
                    raise Exception(f"Failed to instantiate {name}: {e}")
        
        raise Exception("Generated code does not contain a BaseSkill subclass")