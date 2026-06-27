"""
Topic Normalizer

Converts user queries into
consistent topic names.
"""


class TopicNormalizer:

    @staticmethod
    def normalize(query: str) -> str:

        query = query.lower().strip()

        if query.startswith("research"):

            query = query.replace("research", "", 1)

        return query.strip()