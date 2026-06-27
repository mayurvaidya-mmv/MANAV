"""
Test memory existence.
"""

from memory.memory_manager import MemoryManager

memory = MemoryManager()

for topic in [

    "MQTT",

    "MODBUS",

    "UDP",

    "SomethingThatDoesNotExist"

]:

    print(

        f"{topic:30} ->",

        memory.exists(topic)

    )