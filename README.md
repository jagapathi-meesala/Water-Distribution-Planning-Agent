# Water Distribution Planning Agent

An OpenGAP-compatible, framework-independent agent for organizing water demand and distribution planning from caller-provided data.

## Capabilities
- Summarize demand and available supply information
- Identify missing data needed for distribution planning
- Organize candidate distribution plans and constraints
- Prepare shortage-response options
- Track assumptions, dependencies, and follow-up checks

## Run locally

```bash
pytest -q
python3 verification/readiness_audit.py
opengap validate
```

No external APIs, live telemetry, hydraulic simulation, or water-quality testing is included. Outputs are preliminary planning support and require engineering and public-health review before operational use.
