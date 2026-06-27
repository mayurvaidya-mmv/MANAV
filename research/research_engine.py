"""
Research Engine

Executes the complete
research workflow.
"""

from browser.browser_manager import BrowserManager
from ai.ai_manager import AIManager

from knowledge.models import Knowledge
from memory.memory_manager import MemoryManager

from research.topic_normalizer import TopicNormalizer


class ResearchEngine:

    def __init__(self):

        self.browser = BrowserManager()

        self.ai = AIManager()

        self.memory = MemoryManager()

    def execute(self, provider, query):

        # Normalize topic
        topic = TopicNormalizer.normalize(query)

        # Launch browser
        self.browser.launch()

        # Research
        provider.search(
            self.browser,
            query
        )

        # Read webpage
        text = self.browser.read()

        # Close browser
        self.browser.close()

        # Summarize
        result = self.ai.summarize(text)

        if not result.summary.strip():

            print("Research produced an empty summary. Nothing was saved.")

            return result

        # Override AI topic with normalized topic
        result.topic = topic

        # Save to memory
        knowledge = Knowledge(

            topic=result.topic,

            summary=result.summary

        )

        self.memory.save(knowledge)

        return result