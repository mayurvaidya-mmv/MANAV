from browser.browser_manager import BrowserManager

browser = BrowserManager()

browser.launch()

browser.open("https://www.perplexity.ai")

browser.waits.seconds(5)

browser.type(
    "#ask-input",
    "Research MQTT"
)

browser.waits.seconds(1)

browser.press("Enter")

browser.waits.seconds(20)

browser.close()