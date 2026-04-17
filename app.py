import cv2
import time
from datetime import datetime

from config import ZONES
from storage import city_data, alerts_store
from event_schema import create_event
from vision_engine import run_vision
from rule_engine import apply_rules, take_action
from intelligence_engine import compute_zone_metrics
from signal_engine import compute_signal_plan

# predefined valid zones 
VALID_ZONES = [
    "thane_zone_1",
    "thane_zone_2",
    "mumbai_zone_1",
    "mumbai_zone_2",
    "navi_mumbai_zone_1",
    "navi_mumbai_zone_2"
]

# returns fixed traffic density per zone
# used instead of randomness so system behaves predictably (testing/debugging easy)
def deterministic_density(zone_id):
    base_map = {
        "thane_zone_1": 40,
        "thane_zone_2": 55,
        "mumbai_zone_1": 78,
        "mumbai_zone_2": 65,
        "navi_mumbai_zone_1": 30,
        "navi_mumbai_zone_2": 50
    }
    return base_map.get(zone_id, 20)  # default fallback


# returns fixed violation count per zone
def deterministic_violations(zone_id):
    violation_map = {
        "thane_zone_1": 1,
        "thane_zone_2": 2,
        "mumbai_zone_1": 3,
        "mumbai_zone_2": 2,
        "navi_mumbai_zone_1": 0,
        "navi_mumbai_zone_2": 1
    }
    return violation_map.get(zone_id, 0)


def run_engine():

    print("🚀 UCCIS Engine Started...")

    # load traffic video (acts as input stream)
    cap = cv2.VideoCapture("traffic.mp4")

    # check if video loaded properly
    if not cap.isOpened():
        print("❌ Error: traffic.mp4 not found")
        return

    zone_list = VALID_ZONES

    # main continuous loop (simulates real-time system)
    while True:

        ret, frame = cap.read()

        # if video ends, restart from beginning (looping stream)
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # run vision processing (output ignored here since system is deterministic)
        _ = run_vision(frame)

        zone_snapshot = {}  # used later for signal planning

        # process each zone independently
        for zone_id in zone_list:

            # get fixed values (no randomness)
            traffic_density = deterministic_density(zone_id)
            violation_count = deterministic_violations(zone_id)

            timestamp = datetime.utcnow().isoformat()
            trace_id = f"{zone_id}_trace_fixed"  # helps in tracking/debugging

            # event object representing current state of zone
            event = {
                "zone_id": zone_id,
                "traffic_density": traffic_density,
                "violation_count": violation_count,
                "timestamp": timestamp,
                "trace_id": trace_id
            }

            # compute additional intelligence metrics (like trends, severity etc.)
            event["metrics"] = compute_zone_metrics(zone_id, event)

            # apply business rules on event (detect alerts)
            alerts = apply_rules(event)

            # decide actions based on alerts (like signal change, warning etc.)
            actions = take_action(alerts)

            # store alerts separately for API access
            alerts_store.append({
                "zone_id": zone_id,
                "alerts": alerts,
                "actions": actions,
                "timestamp": timestamp,
                "trace_id": f"{zone_id}_alert_trace"
            })

            # store event in city data (historical tracking)
            city_data[zone_id].append(event)

            # minimal snapshot for signal engine
            zone_snapshot[zone_id] = {
                "traffic_density": traffic_density
            }

        # compute signal timing plan based on all zones
        signal_plan = compute_signal_plan(zone_snapshot)

        print("🚦 SIGNAL PLAN:")
        print(signal_plan)

        # show video window (for visualization/debugging)
        cv2.imshow("UCCIS ENGINE", frame)

        # press ESC to stop
        if cv2.waitKey(1) == 27:
            break

        # small delay to simulate real-time processing
        time.sleep(0.05)

    # release resources properly
    cap.release()
    cv2.destroyAllWindows()


# entry point
if __name__ == "__main__":
    run_engine()