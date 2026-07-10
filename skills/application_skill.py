"""
Application Skill

Launches and controls desktop applications.
"""

from hands.executor import Executor
from skills.base_skill import BaseSkill


class ApplicationSkill(BaseSkill):

    # Metadata
    SKILL_NAME = "application"

    SKILL_DESCRIPTION = (
        "Launch and control desktop applications."
    )

    SUPPORTED_INTENTS = [
        "ACTION"
    ]

    SUPPORTED_TASKS = [
        "OPEN_APPLICATION"
    ]

    REQUIRED_INPUTS = [
        "application"
    ]

    OUTPUT_TYPE = "bool"

    def __init__(self):

        self.executor = Executor()

    def execute(self, plan: dict):

        return self.executor.execute(plan)