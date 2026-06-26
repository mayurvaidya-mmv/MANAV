"""
Browser Actions
"""


class BrowserActions:

    def __init__(self, page):

        self.page = page

    def type(self, selector, text):

        self.page.fill(selector, text)

    def press(self, selector, key):

        self.page.press(selector, key)

    def click(self, selector):

        self.page.click(selector)