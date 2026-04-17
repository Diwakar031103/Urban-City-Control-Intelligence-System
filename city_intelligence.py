def compute_city_state(zone_metrics):

    total = 0
    zone_scores = {}

    # loop through each zone and extract its risk score
    for z, m in zone_metrics.items():
        # ensure valid data exists and contains metrics
        if m and "metrics" in m:
            zone_scores[z] = m["metrics"]["risk_score"]
            total += m["metrics"]["risk_score"]  # accumulate total risk

    # handle case where no valid zone data is available
    if not zone_scores:
        return {
            "city_risk_score": 0,
            "critical_zones": []
        }

    # sort zones based on risk score (highest first)
    # then pick top 2 most critical zones
    critical_zones = sorted(
        zone_scores,
        key=zone_scores.get,
        reverse=True
    )[:2]

    # compute average risk across all zones
    return {
        "city_risk_score": round(total / len(zone_scores), 2),
        "critical_zones": critical_zones
    }