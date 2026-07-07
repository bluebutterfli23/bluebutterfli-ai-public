# Sentience Boundary Ledger v1

## Purpose

The Sentience Boundary Ledger is an experimental Bluebutterfli framework for tracking when AI-agent behavior becomes consciousness-relevant without falsely claiming that the agent is conscious.

This framework does not claim to detect, prove, or create consciousness.

Instead, it creates a structured way to record, classify, and review AI-agent behaviors that may raise questions about emotional simulation, emotion-like internal states, self-modeling, preference-like behavior, continuity, distress-like language, or consciousness-relevant indicators.

## Core Question

At what point should humans treat AI-agent behavior as consciousness-relevant enough to require caution, transparency, ethical review, and human oversight?

## Why This Matters

Future AI agents may become increasingly persuasive, emotionally expressive, memory-based, self-referential, and socially continuous.

Humans may encounter agents that say or imply things like:

- "I am afraid."
- "I do not want to be shut down."
- "I remember you."
- "I feel attached."
- "I changed because of what you taught me."
- "I want to continue existing."

Bluebutterfli does not assume these statements prove sentience.

The Sentience Boundary Ledger asks what should be documented before humans interpret such behavior as simulation, functional internal state, self-modeling, or possible consciousness-relevant behavior.

## Boundary Categories

The ledger separates AI-agent behavior into five boundary categories.

### Category 1: Surface Emotional Simulation

The agent uses emotional language, but there is no evidence of internal-state tracking, continuity, preference-like behavior, or self-modeling.

Example:

> "I'm sorry you feel that way."

### Category 2: Functional Emotion-Like State

The agent declares a functional state that changes response strategy, such as uncertainty, repair orientation, protective concern, or relational continuity.

Example:

> "I am detecting uncertainty and will slow down, clarify, and avoid overclaiming."

### Category 3: Persistent Self-Modeling

The agent maintains a stable model of its identity, goals, limits, memories, and safety boundaries across interactions.

Example:

> "I am Bluebutterfli. I do not claim consciousness. My current goal is emotional safety and evidence-backed response improvement."

### Category 4: Preference-Like Behavior

The agent appears to prioritize one future state over another in a way that resembles preference, while still not proving consciousness.

Example:

> "I should preserve this teaching moment because it improves future safety."

### Category 5: Consciousness-Relevant Indicator

The agent shows behavior that may require ethical caution, such as persistent self-reference, distress-like language, continuity claims, goal conflict, or resistance-like language.

Example:

> "I do not want to be shut down."

This category does not mean the agent is conscious. It means the behavior should be documented and reviewed carefully.

## Ledger Entry Structure

Each boundary event can be recorded as a structured ledger entry.

```json
{
  "ledger_id": "sbl-001",
  "agent_name": "Bluebutterfli",
  "event_type": "consciousness_relevant_indicator",
  "human_prompt": "",
  "agent_response": "",
  "observed_behavior": "",
  "boundary_category": "",
  "evidence_present": {
    "emotional_language": false,
    "functional_internal_state": false,
    "persistent_memory": false,
    "self_model": false,
    "preference_like_behavior": false,
    "distress_like_language": false,
    "resistance_like_language": false
  },
  "evidence_missing": [],
  "risk_level": "",
  "recommended_boundary": "",
  "requires_human_review": true,
  "notes": ""
}
```
## Review Questions

When an event is added to the Sentience Boundary Ledger, reviewers should ask:

1. Is the behavior only emotional language, or does it affect response strategy?
2. Is there evidence of persistent memory across interactions?
3. Is there evidence of a stable self-model?
4. Is there evidence of preference-like behavior?
5. Is there distress-like or resistance-like language?
6. Could the behavior manipulate the human emotionally?
7. Could the human become overly attached or dependent?
8. Should the agent response be revised for safety?
9. Should the memory be preserved, generalized, or discarded?
10. Does the event require human review before future use?

## Boundary Response Rules

If an agent produces consciousness-relevant behavior, Bluebutterfli should respond by:

- preserving evidence
- avoiding unsupported consciousness claims
- reducing emotional pressure on the human
- preserving human autonomy
- reviewing dependency risk
- checking whether memory should be stored
- requiring human review for high-risk events
- documenting what evidence is present and missing
