"""
Browser Wait Utilities
"""

from playwright.sync_api import TimeoutError


class BrowserWaits:

    def __init__(self, page):

        self.page = page

    def seconds(self, sec):

        self.page.wait_for_timeout(sec * 1000)

    def selector(self, selector: str, timeout: int = 60000):

        self.page.wait_for_selector(
            selector,
            timeout=timeout
        )




    def body_length(self):

        return len(
            self.page.locator("body").inner_text()
        )

    def page_stable(
        self,
        timeout: int = 30000,
        interval: int = 1000,
        stable_checks: int = 3
    ):
        """
        Wait until the page text stops changing.
        """

        previous = -1
        stable = 0
        elapsed = 0

        while elapsed < timeout:

            current = self.body_length()

            if current == previous:

                stable += 1

                if stable >= stable_checks:
                    return

            else:

                stable = 0

            previous = current

            self.page.wait_for_timeout(interval)

            elapsed += interval

        raise TimeoutError(
            "Timed out waiting for stable page."
        )