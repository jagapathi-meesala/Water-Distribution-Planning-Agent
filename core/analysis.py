from typing import Any, Dict, List


def assess_water_demand(
    demand_records: List[Dict[str, Any]],
    available_supply: Any = None,
    period: str = "",
) -> Dict[str, Any]:
    records = list(demand_records or [])
    missing = []
    if not records:
        missing.append("demand_records")
    if available_supply is None:
        missing.append("available_supply")
    if not period:
        missing.append("period")
    return {
        "record_count": len(records),
        "demand_records": records,
        "available_supply": available_supply,
        "period": period or "Not supplied",
        "missing_information": missing,
        "note": "Units and time periods must be consistent before comparing demand and supply.",
    }


def plan_water_distribution(
    zones: List[Dict[str, Any]],
    available_supply: Any,
    constraints: List[str] = None,
) -> Dict[str, Any]:
    zones = list(zones or [])
    constraints = list(constraints or [])
    incomplete = []
    for index, zone in enumerate(zones):
        zone = dict(zone or {})
        missing_fields = [
            field for field in ("name", "demand", "priority")
            if zone.get(field) is None or zone.get(field) == ""
        ]
        if missing_fields:
            incomplete.append({
                "zone": zone.get("name", f"zone-{index + 1}"),
                "missing_fields": missing_fields,
            })
    return {
        "zones_received": zones,
        "available_supply": available_supply,
        "constraints": constraints,
        "incomplete_zones": incomplete,
        "validation_required": [
            "Confirm consistent units and planning period.",
            "Validate allocation against network capacity and hydraulic model.",
            "Check water quality and applicable local requirements.",
        ],
        "note": "This structures a candidate plan; it does not calculate or certify hydraulic feasibility.",
    }


def prepare_shortage_response(
    shortage: Dict[str, Any],
    options: List[Dict[str, Any]],
) -> Dict[str, Any]:
    shortage = dict(shortage or {})
    options = list(options or [])
    rank = {"urgent": 0, "high": 1, "medium": 2, "low": 3}
    indexed = list(enumerate(options))
    indexed.sort(key=lambda pair: (
        rank.get(str((pair[1] or {}).get("priority", "")).lower(), 4),
        pair[0],
    ))
    ordered = []
    for _, option in indexed:
        item = dict(option or {})
        item.setdefault("owner", "unspecified")
        item.setdefault("duration", "unspecified")
        item.setdefault("status", "needs-review")
        ordered.append(item)
    return {
        "shortage_summary": shortage.get("description", "Not supplied"),
        "response_options": ordered,
        "missing_information": [
            key for key in ("affected_zones", "estimated_duration", "available_supply")
            if not shortage.get(key)
        ],
        "review_note": "Coordinate emergency actions with responsible local authorities and qualified professionals.",
    }
