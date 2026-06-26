"""
Application Skill
"""

from hands.executor import Executor
from skills.base_skill import BaseSkill


class ApplicationSkill(BaseSkill):

    def __init__(self):

        self.executor = Executor()

    def execute(self, plan: dict):

        self.executor.execute(plan)