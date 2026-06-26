"""
High-level Browser Manager.
"""

from email.mime import text

from browser.playwright_engine import PlaywrightEngine
from browser.actions import BrowserActions
from browser.waits import BrowserWaits
from browser.page_reader import PageReader


class BrowserManager:

    def __init__(self):

        self.engine = PlaywrightEngine()

        self.actions = None
        self.waits = None
        self.reader = None

    def launch(self):

        self.engine.launch()

        self.actions = BrowserActions(self.engine.page)

        self.waits = BrowserWaits(self.engine.page)

        self.reader = PageReader(self.engine.page)

        print("Browser launched.")

    def open(self, url):

        self.engine.goto(url)

        print(f"Opened {url}")

    def read(self):

        return self.reader.read()

    def close(self):

        self.engine.close()

        print("Browser closed.")
        
    def type(self, selector: str, text: str):

        self.actions.type(selector, text)
    def press(self, key: str):

        self.actions.press(key)