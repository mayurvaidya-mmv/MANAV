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

            self.application.execute(plan)

            return

        if task == "WEB_RESEARCH":

            self.research.execute(plan)

            return

        print(f"Unknown task: {task}")