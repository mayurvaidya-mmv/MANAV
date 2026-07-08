"""
Application Skill

Opens applications on Windows.
"""

from skills.base_skill import BaseSkill
from hands.executor import Executor


class ApplicationSkill(BaseSkill):
    
    # Metadata attributes — tells the system what this skill does
    SKILL_NAME = "application"
    SKILL_DESCRIPTION = "Open and launch applications on Windows"
    SUPPORTED_INTENTS = ["ACTION"]
    SUPPORTED_TASKS = ["OPEN_APPLICATION"]
    REQUIRED_INPUTS = ["application"]
    OUTPUT_TYPE = "dict"

    def __init__(self):
        self.executor = Executor()

    def execute(self, plan: dict):
        """Execute the application skill."""
        application = plan["arguments"]["application"]
        self.executor.open_application(application)
        return {"status": "opened", "application": application}