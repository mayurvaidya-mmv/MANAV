"""
Memory Manager

Handles persistent knowledge storage.
"""

import json
from pathlib import Path
from dataclasses import asdict

from knowledge.models import Knowledge


class MemoryManager:

    def __init__(self):

        self.memory_path = Path("memory/knowledge")

        self.memory_path.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, knowledge: Knowledge):

        filename = knowledge.topic.lower().replace(" ", "_") + ".json"

        filepath = self.memory_path / filename

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                asdict(knowledge),
                file,
                indent=4,
                ensure_ascii=False
            )

        return filepath

    def load(self, topic: str):

        filename = topic.lower().replace(" ", "_") + ".json"

        filepath = self.memory_path / filename

        if not filepath.exists():

            return None

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return Knowledge(**data)
    
    def exists(self, topic: str):

        filename = topic.lower().replace(" ", "_") + ".json"

        filepath = self.memory_path / filename

        return filepath.exists()