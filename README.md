# 🚦 UCCIS (Urban City Control Intelligence System)

## 📌 Overview

UCCIS is a smart city monitoring system that processes zone-based traffic data and generates alerts using rule-based intelligence.

---

## 🧠 Architecture

Input → Event → Intelligence → Rules → Alerts → API → Dashboard

---

## 🗺️ Zones (Fixed)

* thane_zone_1
* thane_zone_2
* mumbai_zone_1
* mumbai_zone_2
* navi_mumbai_zone_1
* navi_mumbai_zone_2

---

## 📦 Output Schema

```json
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

## ⚙️ API Endpoints

* `/zone/traffic?zone_id=...`
* `/zone/state`
* `/alerts`

---

## 🚀 Run

```bash
uvicorn api:app --reload
streamlit run dashboard.py
```

---

## ✅ Features

* Deterministic output
* Fixed schema
* Rule-based alerts
* Real-time API + dashboard

---

## ⚠️ Limitations

* In-memory storage
* Basic rules
* Vision not used in decisions

---

## 🎯 Conclusion

UCCIS demonstrates a complete structured pipeline for traffic intelligence with API and dashboard integration.


