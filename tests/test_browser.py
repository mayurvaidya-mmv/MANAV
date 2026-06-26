"""
Browser Test
"""

import time

from browser.browser_manager import BrowserManager


browser = BrowserManager()

browser.launch()

browser.open("https://www.perplexity.ai")

time.sleep(5)

browser.close()