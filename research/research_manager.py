"""
Research Manager

Chooses which research provider to use.
"""

from research.providers.perplexity_provider import PerplexityProvider


class ResearchManager:

    def __init__(self):

        # Default provider
        self.provider = PerplexityProvider()

    def research(self, query: str):

        self.provider.search(query)