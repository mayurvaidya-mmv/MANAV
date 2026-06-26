from browser.browser_manager import BrowserManager

browser = BrowserManager()

browser.launch()

browser.open("https://www.perplexity.ai")

browser.waits.seconds(5)

# Temporary selector
selector = "#ask-input"

browser.type(
    selector,
    "Research MQTT"
)

browser.waits.seconds(10)

browser.close()