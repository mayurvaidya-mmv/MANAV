from enum import Enum


class AIProvider(Enum):
    LMSTUDIO = "lmstudio"
    OPENAI = "openai"
    OLLAMA = "ollama"
    CLAUDE = "claude"