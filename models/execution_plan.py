"""
Execution Plan

Represents a parsed task
ready for execution.
"""

from dataclasses import dataclass, field


@dataclass
class ExecutionPlan:

    intent: str

    task: str

    arguments: dict = field(default_factory=dict)