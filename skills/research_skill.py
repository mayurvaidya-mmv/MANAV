"""
Research Skill

Currently a placeholder.

Next ticket will connect it
to Perplexity or Browser.
"""

from skills.base_skill import BaseSkill


class ResearchSkill(BaseSkill):

    def execute(self, plan: dict):

        query = plan["arguments"]["query"]

        print()

        print("=" * 50)

        print("Research Skill")

        print(f"Searching for: {query}")

        print("=" * 50)

        print()

        # Implementation next ticket