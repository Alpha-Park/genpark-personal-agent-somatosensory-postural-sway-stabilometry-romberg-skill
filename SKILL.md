---
name: genpark-personal-agent-somatosensory-postural-sway-stabilometry-romberg-skill
version: 1.0.0
description: Calculates force platform 95% confidence ellipse sway area, mean velocity, and Romberg Quotient (Area_EC / Area_EO).
license: Apache-2.0
compatibility:
  python: ">=3.9"
  openclaw: ">=1.0.0"
  mcp: ">=1.0.0"
---

# Somatosensory Postural Sway & Center of Pressure (COP) Stabilometry Skill

A zero-dependency personal agent skill for evaluating postural equilibrium, sensorimotor integration, and differentiating sensory ataxia from cerebellar dysfunction via force platform Romberg stabilometry.

## Features
- **95% Confidence Ellipse Area ($Area_{95}$)**: Quantifies total spatial dispersion of center of pressure sway in $mm^2$.
- **Mean Sway Velocity ($V_{\text{sway}}$)**: Measures neuromuscular postural correction velocity in $mm/s$.
- **Romberg Quotient ($RQ$)**: Computes ratio of eyes-closed to eyes-open sway area to evaluate visual compensation.
- **Ataxia Differential Diagnosis**: Separates proprioceptive sensory ataxia ($RQ > 3.0$) from cerebellar vermian midline ataxia ($Area_{\text{EO}} > 450\text{ mm}^2, RQ \le 1.8$) and normal stability.

## MCP Server Integration
Exposes `evaluate_stabilometry` for personal fall risk screening, neurological wellness, and balance optimization.
