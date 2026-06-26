"""
Base class for all MANAS skills.
"""


class BaseSkill:

    def execute(self, plan: dict):
        raise NotImplementedError(
            "Skill must implement execute()."
        )