# MANAS

## Self-Extending AI Engineering Assistant

MANAS is a local-first, LLM-powered AI assistant being engineered toward
a **self-extending agent architecture**.

The long-term goal is not to build a fixed command-based assistant.
MANAS is designed around a capability system in which the Planner can
discover existing Skills, while a Meta-Agent can generate a new Skill
when a required capability is missing, subject to the Approval/Trust
layer.

> **Current status:** Active development --- V4 self-extending
> architecture\
> **Primary development branch:** `approach-b`

------------------------------------------------------------------------

## Why MANAS?

Traditional assistants become difficult to extend when every new
capability requires another hardcoded command, intent, dispatcher rule,
or executor branch.

MANAS is being engineered around a different model:

``` text
Traditional assistant
User
  ↓
Hardcoded command
  ↓
Hardcoded action
  ↓
Result
```

versus:

``` text
MANAS
User
  ↓
Intent
  ↓
Planner
  ↓
Skill Registry
  ↓
Existing Skill ────────────────┐
                               │
Missing Skill                  │
  ↓                            │
Meta-Agent                     │
  ↓                            │
Generate Skill                 │
  ↓                            │
Approval / Trust               │
  ↓                            │
Register + Persist             │
  └────────────────────────────┘
               ↓
        Action Dispatcher
               ↓
        Skill.execute()
               ↓
             Result
```

The architecture is designed so that MANAS can grow its capabilities
without requiring every future capability to be manually hardcoded into
the central dispatcher.

------------------------------------------------------------------------

# Architecture

The current MANAS architecture is **frozen V4 Self-Extending
Architecture**.

``` text
                         USER
                           │
                    Voice / Text
                           │
                           ▼
                     ┌───────────┐
                     │  Router   │
                     └─────┬─────┘
                           │
                           ▼
                  Intent Classifier
                           │
                           ▼
                     ┌───────────┐
                     │  Planner  │
                     └─────┬─────┘
                           │
                    Query SkillRegistry
                           │
              ┌────────────┴────────────┐
              │                         │
        Skill exists              Skill missing
              │                         │
              ▼                         ▼
      Create execution plan       Meta-Agent
              │                         │
              │                    LLM generates
              │                     new Skill
              │                         │
              │                    Approval Layer
              │                         │
              │                    Skill Registry
              │                         │
              │                      Save + Git
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                    ActionDispatcher
                           │
                     Approval / Trust
                           │
                           ▼
                    Skill.execute()
                           │
                           ▼
                         Result
                           │
                    ┌──────┴──────┐
                    ▼             ▼
             Knowledge Memory  Skill Memory
                Tier 1            Tier 2
```

## Architectural principles

-   The frozen V4 architecture is the source of truth.
-   Capabilities are represented as Skills.
-   Skills expose a common `BaseSkill` contract and metadata.
-   `SkillRegistry` dynamically discovers and manages Skills.
-   The Planner queries the available capabilities instead of relying
    only on fixed dispatch rules.
-   `MetaAgent` is responsible for capability generation when a required
    Skill is missing.
-   Generated capabilities pass through the Approval/Trust system.
-   Approved Skills are persisted and registered.
-   Git provides traceability for capability changes.
-   Runtime wires the services together.
-   Potentially destructive or consequential operations are controlled
    through approval tiers.
-   MANAS remains local-first; additional infrastructure is introduced
    only when it has a legitimate engineering purpose.

------------------------------------------------------------------------

# Complete Execution Flow

A normal request follows this conceptual flow:

``` text
User
 ↓
Router
 ↓
Intent Classifier
 ↓
Planner
 ↓
Skill Registry
 ↓
Find suitable Skill
 ↓
Execution Plan
 ↓
Action Dispatcher
 ↓
Approval / Trust
 ↓
Skill.execute()
 ↓
Result
```

When the required capability does not exist:

``` text
User
 ↓
Router
 ↓
Intent Classifier
 ↓
Planner
 ↓
Skill Registry
 ↓
Skill Missing
 ↓
Meta-Agent
 ↓
Design / Generate Skill
 ↓
Validate / Sanity Check
 ↓
Approval Layer
 ↓
Register Skill
 ↓
Persist + Git
 ↓
Planner Retry
 ↓
Action Dispatcher
 ↓
Approval / Trust
 ↓
Skill.execute()
 ↓
Result
```

------------------------------------------------------------------------

