from core.analysis import assess_water_demand, plan_water_distribution, prepare_shortage_response


def test_demand_missing_fields():
    result = assess_water_demand([], None, "")
    assert "available_supply" in result["missing_information"]
    assert result["record_count"] == 0


def test_demand_keeps_supplied_values():
    result = assess_water_demand([{"zone": "A", "demand": 50}], 100, "daily")
    assert result["available_supply"] == 100
    assert result["period"] == "daily"


def test_distribution_flags_incomplete_zone():
    result = plan_water_distribution([{"name": "Zone A"}], 100)
    assert result["incomplete_zones"][0]["missing_fields"] == ["demand", "priority"]


def test_distribution_includes_validation():
    result = plan_water_distribution([], 10)
    assert result["validation_required"]


def test_shortage_priority_order():
    result = prepare_shortage_response({}, [
        {"name": "Monitor", "priority": "low"},
        {"name": "Critical zone", "priority": "urgent"},
    ])
    assert result["response_options"][0]["name"] == "Critical zone"


def test_shortage_defaults():
    result = prepare_shortage_response({"description": "Low supply"}, [{"name": "Review"}])
    assert result["response_options"][0]["owner"] == "unspecified"
