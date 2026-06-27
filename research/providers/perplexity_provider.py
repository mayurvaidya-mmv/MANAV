"""
Perplexity Research Provider

Knows how to interact with
Perplexity AI.
"""

from config.settings import DEBUG


class PerplexityProvider:

    def search(self, browser, query: str):

        if DEBUG:

            print()
            print("=" * 50)
            print("Perplexity Provider")
            print(f"Searching: {query}")
            print("=" * 50)

        else:

            print("\nResearching...")

        browser.open("https://www.perplexity.ai")

        browser.waits.seconds(5)

        browser.type(
            "#ask-input",
            query
        )

        browser.waits.seconds(1)

        browser.press("Enter")

        if DEBUG:
            print("Waiting for research...")

        browser.waits.seconds(15)