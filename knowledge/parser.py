"""
knowledge/parser.py
"""

from knowledge.models import ResearchResult


class KnowledgeParser:

    def parse_summary(self, text: str) -> ResearchResult:

        return ResearchResult(

            topic="Unknown",

            summary=text.strip()
        )