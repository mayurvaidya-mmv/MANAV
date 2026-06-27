"""
Research Engine

Executes the complete
research workflow.
"""

from browser.browser_manager import BrowserManager
from ai.ai_manager import AIManager


class ResearchEngine:

    def __init__(self):

        self.browser = BrowserManager()

        self.ai = AIManager()

    def execute(self, provider, query):

        self.browser.launch()

        provider.search(
            self.browser,
            query
        )

        text = self.browser.read()

        self.browser.close()

        result = self.ai.summarize(text)

        return result