# Core Components

  -----------------------------------------------------------------------
  Component               Role                    Current status
  ----------------------- ----------------------- -----------------------
  Router                  Entry point for         Implemented
                          requests and intent     
                          routing                 

  Intent Classifier       Determines high-level   Implemented
                          intent                  

  Planner                 Converts intent/request In development toward
                          into an execution plan  fully dynamic planning

  Skill Registry          Discovers, loads,       Implemented
                          registers and searches  
                          Skills                  

  BaseSkill               Common Skill interface  Implemented
                          and metadata contract   

  Dynamic Dispatcher      Resolves a plan to the  Implemented
                          appropriate Skill       

  Approval Layer          Controls execution      Implemented
                          based on trust/risk     
                          tier                    

  Execution Engine        Provides execution      Implemented
                          infrastructure          

  Meta-Agent              Generates missing       In development/testing
                          capabilities            

  Capability Engine       Analysis, generation,   In development/testing
                          validation and          
                          registration pipeline   

  Runtime                 Wires MANAS services    Implemented
                          together                

  Memory                  Stores/persists project Basic infrastructure
                          knowledge and results   implemented

  Browser subsystem       Browser automation and  Implemented
                          page interaction        

  Research subsystem      Research workflow and   Implemented
                          provider integration    

  Voice subsystem         Offline speech          Implemented
                          input/output            

  Screen/Eyes subsystem   Future screen-aware     Planned/in development
                          interaction             

  Docker                  Reproducible deployment Next milestone
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Current Capabilities

## Implemented

### Local LLM integration

MANAS integrates with a locally hosted LLM through the existing AI
layer.

The current development setup has used **LM Studio** for local
inference.

### Intent classification

Natural-language requests can be classified and routed through the MANAS
intent system.

Example:

``` text
Research MQTT
```

can be routed into the research workflow.

### Research

MANAS contains a research subsystem capable of:

-   accepting research requests,
-   launching browser-based research workflows,
-   collecting research context,
-   using the LLM for summarization,
-   persisting research results.

Example:

``` text
Research MQTT
Research Doppler Effect
Research AWS IoT Core
```

### Browser automation

The browser subsystem includes Playwright-based browser interaction and
page-reading utilities.

### Voice input

MANAS supports offline speech recognition through Faster-Whisper.

``` text
Microphone
   ↓
Audio recording
   ↓
Whisper
   ↓
Text command
```

### Voice output

MANAS supports local speech synthesis through Piper.

``` text
MANAS response
   ↓
Piper
   ↓
Spoken response
```

### Skill Registry

The V4 Skill Registry is implemented and provides the
capability-discovery foundation.

### Dynamic dispatch

The Dispatcher can resolve work through the Skill Registry rather than
requiring every Skill to be manually wired into the dispatcher.

### Approval / Trust Layer

MANAS has an approval model for controlling actions according to their
risk.

Conceptually:

``` text
Tier 0 → automatic
Tier 1 → execute + log
Tier 2 → user approval
Tier 3 → explicit approval + confirmation
```

### Execution Engine

MANAS has a dedicated execution-engine component for controlled
execution.

### GitHub Actions CI

The project includes GitHub Actions CI for automated project
verification.

The current CI workflow installs the Python dependencies and performs
Python compilation checks.

------------------------------------------------------------------------

# Self-Extension Status

The self-extension architecture is the central V4 objective.

The repository contains:

``` text
brain/meta_agent.py
brain/capability_engine/
```

with components for capability analysis, generation, validation,
cleaning and registration.

The intended flow is:

``` text
Capability missing
       ↓
Meta-Agent
       ↓
Capability analysis
       ↓
Skill generation
       ↓
Validation
       ↓
Approval
       ↓
Registration
       ↓
Persistence
       ↓
Retry
```

### Current status

**The self-extension infrastructure is under active development and
testing.**

The existence of the generation pipeline does not mean that arbitrary
real-world tasks can already be handled autonomously. End-to-end
autonomous capability acquisition remains an active engineering
objective.

------------------------------------------------------------------------

# Memory Architecture

MANAS V4 distinguishes between two forms of memory:

``` text
                         RESULT
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
          Knowledge Memory        Skill Memory
             Tier 1                  Tier 2
```

### Tier 1 --- Knowledge Memory

Used for information MANAS has accumulated, such as research results and
project knowledge.

Current repository state includes persistent memory/knowledge
infrastructure.

Semantic vector/RAG memory is a future development area rather than
something claimed here as fully deployed.

### Tier 2 --- Skill Memory

Represents what MANAS can do.

The Skill Registry and skill manifest provide the foundation for this
layer.

Generated capabilities are intended to become persistent,
version-controlled Skills rather than temporary one-off actions.

------------------------------------------------------------------------

# Technology Stack

  -----------------------------------------------------------------------
  Area                                Technology
  ----------------------------------- -----------------------------------
  Language                            Python

  LLM                                 Local LLM via LM Studio

  Speech Recognition                  Faster-Whisper

  Speech Synthesis                    Piper

  Browser Automation                  Playwright

  AI / Agent Logic                    Custom Python architecture + LLM

  Skill System                        Custom `BaseSkill` + Skill Registry

  Memory                              Python-based persistent memory
                                      infrastructure; semantic memory
                                      planned

  Testing                             Python test suite

  Version Control                     Git / GitHub

  CI                                  GitHub Actions

  Deployment                          Docker --- next milestone

  Runtime Architecture                Modular Python services
  -----------------------------------------------------------------------

