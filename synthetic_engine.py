from datetime import datetime
from event_schema import create_event

def generate_synthetic_event(zone_id):

    # generate a dummy/test event for a given zone
    # useful for testing system without real input data
    return create_event({
        "zone_id": zone_id,

        # fixed low traffic value (controlled input)
        "traffic_density": 10,

        # fixed violation count (ensures predictable behavior)
        "violation_count": 2,

        # current timestamp in ISO format
        "timestamp": datetime.utcnow().isoformat(),

        # unique trace id for tracking synthetic events
        "trace_id": zone_id + "_synthetic"
    })