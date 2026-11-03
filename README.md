# Somatosensory Postural Sway & Center of Pressure (COP) Stabilometry Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard-green.svg)](https://modelcontextprotocol.io/)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)](requirements.txt)
[![Status: Production-Ready](https://img.shields.io/badge/status-production--ready-success.svg)](https://github.com/alphaparkinc)

A zero-dependency, mathematically rigorous personal agent skill that evaluates static postural stability, center of pressure dynamics, and sensory ataxia via Romberg force platform stabilometry.

## Architecture

```mermaid
flowchart TD
    A[Force Platform Transducers] --> B[Center of Pressure Coordinates X, Y]
    B --> C[Compute 95% Confidence Ellipse Area & Sway Velocity]
    C --> D[Record Trials: Eyes Open vs Eyes Closed]
    D --> E[Compute Romberg Quotient RQ = Area_EC / Area_EO]
    E --> F[Ataxia Classification: Sensory vs Cerebellar vs Vestibular]
```

## Quick Start

```python
from client import PosturalSwayStabilometryClient

client = PosturalSwayStabilometryClient()
result = client.evaluate_stabilometry(
    sway_area_eyes_open_mm2=115.0,
    sway_area_eyes_closed_mm2=205.0,
    sway_velocity_eyes_open_mm_s=8.2,
    sway_velocity_eyes_closed_mm_s=11.5
)
print("Romberg Quotient:", result["stabilometric_kinetics"]["romberg_quotient_area"])
print("Balance Status:", result["clinical_postural_assessment"]["balance_classification"])
```

## License
Apache-2.0
