# Deterministic Reflection Agent Project

## Problem Understanding

The goal of this assignment is to design a deterministic decision tree system that guides a user through structured daily reflection. The system must collect responses, navigate through predefined branches, and generate a meaningful summary based on behavioral signals. The reflection is structured across three psychological axes:

* Axis 1: Locus of Control (Internal vs External)
* Axis 2: Contribution vs Entitlement
* Axis 3: Perspective Radius (Self vs Others)

The challenge lies in designing a system that is Deterministic, both structured and scalable and capable of producing insightful summaries based on user input

## Approach

### Tree Design

The decision tree is implemented as a tabular structure (TSV) where each row represents a node. Each node contains:

* `id`: Unique identifier
* `parentId`: Defines hierarchy
* `type`: Node type (start, question, decision, reflection, bridge, summary, end)
* `text`: Content shown to user
* `options`: Possible responses
* `target`: Explicit jump (used in bridges)
* `signal`: Behavioral signal for scoring

The tree is divided into three sequential sections corresponding to the three axes.

### Node Types

Each node type has a specific role:

* **Start**: Entry point of the flow
* **Question**: Collects user input
* **Decision**: Routes based on answers
* **Reflection**: Provides contextual feedback
* **Bridge**: Transitions between axes
* **Summary**: Generates final output
* **End**: Terminates execution

This separation ensures modularity and clarity.

### Navigation Logic

Traversal is implemented using a loop-based execution model:

1. Start from `START`
2. At each node:

   * Display text
   * Collect or simulate response
   * Move to next node using:

     * `target` (for bridges)
     * `parent-child` relationship (for questions)

A key design decision was to prioritize `target` navigation over child traversal, ensuring correct handling of bridge nodes.

## Signal Processing

Each relevant node emits a signal mapped to one of the axes.

Example:

* `axis1:internal`
* `axis2:contribution`
* `axis3:other`

Signals are accumulated in a state dictionary:

```python
signals = {
  "axis1": {"internal": 0, "external": 0},
  "axis2": {"contribution": 0, "entitlement": 0},
  "axis3": {"self": 0, "other": 0}
}
```

At the end of traversal, the dominant value for each axis is computed using:

```python
max(values, key=values.get)
```

This enables deterministic summarization.

---

## Summary Generation

The summary node uses placeholders:

```
Today you showed {axis1.dominant} control,
leaned toward {axis2.dominant},
and focused on {axis3.dominant} impact.
```

These placeholders are dynamically replaced using computed dominant signals.

---

## Challenges and Fixes

### Infinite Loop Issue

Initial implementation caused loops due to:

* Falling back to child traversal after using `target`

Fix: Introduced `continue` after target assignment to prevent override.


### Data Consistency

Ensured:

* Unique node IDs
* No conflicting parent-target relationships
* Clean separation between navigation types


## Determinism and Guardrails

The system avoids hallucination by:

* Using a fully predefined structure
* Restricting outputs to templated summaries
* Eliminating randomness in traversal

All outputs are explainable and reproducible.


## Conclusion

This implementation demonstrates a robust approach to building structured reflective systems using decision trees. It combines:

* Clear architecture
* Deterministic logic
* Signal-based reasoning

The design is extensible and can be adapted to other domains requiring guided decision flows.
