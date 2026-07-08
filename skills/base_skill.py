"""
skills/base_skill.py

Base class for all MANAS skills.
Updated with metadata attributes for dynamic skill discovery and generation.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class SkillMetadata:
    """Structured metadata about a skill."""
    name: str
    description: str
    supported_intents: List[str]
    supported_tasks: List[str]
    required_inputs: List[str]
    output_type: str


class BaseSkill(ABC):
    """
    Base class for all MANAS skills.
    
    Every skill must:
    1. Inherit from BaseSkill
    2. Set the class attributes (SKILL_NAME, SKILL_DESCRIPTION, etc.)
    3. Implement the execute() method
    """
    
    # CLASS ATTRIBUTES — must be set by subclasses
    SKILL_NAME: str = None
    SKILL_DESCRIPTION: str = None
    SUPPORTED_INTENTS: List[str] = None  # e.g. ["RESEARCH", "ACTION"]
    SUPPORTED_TASKS: List[str] = None     # e.g. ["WEB_RESEARCH", "OPEN_APPLICATION"]
    REQUIRED_INPUTS: List[str] = None     # e.g. ["query", "application"]
    OUTPUT_TYPE: str = None                # e.g. "ResearchResult", "dict", "bool"
    
    def __init__(self):
        """Initialize the skill. Override if needed."""
        pass
    
    @abstractmethod
    def execute(self, plan: dict) -> Any:
        """
        Execute the skill.
        
        Args:
            plan: dict with structure:
                {
                    "intent": str,              # e.g. "RESEARCH"
                    "task": str,                # e.g. "WEB_RESEARCH"
                    "arguments": dict           # task-specific arguments
                }
        
        Returns:
            Result (type depends on the skill, see OUTPUT_TYPE)
        """
        raise NotImplementedError(f"{self.__class__.__name__} must implement execute()")
    
    def metadata(self) -> SkillMetadata:
        """
        Return structured metadata about this skill.
        Used by SkillRegistry and Meta-Agent.
        """
        return SkillMetadata(
            name=self.SKILL_NAME or self.__class__.__name__.lower(),
            description=self.SKILL_DESCRIPTION or "",
            supported_intents=self.SUPPORTED_INTENTS or [],
            supported_tasks=self.SUPPORTED_TASKS or [],
            required_inputs=self.REQUIRED_INPUTS or [],
            output_type=self.OUTPUT_TYPE or "dict"
        )
    
    def classify_tier(self, plan: dict):
        """
        (Optional) Override to provide skill-specific tier classification.
        By default, uses ApprovalLayer's task_tier_map.
        """
        return None