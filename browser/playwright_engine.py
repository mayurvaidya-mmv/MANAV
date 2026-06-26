"""
Playwright Engine

Low-level browser operations.
"""

from playwright.sync_api import sync_playwright


class PlaywrightEngine:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.page = None

    def launch(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

    def goto(self, url):

        self.page.goto(url)

    def close(self):

        self.browser.close()

        self.playwright.stop()