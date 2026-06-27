"""
Perplexity Research Provider

Uses Playwright + Local LLM
to perform autonomous research.
"""

from browser.browser_manager import BrowserManager
from ai.ai_manager import AIManager


class PerplexityProvider:

    def __init__(self):

        self.browser = BrowserManager()
        self.ai = AIManager()

    def search(self, query: str):

        print()
        print("=" * 50)
        print("Perplexity Provider")
        print(f"Searching: {query}")
        print("=" * 50)

        # Launch browser
        self.browser.launch()

        # Open Perplexity
        self.browser.open("https://www.perplexity.ai")

        # Give the page time to load
        self.browser.waits.seconds(5)

        # Type the research query
        self.browser.type(
            "#ask-input",
            query
        )

        self.browser.waits.seconds(1)

        # Submit
        self.browser.press("Enter")

        print("Waiting for research...")

        # Temporary wait
        self.browser.waits.seconds(15)

        # Read the webpage
        text = self.browser.read()

        # Close browser
        self.browser.close()

        # Summarize locally
        result = self.ai.summarize(text)

        return result