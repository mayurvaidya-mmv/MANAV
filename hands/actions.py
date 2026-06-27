"""
Action Dispatcher

Chooses the correct skill.
"""

from skills.application_skill import ApplicationSkill
from skills.research_skill import ResearchSkill


class ActionDispatcher:

    def __init__(self):

        self.application = ApplicationSkill()

        self.research = ResearchSkill()

    def dispatch(self, plan):

        task = plan["task"]

        if task == "OPEN_APPLICATION":

            return self.application.execute(plan)

        if task == "WEB_RESEARCH":

            return self.research.execute(plan)

        print(f"Unknown task: {task}")

        return None