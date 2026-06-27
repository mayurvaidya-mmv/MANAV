"""
Test the Memory Manager.
"""

from knowledge.models import Knowledge
from memory.memory_manager import MemoryManager


memory = MemoryManager()

knowledge = Knowledge(

    topic="MQTT",

    summary="MQTT is a lightweight publish-subscribe messaging protocol."

)

path = memory.save(knowledge)

print()

print("=" * 60)

print("Knowledge saved successfully!")

print(path)

print("=" * 60)