Technologies are introduced based on their purpose inside MANAS rather
than being added solely for resume value.

------------------------------------------------------------------------

# Project Structure

The repository is organized around the MANAS architecture:

``` text
MANAS/
│
├── ai/                  # AI / LLM integration
├── brain/               # Planning, Meta-Agent and capability engineering
├── browser/             # Browser automation
├── config/              # Configuration
├── core/                # Runtime, services, events, registry, execution
├── docs/                # Project documentation
├── ears/                # Audio/input components
├── eyes/                # Screen/vision components
├── hands/               # Action and execution components
├── knowledge/           # Knowledge models/parsing
├── memory/              # Persistent memory
├── models/              # Data/model structures
├── mouth/               # Output components
├── research/            # Research subsystem
├── resources/           # Project resources
├── router/              # Routing, classification and planning
├── scripts/             # Utility scripts
├── skills/              # MANAS capabilities
├── tests/               # Automated tests
├── voice/               # Voice input/output
│
├── .github/
│   └── workflows/       # GitHub Actions CI
│
├── main.py              # Text interface
├── voice.py             # Voice interface
├── requirements.txt     # Python dependencies
└── README.md
```

------------------------------------------------------------------------

# Running MANAS

## Requirements

Current development is Python-based.

You will need:

-   Python 3.13
-   Git
-   A local LLM runtime such as LM Studio
-   A compatible local model
-   Python dependencies from `requirements.txt`

Voice functionality additionally requires the local Whisper/Piper assets
used by the project.

------------------------------------------------------------------------

## Installation

Clone the repository and enter the project:

``` bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd MANAS
```

Create a virtual environment:

### Windows

``` powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# Configuration

MANAS uses project configuration files for non-secret settings.

If external services require credentials or API keys, keep them outside
Git-tracked source files.

Use an environment file for secrets:

``` text
.env
```

Do **not** commit secrets to GitHub.

A future `.env.example` will document required variables without
exposing credentials.

------------------------------------------------------------------------

# Running the Text Interface

From the project root:

``` bash
python main.py
```

Example interaction:

``` text
MANAS AI Runtime

You: Research MQTT
```

MANAS routes the request through its AI/router/research pipeline and
returns the resulting research summary.

------------------------------------------------------------------------

# Running the Voice Interface

``` bash
python voice.py
```

Conceptually:

``` text
Microphone
    ↓
Audio Recorder
    ↓
Faster-Whisper
    ↓
MANAS Runtime
    ↓
Skill / Research / Action
    ↓
Piper
    ↓
Speaker
```

------------------------------------------------------------------------

# Example Interactions

Current demonstrated workflows include requests such as:

``` text
Research MQTT
Research Doppler Effect
Open Chrome
```

The exact capabilities available depend on the current registered Skills
and the implementation status of the relevant subsystem.

MANAS should **not** be interpreted as already supporting arbitrary
natural-language computer tasks simply because the V4 architecture is
designed to eventually support them.

------------------------------------------------------------------------

# Development Status

## V4 Milestones

``` text
V4.0      Foundation                         ✅
V4.0.1    GitHub Actions CI                  ✅
V4.2      Skill Registry                     ✅
V4.3      Dynamic Dispatcher                 ✅
V4.5      Approval Layer                     ✅
Epic 1    Execution Engine                   ✅
          Self-extension infrastructure      🟡
          Fully autonomous capability loop   🟡
          Public documentation               🚧
          Docker support                     → Next
```

MANAS is an actively developed engineering project. The implementation
intentionally progresses incrementally rather than presenting unfinished
capabilities as complete.

------------------------------------------------------------------------

# Testing and CI

The repository contains automated tests covering multiple MANAS
components, including areas such as:

-   Runtime infrastructure
-   Configuration
-   Logging
-   Event Bus
-   Router
-   Intent classification
-   Skill Registry
-   Approval Layer
-   Execution
-   Meta-Agent/capability generation
-   Browser integration
-   Memory
-   Voice components

Run the test suite with:

``` bash
python -m pytest
```

GitHub Actions provides continuous integration for repository changes.

The current CI workflow performs dependency installation and Python
project verification.

------------------------------------------------------------------------

# Security and Trust

MANAS can eventually execute operations on the host computer, so
unrestricted execution is not treated as a safe default.

The V4 architecture therefore includes an Approval/Trust Layer.

The intended model is:

``` text
Low-risk action
     ↓
