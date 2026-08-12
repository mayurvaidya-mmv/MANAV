"""
MANAS Host Agent.

Runs on the host operating system and exposes
machine-level capabilities to MANAS.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from host.capabilities.applications import launch_application


app = FastAPI(
    title="MANAS Host Agent",
    version="0.1.0",
)


class ApplicationLaunchRequest(BaseModel):
    application: str


@app.get("/health")
def health():
    """Host Agent health check."""

    return {
        "status": "ok",
        "agent": "manas-host-agent",
        "version": "0.1.0",
    }


@app.post("/capabilities/application/launch")
def application_launch(
    request: ApplicationLaunchRequest,
):
    """Launch a Windows application."""

    launch_application(
        request.application
    )

    return {
        "success": True,
        "application": request.application,
    }