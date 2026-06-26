"""
Browser Wait Utilities
"""


class BrowserWaits:

    def __init__(self, page):

        self.page = page

    def seconds(self, sec):

        self.page.wait_for_timeout(sec * 1000)

    def selector(self, selector):

        self.page.wait_for_selector(selector)
    
    def selector(self, selector: str, timeout: int = 60000):

        self.page.wait_for_selector(
            selector,
            timeout=timeout
        )