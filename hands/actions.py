"""
Action Dispatcher

Delegates execution through the Skill Registry.
"""

from core.skill_registry import SkillRegistry

from skills.application_skill import ApplicationSkill
from skills.research_skill import ResearchSkill


class ActionDispatcher:

    def __init__(self):

        self.registry = SkillRegistry()

        #
        # Temporary manual registration.
        #
        # Auto-discovery and manifest loading
        # will be implemented in later versions.
        #

        self.registry.register(
            ResearchSkill()
        )

        self.registry.register(
            ApplicationSkill()
        )

    def dispatch(self, plan):

        task = plan["task"]

        #
        # Search for the skill that supports
        # this task.
        #

        for skill in self.registry.all_skills().values():

            metadata = skill.metadata()

            if task in metadata.supported_tasks:

                return skill.execute(plan)

        print(f"Unknown task: {task}")

        return None