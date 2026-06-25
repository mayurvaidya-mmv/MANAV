"""
router/router.py

Main routing module for Personal JARVIS.
"""

from router.intent_classifier import IntentClassifier


class Router:

    def __init__(self):
        self.classifier = IntentClassifier()

    def route(self, request: str):
        """
        Classify the user's request and return the detected intent.
        """

        intent = self.classifier.classify(request)

        return intent