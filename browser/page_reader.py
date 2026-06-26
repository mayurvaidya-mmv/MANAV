"""
browser/page_reader.py

Reads visible text from the current webpage.
"""


class PageReader:

    def __init__(self, page):

        self.page = page

    def read(self):

        text = self.page.locator("body").inner_text()

        return text