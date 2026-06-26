from browser.browser_manager import BrowserManager
from ai.ai_manager import AIManager

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

ai = AIManager()

result = ai.summarize(text)

print("\n" + "=" * 70)

print("Topic:")
print(result.topic)

print()

print("Summary:")
print(result.summary)

print("=" * 70)