def apply_rules(event):

    alerts = []

    # check for high traffic condition
    # threshold-based rule (simple and deterministic)
    if event["traffic_density"] > 70:
        alerts.append("HIGH_TRAFFIC")

    # check for high violation count
    if event["violation_count"] > 2:
        alerts.append("HIGH_VIOLATION")

    # return list of triggered alerts (can be empty)
    return alerts


def take_action(alerts):

    actions = []

    # map each alert to a corresponding action
    for a in alerts:

        # if traffic is high → adjust signal timing
        if a == "HIGH_TRAFFIC":
            actions.append("INCREASE_SIGNAL_TIME")

        # if violations are high → send enforcement team
        elif a == "HIGH_VIOLATION":
            actions.append("SEND_TRAFFIC_POLICE")

    # return list of actions to be executed
    return actions