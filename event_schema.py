def create_event(data):

    # list of mandatory fields expected in input data
    # keeping it strict to avoid malformed events
    required = ["zone_id", "traffic_density", "violation_count", "timestamp", "trace_id"]

    # validate all required fields are present
    for r in required:
        if r not in data:
            raise ValueError(f"Missing field: {r}")  # fail fast if data is incomplete

    # construct standardized event object
    return {
        "zone_id": data["zone_id"],
        "traffic_density": data["traffic_density"],
        "violation_count": data["violation_count"],
        # derive congestion level based on simple threshold logic
        "congestion_level": "HIGH" if data["traffic_density"] > 50 else "LOW",
        "timestamp": data["timestamp"],
        "trace_id": data["trace_id"]
    }