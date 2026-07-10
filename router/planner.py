"""
Planner

Creates an execution plan using the Skill Registry.
"""

from router.intent_types import Intent

from core.skill_registry import SkillRegistry

from skills.research_skill import ResearchSkill
from skills.application_skill import ApplicationSkill


class Planner:

    def __init__(self):

        self.registry = SkillRegistry()

        #
        # Temporary manual registration.
        # Auto-registration comes in later versions.
        #

        self.registry.register(
            ResearchSkill()
        )

        self.registry.register(
            ApplicationSkill()
        )

    def create_plan(self, intent: Intent, request: str):

        request = request.strip()

        #
        # Find the skill supporting this intent.
        #

        selected_skill = None

        for skill in self.registry.all_skills().values():

            metadata = skill.metadata()

            if intent.name in metadata.supported_intents:

                selected_skill = metadata

                break

        #
        # No matching skill
        #

        if selected_skill is None:

            return {
                "intent": intent.name,
                "task": "UNKNOWN",
                "arguments": {}
            }

        #
        # First supported task
        #

        task = selected_skill.supported_tasks[0]

        #
        # Build arguments
        #

        arguments = {}

        if task == "OPEN_APPLICATION":

            application = (
                request
                .replace("open", "")
                .strip()
                .lower()
            )

            arguments["application"] = application

        elif task == "WEB_RESEARCH":

            arguments["query"] = request

        elif task == "CHAT":

            arguments["message"] = request

        return {

            "intent": intent.name,

            "task": task,

            "arguments": arguments

        }