"""
Perplexity Research Provider

Version 1
"""

import urllib.parse
import webbrowser


class PerplexityProvider:

    def search(self, query: str):

        encoded_query = urllib.parse.quote(query)

        url = f"https://www.perplexity.ai/search?q={encoded_query}"

        print()
        print("=" * 50)
        print("Perplexity Provider")
        print(f"Searching: {query}")
        print("=" * 50)

        webbrowser.open(url)