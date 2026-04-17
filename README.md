# Urban City Control Intelligence System

## Overview

This project is a structured implementation of a smart city monitoring system. It simulates how predefined city zones are monitored using traffic data and rule-based intelligence.

The system processes input data, generates structured events, applies rules, and exposes outputs via APIs and a dashboard.

## System Components
### 1. Vision Engine

* Uses YOLOv8 model
* Runs object detection on video frames
* (Execution component; system uses deterministic data for output consistency)

### 2. Event System

* Converts all inputs into a strict structured format
* Ensures consistency using a fixed schema:
zone_id

traffic_density  

violation_count  

congestion_level  

timestamp  

trace_id

### 3. Zone-Based System

City is strictly divided into 6 zones:

* thane_zone_1
* thane_zone_2
* mumbai_zone_1
* mumbai_zone_2
* navi_mumbai_zone_1
* navi_mumbai_zone_2

### 4. Intelligence Engine

Computes:
* Average traffic density
* Average violation count
* Traffic trend (increasing/decreasing)
* Risk score

### 5. Rule Engine

Applies deterministic rules:

* High traffic → HIGH_TRAFFIC alert
* High violations → HIGH_VIOLATION alert
  
### 6. Alerts & Actions

Alerts generated:
* HIGH_TRAFFIC
* HIGH_VIOLATION

Actions taken:
* INCREASE_SIGNAL_TIME
* SEND_TRAFFIC_POLICE
  
### 7. API Layer (FastAPI)

Endpoints:
/zone/traffic?zone_id=... → single zone data
/zone/state → all zones state
/alerts → alerts output

All responses follow strict JSON schema with trace_id and timestamp.

### API Output Proof

/zone/state response:

<img width="1359" height="716" alt="image" src="https://github.com/user-attachments/assets/8c920175-8c1d-4399-9e95-529f384228ea" />


/zone/traffic?zone_id=mumbai_zone_1 response:

<img width="1365" height="718" alt="image" src="https://github.com/user-attachments/assets/335f5d89-f9d4-441e-8706-36bb9e58b250" />

http://127.0.0.1:8000/docs

<img width="1365" height="723" alt="image" src="https://github.com/user-attachments/assets/dd573e92-e222-4fc6-980e-24d2314e8c8e" />


### 8. Dashboard (Streamlit)

Displays:

* Zone state (traffic, violations, congestion)
* Live alerts
* Auto-refresh system
  
#### Dashboard Output

<img width="1347" height="716" alt="image" src="https://github.com/user-attachments/assets/125aec27-6992-4926-b88b-6bc8fb35f1d5" />


#### Data Flow

Input → Event Creation → Intelligence → Rules → Alerts → Actions → API → Dashboard

### System Characteristics

* Deterministic output (same input → same output)
* Fixed schema enforcement
* Traceable outputs using trace_id
* Real-time API exposure
  
### System Execution Proof

<img width="1364" height="714" alt="image" src="https://github.com/user-attachments/assets/0bfbc956-b6ec-4b6b-ad77-cda449a67868" />


#### Limitations
* No database (in-memory storage)
* Basic rule engine
* Vision output not directly used in decision logic
* Simple dashboard
  
### Conclusion

This project demonstrates a complete structured pipeline of a city intelligence system with deterministic processing, rule-based decision making, API exposure, and dashboard visualization.
