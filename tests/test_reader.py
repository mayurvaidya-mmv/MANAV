from browser.browser_manager import BrowserManager
from ai.ai_manager import AIManager

browser = BrowserManager()

browser.launch()

browser.open("https://example.com")

browser.waits.seconds(3)

text = browser.read()

browser.close()

ai = AIManager()

result = ai.summarize(text)

print("\n" + "=" * 60)

print("Topic:")
print(result.topic)

print()

print("Summary:")
print(result.summary)

print("=" * 60)