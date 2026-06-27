"""
Research Manager

Chooses whether to use memory
or perform fresh research.
"""

from knowledge.models import ResearchResult

from memory.memory_manager import MemoryManager

from research.research_engine import ResearchEngine
from research.providers.perplexity_provider import PerplexityProvider
from research.topic_normalizer import TopicNormalizer


class ResearchManager:
    def research(self, query: str):

        topic = TopicNormalizer.normalize(query)

        print(f"[DEBUG] Query : {query}")
        print(f"[DEBUG] Topic : {topic}")
        print(f"[DEBUG] Exists: {self.memory.exists(topic)}")

        if self.memory.exists(topic):
            ...

    def __init__(self):

        self.engine = ResearchEngine()

        self.provider = PerplexityProvider()

        self.memory = MemoryManager()

    def research(self, query: str):

        topic = TopicNormalizer.normalize(query)

        if self.memory.exists(topic):

            print("\nLoaded from memory.\n")

            knowledge = self.memory.load(topic)

            return ResearchResult(

                topic=knowledge.topic,

                summary=knowledge.summary

            )

        return self.engine.execute(

            self.provider,

            query

        )