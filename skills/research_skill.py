"""
Research Skill

Delegates research to the Research Manager.
"""

from skills.base_skill import BaseSkill
from research.research_manager import ResearchManager


class ResearchSkill(BaseSkill):

    def __init__(self):

        self.manager = ResearchManager()

    def execute(self, plan: dict):

        query = plan["arguments"]["query"]

        self.manager.research(query)