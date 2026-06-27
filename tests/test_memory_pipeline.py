from memory.memory_manager import MemoryManager

memory = MemoryManager()

topic = "mqtt"

print("Exists:", memory.exists(topic))

knowledge = memory.load(topic)

print()

print(knowledge)