"""
intent_types.py

Defines the categories the router classifies every incoming request into.

Two groups, handled differently by the router (see Phase 0 decision):

1. PATTERN_MATCH categories — checked first, via simple keyword/regex
   matching, BEFORE any LLM call. These are meta-control over the
   assistant itself, not requests that need reasoning.

2. LLM_CLASSIFIED categories — checked only if no pattern match is
   found. These require an LLM (local or cloud) to classify, because
   they depend on understanding the meaning of the request.
"""

# --- Checked first, no LLM involved ---
SYSTEM = "system"          # e.g. "Switch to local mode.", "Use GPT-5.5."
EXIT = "exit"               # e.g. "Sleep.", "Good night JARVIS."

# --- Checked second, via LLM classification ---
CHAT = "chat"                       # e.g. "Explain MQTT."
RESEARCH = "research"               # e.g. "Research silicon carbide MOSFETs."
ACTION = "action"                   # e.g. "Open KiCad."
SCREEN_CONTEXT = "screen_context"   # e.g. "Explain this error."
MEMORY_LOOKUP = "memory_lookup"     # e.g. "What AWS services did I use?"
TASK_DELEGATE = "task_delegate"     # e.g. "Open the PDF and summarize it."

PATTERN_MATCH_CATEGORIES = [SYSTEM, EXIT]

LLM_CLASSIFIED_CATEGORIES = [
    CHAT,
    RESEARCH,
    ACTION,
    SCREEN_CONTEXT,
    MEMORY_LOOKUP,
    TASK_DELEGATE,
]

ALL_CATEGORIES = PATTERN_MATCH_CATEGORIES + LLM_CLASSIFIED_CATEGORIES