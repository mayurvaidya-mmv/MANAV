"""
Research Manager

Chooses which research provider to use.
"""

from research.research_engine import ResearchEngine
from research.providers.perplexity_provider import PerplexityProvider


class ResearchManager:

    def __init__(self):

        self.engine = ResearchEngine()

        # Default provider
        self.provider = PerplexityProvider()

    def research(self, query: str):

        return self.engine.execute(
            self.provider,
            query
        )