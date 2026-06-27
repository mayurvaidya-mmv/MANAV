"""
Knowledge Parser
"""

from knowledge.models import ResearchResult


class KnowledgeParser:

    def parse_summary(self, text: str) -> ResearchResult:

        topic = "Unknown"

        summary = text.strip()

        if "Topic:" in text:

            lines = text.splitlines()

            for i, line in enumerate(lines):

                if line.startswith("Topic:"):

                    topic = line.replace("Topic:", "").strip()

                if line.startswith("Summary:"):

                    summary = "\n".join(lines[i + 1:]).strip()

                    break

        return ResearchResult(

            topic=topic,

            summary=summary

        )