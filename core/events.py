"""
Event Bus

Provides publish/subscribe communication
between MANAS services.
"""


class EventBus:

    def __init__(self):

        self._subscribers = {}

    def subscribe(self, event_name: str, callback):

        self._subscribers.setdefault(
            event_name,
            []
        ).append(callback)

    def publish(self, event_name: str, data=None):

        callbacks = self._subscribers.get(
            event_name,
            []
        )

        for callback in callbacks:

            callback(data)