# 🚦 UCCIS (Urban City Control Intelligence System)

## 📌 Overview

UCCIS is a structured smart city monitoring system that simulates zone-based traffic intelligence.

The system processes input data, generates structured events, applies rule-based logic, and exposes outputs via APIs and a dashboard.

---

## 🧠 System Architecture

Flow:

Input → Event → Intelligence → Rules → Alerts → API → Dashboard

---

## 🧩 Components

### 1. Vision Engine

* Uses YOLOv8
* Runs object detection on video frames
* Execution component (not used in decision logic for deterministic output)

---

### 2. Event System

All data is converted into a strict schema:

```
{
  "zone_id": "mumbai_zone_1",
  "traffic_density": 78,
  "violation_count": 3,
  "congestion_level": "HIGH",
  "timestamp": "...",
  "trace_id": "abc123"
}
```

---

### 3. Zones (STRICT)

```
thane_zone_1  
thane_zone_2  
mumbai_zone_1  
mumbai_zone_2  
navi_mumbai_zone_1  
navi_mumbai_zone_2  
```

---

### 4. Intelligence Engine

* Average traffic
* Average violations
* Trend detection
* Risk score

---

### 5. Rule Engine

Deterministic rules:

* HIGH_TRAFFIC → traffic_density > 70
* HIGH_VIOLATION → violation_count > 2

---

### 6. Alerts & Actions

| Alert          | Action               |
| -------------- | -------------------- |
| HIGH_TRAFFIC   | INCREASE_SIGNAL_TIME |
| HIGH_VIOLATION | SEND_TRAFFIC_POLICE  |

---

### 7. API Layer (FastAPI)

Endpoints:

* `/zone/traffic?zone_id=...`
* `/zone/state`
* `/alerts`

---

### 8. Dashboard (Streamlit)

* Real-time zone data
* Alerts visualization
* Auto-refresh enabled

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install fastapi uvicorn streamlit ultralytics opencv-python
```

### 2. Start Backend

```
uvicorn api:app --reload
```

### 3. Run Dashboard

```
streamlit run dashboard.py
```

---

## 📡 API Example

### `/zone/state`

```
[
  {
    "zone_id": "mumbai_zone_1",
    "traffic_density": 78,
    "violation_count": 3,
    "congestion_level": "HIGH",
    "timestamp": "2026-04-18T10:00:00",
    "trace_id": "mumbai_zone_1_trace_fixed"
  }
]
```

---

## ✅ Key Features

* Deterministic system (same input → same output)
* Strict schema enforcement
* Zone-based architecture
* Real-time API + dashboard
* Traceable outputs using trace_id

---

## ⚠️ Limitations

* No database (in-memory storage)
* Basic rule engine
* Vision output not used in decision logic
* Simple UI

---

## 🎯 Conclusion

UCCIS demonstrates a complete structured pipeline for city intelligence systems with deterministic processing, rule-based alerts, API exposure, and visualization.

---

