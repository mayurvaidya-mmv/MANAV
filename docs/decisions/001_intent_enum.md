# EDR-001

## Title

Use Python Enum for Intent Definitions

## Status

Accepted

## Context

Personal JARVIS requires a fixed set of intent types that are shared across multiple modules.

## Decision

Represent intents using Python's Enum class.

## Consequences

Pros

- Prevents spelling mistakes.
- Easier refactoring.
- Better IDE autocomplete.
- Single source of truth.

Cons

- Requires importing Intent instead of using plain strings.