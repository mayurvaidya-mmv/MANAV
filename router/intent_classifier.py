"""
router/intent_classifier.py
"""

from ai.ai_manager import AIManager
from router.intent_types import Intent


class IntentClassifier:

    def __init__(self):

        self.ai = AIManager()

    def classify(self, request: str) -> Intent:

        result = self.ai.classify_intent(request)

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