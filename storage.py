from collections import defaultdict, deque

# Store recent events for each zone (max 50 events per zone)
city_data = defaultdict(lambda: deque(maxlen=50))

# Store all generated alerts
alerts_store = []

# Store computed metrics for each zone over time
metrics_store = defaultdict(list)   