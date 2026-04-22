# Reflection Tree Diagram

This diagram represents the deterministic flow across three axes:
- Axis 1: Locus of Control
- Axis 2: Contribution vs Entitlement
- Axis 3: Perspective Radius

```mermaid
graph TD
START --> A1_OPEN
A1_OPEN --> A1_D1
A1_D1 --> A1_Q_HIGH
A1_D1 --> A1_Q_LOW
A1_Q_HIGH --> A1_Q2 --> A1_R_INT
A1_Q_LOW --> A1_Q2B --> A1_R_EXT
A1_R_INT --> A2_OPEN
A1_R_EXT --> A2_OPEN
A2_OPEN --> A2_D1
A2_D1 --> A2_Q_HIGH --> A2_R_CON
A2_D1 --> A2_Q_LOW --> A2_R_ENT
A2_R_CON --> A3_OPEN
A2_R_ENT --> A3_OPEN
A3_OPEN --> A3_Q1 --> A3_Q2 --> A3_D1
A3_D1 --> A3_R_SELF
A3_D1 --> A3_R_OTHER
A3_R_OTHER --> SUMMARY --> END