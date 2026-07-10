"""
Planner

Creates an execution plan using the Skill Registry.
"""

from router.intent_types import Intent


class Planner:

    def __init__(self, services):

        self.registry = services.get(
            "skill_registry"
        )

    def create_plan(self, intent: Intent, request: str):

        request = request.strip()

        selected_skill = None

        for skill in self.registry.all_skills().values():

            metadata = skill.metadata()

            if intent.name in metadata.supported_intents:

                selected_skill = metadata

                break

        if selected_skill is None:

            return {
                "intent": intent.name,
                "task": "UNKNOWN",
                "arguments": {}
            }

        task = selected_skill.supported_tasks[0]

        arguments = {}

        if task == "OPEN_APPLICATION":

            arguments["application"] = (
                request
                .replace("open", "")
                .strip()
                .lower()
            )

        elif task == "WEB_RESEARCH":

            arguments["query"] = request

        elif task == "CHAT":

            arguments["message"] = request

        return {

            "intent": intent.name,

            "task": task,

            "arguments": arguments

        }