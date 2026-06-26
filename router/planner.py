"""
router/planner.py

Creates an execution plan based on
the detected intent and user request.
"""

from router.intent_types import Intent


class Planner:

    def create_plan(self, intent: Intent, request: str):

        request = request.strip()

        if intent == Intent.ACTION:

            return {
                "intent": intent.name,
                "task": "OPEN_APPLICATION",
                "arguments": {
                    "application": request.replace("open", "").strip().lower()
                }
            }

        if intent == Intent.RESEARCH:

            return {
                "intent": intent.name,
                "task": "WEB_RESEARCH",
                "arguments": {
                    "query": request
                }
            }

        if intent == Intent.CHAT:

            return {
                "intent": intent.name,
                "task": "CHAT",
                "arguments": {
                    "message": request
                }
            }

        return {
            "intent": intent.name,
            "task": "UNKNOWN",
            "arguments": {}
        }