"""
Capability Analysis Report
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class CapabilityReport:

    goal: str

    existing_skills: List[str] = field(default_factory=list)

    missing_capabilities: List[str] = field(default_factory=list)

    suggested_skill: str = ""

    estimated_complexity: str = "Unknown"

    status: str = "UNKNOWN"