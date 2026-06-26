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

print("Waiting for answer...")

browser.waits.seconds(15)

text = browser.read()

browser.close()

print("\n" + "=" * 70)

print(text[:3000])

print("=" * 70)