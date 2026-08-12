"""
Global settings.

Non-secret configuration can be provided through environment variables.
Secrets should be stored in .env or the host environment.
"""

import os

from dotenv import load_dotenv

load_dotenv()


# ==========================
# Local LLM
# ==========================

LOCAL_LLM_HOST = os.getenv(
    "LOCAL_LLM_HOST",
    "http://127.0.0.1:1234"
)

LOCAL_MODEL = os.getenv(
    "LOCAL_MODEL",
    "deepseek-r1-0528-qwen3-8b"
)

DEBUG = os.getenv(
    "DEBUG",
    "False"
).lower() == "true"


# ==========================
# Whisper
# ==========================

WHISPER_MODEL = os.getenv(
    "WHISPER_MODEL",
    "base"
)

WHISPER_DEVICE = os.getenv(
    "WHISPER_DEVICE",
    "cpu"
)

WHISPER_COMPUTE_TYPE = os.getenv(
    "WHISPER_COMPUTE_TYPE",
    "int8"
)