from collections import deque

# maintains recent history of events per zone (sliding window)
zone_history = {}

WINDOW = 5  # number of recent events to consider

def compute_zone_metrics(zone_id, event):

    # initialize deque for zone if not already present
    # deque with maxlen automatically removes oldest entries
    zone_history.setdefault(zone_id, deque(maxlen=WINDOW))

    # add latest event to history
    zone_history[zone_id].append(event)

    # convert deque to list for easier processing
    h = list(zone_history[zone_id])

    # calculate average traffic density over recent window
    avg_traffic = sum(e["traffic_density"] for e in h) / len(h)

    # calculate average violations over recent window
    avg_violation = sum(e["violation_count"] for e in h) / len(h)

    # determine traffic trend based on first vs latest value
    trend = "STABLE"
    if len(h) > 1:
        if h[-1]["traffic_density"] > h[0]["traffic_density"]:
            trend = "INCREASING"
        elif h[-1]["traffic_density"] < h[0]["traffic_density"]:
            trend = "DECREASING"

    # compute overall risk score using weighted formula
    # traffic has weight 2, violations have higher impact (weight 3)
    risk_score = avg_traffic * 2 + avg_violation * 3

    # return computed metrics
    return {
        "avg_traffic": avg_traffic,
        "avg_violation": avg_violation,
        "trend": trend,
        "risk_score": risk_score
    }