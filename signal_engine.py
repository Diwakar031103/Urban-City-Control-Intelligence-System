# UCCIS Signal Engine
# This module calculates traffic signal timing based on traffic density

def compute_signal_plan(zone_snapshot):

    # Dictionary to store final signal timings for each zone
    signal_plan = {}

    # Step 1: Calculate green signal time for each zone
    for zone_id, data in zone_snapshot.items():

        # Get traffic density for current zone (default = 0 if missing)
        density = data.get("traffic_density", 0)

        # Convert traffic density into green time (basic linear mapping)
        green_time = density * 3

        # Apply minimum green time constraint
        if green_time < 10:
            green_time = 10
        # Apply maximum green time constraint
        elif green_time > 60:
            green_time = 60

        # Store initial signal configuration for the zone
        signal_plan[zone_id] = {
            "traffic_density": density,
            "green_time": green_time,
            "red_time": 0
        }

    # Step 2: Calculate total cycle time (sum of all green times)
    total_cycle = sum(v["green_time"] for v in signal_plan.values())

    # Step 3: Calculate red time for each zone
    # Red time = remaining cycle time when other zones are green
    for zone_id in signal_plan:
        signal_plan[zone_id]["red_time"] = total_cycle - signal_plan[zone_id]["green_time"]

    # Return final signal plan with timing for all zones
    return signal_plan