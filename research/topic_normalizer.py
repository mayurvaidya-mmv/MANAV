"""
Topic Normalizer
"""

from knowledge.aliases import ALIASES


class TopicNormalizer:

    @staticmethod
    def normalize(query: str) -> str:

        query = query.lower().strip()

        if query.startswith("research"):

            query = query[len("research"):].strip()

        query = " ".join(query.split())

        return ALIASES.get(query, query)