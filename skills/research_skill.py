"""
Research Skill

Delegates research to the Research Manager.
"""

from skills.base_skill import BaseSkill
from research.research_manager import ResearchManager


class ResearchSkill(BaseSkill):
    
    # Metadata attributes — tells the system what this skill does
    SKILL_NAME = "research"
    SKILL_DESCRIPTION = "Perform web research using Perplexity and local AI"
    SUPPORTED_INTENTS = ["RESEARCH"]
    SUPPORTED_TASKS = ["WEB_RESEARCH"]
    REQUIRED_INPUTS = ["query"]
    OUTPUT_TYPE = "ResearchResult"

    def __init__(self):
        self.manager = ResearchManager()

    def execute(self, plan: dict):
        """Execute the research skill."""
        query = plan["arguments"]["query"]
        result = self.manager.research(query)
        return result