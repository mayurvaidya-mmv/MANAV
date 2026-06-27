"""
Perplexity Research Provider

Knows how to interact with
Perplexity AI.
"""


class PerplexityProvider:

    def search(self, browser, query: str):

        print()
        print("=" * 50)
        print("Perplexity Provider")
        print(f"Searching: {query}")
        print("=" * 50)

        browser.open("https://www.perplexity.ai")

        browser.waits.seconds(5)

        browser.type(
            "#ask-input",
            query
        )

        browser.waits.seconds(1)

        browser.press("Enter")

        print("Waiting for research...")

        browser.waits.seconds(15)