"""
knowledge/models.py

Domain models used by MANAS.
"""

from dataclasses import dataclass, field


@dataclass
class ResearchResult:

    topic: str

    summary: str

    key_points: list[str] = field(default_factory=list)

    applications: list[str] = field(default_factory=list)

    references: list[str] = field(default_factory=list)

    next_topics: list[str] = field(default_factory=list)