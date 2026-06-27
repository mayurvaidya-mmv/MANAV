"""
Global settings.

Only non-secret configuration belongs here.

Secrets will eventually move to .env
"""

# LM Studio Server (Base URL only)
LOCAL_LLM_HOST = "http://127.0.0.1:1234"

# Model name (will become configurable later)
LOCAL_MODEL = "deepseek-r1-0528-qwen3-8b"

DEBUG = False