from core.events import EventBus

bus = EventBus()


def handler(message):

    print("Received:", message)


bus.subscribe(
    "HELLO",
    handler
)

bus.publish(
    "HELLO",
    "MANAS Runtime"
)