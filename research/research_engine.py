"""
Research Engine

Executes the complete
research workflow.
"""

from browser.browser_manager import BrowserManager
from ai.ai_manager import AIManager

from knowledge.models import Knowledge
from memory.memory_manager import MemoryManager


class ResearchEngine:

    def __init__(self):

        self.browser = BrowserManager()

        self.ai = AIManager()

        self.memory = MemoryManager()

    def execute(self, provider, query):

        # Launch browser
        self.browser.launch()

        # Research
        provider.search(
            self.browser,
            query
        )

        # Read page
        text = self.browser.read()

        # Close browser
        self.browser.close()

        # Summarize
        result = self.ai.summarize(text)

        # Save into long-term memory
        knowledge = Knowledge(

            topic=result.topic,

            summary=result.summary

        )

        self.memory.save(knowledge)

        return result