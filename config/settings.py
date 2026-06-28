"""
Global settings.

Only non-secret configuration belongs here.

Secrets will eventually move to .env
"""
from core.config import Config

# LM Studio Server (Base URL only)
LOCAL_LLM_HOST = "http://127.0.0.1:1234"

# Model name (will become configurable later)
LOCAL_MODEL = "deepseek-r1-0528-qwen3-8b"

DEBUG = False

# ==========
# Whisper
# ==========

WHISPER_MODEL = "base"

WHISPER_DEVICE = "cpu"

WHISPER_COMPUTE_TYPE = "int8"