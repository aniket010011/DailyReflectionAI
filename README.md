# Daily Reflection Tree (Deterministic AI System)

## Overview

This project implements a **deterministic decision tree-based reflection system** that guides users through structured introspection and generates insights based on their responses.

The system operates across three behavioral axes:

* Locus of Control (Internal vs External)
* Contribution vs Entitlement
* Perspective Radius (Self vs Others)

---

## Project Structure

```
project/
│
├── tree/
│   ├── reflection-tree.tsv
│   └── tree-diagram.md
│
├── agent/
│   └── app.py
│
├── transcripts/
│   ├── persona1.md
│   └── persona2.md
│
├── write-up.md
└── README.md
```

---

## How It Works

1. The decision tree is defined in a TSV file.
2. Each node represents a step in the reflection process.
3. The agent traverses the tree based on user input.
4. Signals are collected during traversal.
5. A final summary is generated using dominant signals.

---

## Running the Project

### Navigation to folder

```bash
cd DailyReflectionAI/agent
```


### Running the application

```bash
python app.py
```


## Example Output

```
Today you showed internal control,
leaned toward contribution,
and focused on other impact.
```


## Design Highlights

* Fully deterministic (no randomness)
* Modular node structure
* Explicit control flow using parent-child + target links
* Signal-based reasoning system
* Clean separation of logic and data


## Guardrails Against Hallucination

* No generative AI used in runtime
* All outputs are predefined templates
* Strict traversal rules ensure consistency


## Author

Aniket Sengupta