Automatic execution

Consequential action
     ↓
User approval

Irreversible / high-risk action
     ↓
Explicit approval + confirmation
```

Potentially destructive or system-level capabilities should remain
behind the appropriate approval boundary.

Generated Skills are also intended to be validated, approved, persisted
and version-controlled.

------------------------------------------------------------------------

# Current Limitations

MANAS is **not yet a general-purpose autonomous computer agent**.

Current limitations include:

-   Arbitrary natural-language tasks are not universally supported.
-   Fully autonomous Skill generation and execution is still under
    development/testing.
-   General-purpose dynamic planning is still evolving.
-   Continuous background operation is not yet the finished target.
-   Full screen understanding/vision is not yet a completed capability.
-   Semantic/RAG memory is not yet presented as fully implemented.
-   General desktop automation across arbitrary applications remains
    under development.
-   Docker support is the next deployment milestone.

These limitations are intentional engineering boundaries, not hidden
from the project documentation.

------------------------------------------------------------------------

# Roadmap

The immediate development sequence is:

``` text
README / Public Documentation
        ↓
Docker
        ↓
Linux integration/support
        ↓
Strong tool/skill execution
        ↓
Controlled tool calling
        ↓
Knowledge Memory / Tier 1
        ↓
Skill Memory / Tier 2
        ↓
RAG where architecturally appropriate
        ↓
Evaluation framework
        ↓
Observability / logging improvements
        ↓
Error handling / retry mechanisms
        ↓
API layer where justified
        ↓
Linux service / deployment
        ↓
Remote automation where useful
        ↓
Cloud / AWS integration where useful
        ↓
Extensibility improvements
        ↓
Open-source preparation
```

Kubernetes is **not currently required**. It will only be evaluated if
MANAS becomes a genuinely distributed system where orchestration
provides a real architectural or operational benefit.

------------------------------------------------------------------------

# Engineering Philosophy

MANAS is being developed around a few principles:

1.  **Architecture first** --- the frozen V4 architecture is the source
    of truth.
2.  **Incremental implementation** --- build and verify one meaningful
    milestone at a time.
3.  **Working features over feature count** --- incomplete capabilities
    are not presented as finished.
4.  **Preserve working functionality** --- existing components are
    reused when they already satisfy the architecture.
5.  **Controlled autonomy** --- autonomous reasoning does not mean
    unrestricted execution.
6.  **Version-controlled self-extension** --- capability growth should
    remain traceable.
7.  **Local-first design** --- local inference and local execution
    remain important parts of the project.
8.  **Purposeful technology choices** --- technologies are introduced
    because they solve an engineering problem.
9.  **Test before claiming** --- documented capabilities should
    correspond to actual implementation/testing.
10. **Professional Git workflow** --- meaningful milestones are tested,
    documented, committed and pushed.

------------------------------------------------------------------------

# Git / Development Workflow

The current development workflow is:

``` text
Implement
   ↓
Local testing
   ↓
Documentation
   ↓
Git commit
   ↓
Git push
   ↓
GitHub Actions CI
```

The active development branch for the current V4 work is:

``` text
approach-b
```

Meaningful changes are kept as separate milestones rather than being
bundled into unrelated commits.

------------------------------------------------------------------------

# Screenshots / Demo

> **Demo media placeholder**

Screenshots and GIF/video demonstrations will be added as they become
available.

Potential future demonstrations:

-   MANAS voice interaction
-   Research workflow
-   Browser automation
-   Skill discovery
-   Skill generation
-   Approval flow
-   Capability registration
-   Self-extension workflow

------------------------------------------------------------------------

# Open Source / License

MANAS is currently maintained as a **public GitHub project**, but no
open-source license is claimed here until one is deliberately selected
and added to the repository.

For now, the priority is:

> **Public + understandable + runnable + documented + professionally
> engineered.**

A formal contribution/open-source workflow can be introduced later when
the project reaches an appropriate level of stability.

------------------------------------------------------------------------

# Project Vision

The long-term vision for MANAS is a capable personal AI engineering
environment that can:

``` text
Understand goals
      ↓
Reason about tasks
      ↓
Discover capabilities
      ↓
Use existing Skills
      ↓
Identify missing capabilities
      ↓
Generate new Skills
      ↓
Request approval when necessary
      ↓
Execute safely
      ↓
Persist new capabilities
      ↓
Continue improving
```

The project is intentionally being built toward this vision
incrementally.

------------------------------------------------------------------------

## Status

**MANAS V4 --- Active Development**

Built as a practical engineering project combining:

**Python · AI/LLMs · Agent Architecture · Tool/Skill Systems · Browser
Automation · Voice Interfaces · Software Architecture · Testing ·
Git/GitHub · CI/CD · Automation**
