"""
Knowledge Models

Models used by MANAS.
"""

from dataclasses import dataclass, field
from datetime import datetime


# -------------------------------------------------------------------
# Temporary result returned by the AI
# -------------------------------------------------------------------

@dataclass
class ResearchResult:

    topic: str

    summary: str


# -------------------------------------------------------------------
# Persistent knowledge stored in memory
# -------------------------------------------------------------------

@dataclass
class Knowledge:

    topic: str

    summary: str

    tags: list = field(default_factory=list)

    source: str = "Perplexity"

    created: str = datetime.now().strftime("%Y-%m-%d")