# Explainability

## Inputs and Data Sources

The agent accepts caller-provided demand, available supply, storage, distribution zones, delivery constraints, priority groups, and shortage-response options. It does not access live telemetry, reservoir systems, water-quality systems, or geographic networks.

## Decision and Reasoning

The agent organizes supplied values, checks whether key fields are present, and structures candidate plans using supplied priorities. It does not infer missing flow rates, calculate hydraulic feasibility, or independently validate safety.

## Limits and Constraints

The agent does not run hydraulic network simulations, verify water quality, access live infrastructure, or certify operational plans. Real deployments require accurate measurements, local rules, engineering review, and public-health oversight.

## assess-water-demand

### Inputs
Demand records, population or zone descriptions, time period, and available supply.

### Data Sources
Caller-provided information only.

### Decision
Checks whether demand, supply, and period information are present and returns supplied totals without inventing missing values.

### Outputs
Demand summary, supplied figures, and missing fields.

### Failure Handling
Missing or ambiguous values are flagged.

### Limits
No demand forecasting or engineering validation.

## plan-water-distribution

### Inputs
Zones, available supply, demand, priorities, and constraints.

### Data Sources
Caller-provided information only.

### Decision
Organizes proposed zone allocations and identifies whether the required planning fields are present.

### Outputs
Structured candidate plan and validation warnings.

### Failure Handling
Incomplete zone records are preserved and flagged.

### Limits
No hydraulic feasibility, pressure, or water-quality determination.

## prepare-shortage-response

### Inputs
Shortage description, supplied response options, priorities, and constraints.

### Data Sources
Caller-provided information only.

### Decision
Orders response options by explicitly supplied priority and lists validation tasks.

### Outputs
Ordered response options and information gaps.

### Failure Handling
Unknown owners, durations, or quantities remain unspecified.

### Limits
Emergency decisions require responsible local authorities and qualified professionals.

## Traceability

Plan observations map to caller-provided fields and options.

## Transparency

The agent distinguishes supplied values, missing information, and proposed actions.

## Reproducibility

The core is deterministic for identical inputs.

## Safety

The agent does not present preliminary plans as engineering approval or proof of water safety.
