"""
Test memory loading.
"""

from memory.memory_manager import MemoryManager

memory = MemoryManager()

knowledge = memory.load("MQTT")

print()

if knowledge is None:

    print("Not found.")

else:

    print("=" * 60)

    print("Topic:", knowledge.topic)

    print()

    print("Summary:")

    print(knowledge.summary)

    print("=" * 60)