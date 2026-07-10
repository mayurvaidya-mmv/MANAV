"""
Action Dispatcher

Delegates execution through the Skill Registry.
"""


class ActionDispatcher:

    def __init__(self, services):

        self.registry = services.get(
            "skill_registry"
        )

    def dispatch(self, plan):

        task = plan["task"]

        for skill in self.registry.all_skills().values():

            metadata = skill.metadata()

            if task in metadata.supported_tasks:

                return skill.execute(plan)

        print(f"Unknown task: {task}")

        return None