"""
router/intent_classifier.py

Uses the local LLM (LM Studio) to classify
a user's request into one of the supported intents.
"""

import requests

from config.settings import LOCAL_LLM_HOST
from router.intent_types import Intent


SYSTEM_PROMPT = """
You are an intent classifier.

Classify the user's request into EXACTLY ONE of the following intents:

chat
action
research
screen_context
memory_lookup
task_delegate
system
exit

Respond ONLY with the intent name.
Do not explain.
Do not add punctuation.
"""


class IntentClassifier:

    def __init__(self):
        self.url = f"{LOCAL_LLM_HOST}/chat/completions"

    def classify(self, request: str) -> Intent:

        response = requests.post(
            self.url,
            json={
                "model": "local-model",
                "messages": [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": request
                    }
                ],
                "temperature": 0
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        print("\n========== LM STUDIO RESPONSE ==========")
        print(data)
        print("========================================\n")

        result = (
            data["choices"][0]["message"]["content"]
            .strip()
            .lower()
        )

        mapping = {
            "chat": Intent.CHAT,
            "action": Intent.ACTION,
            "research": Intent.RESEARCH,
            "screen_context": Intent.SCREEN_CONTEXT,
            "memory_lookup": Intent.MEMORY_LOOKUP,
            "task_delegate": Intent.TASK_DELEGATE,
            "system": Intent.SYSTEM,
            "exit": Intent.EXIT
        }

        return mapping.get(result, Intent.CHAT)