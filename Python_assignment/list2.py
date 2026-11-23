readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]
list = []
alerts = []

for i in readings:
    if i is None:
        continue
    if 0 > i <30:
        continue
    list.append(i)
    if i > 30:
        alerts.append(i)

avg = sum(list) / len(list)
print(f"Clean readings: {list}")
print(f"Average: {avg} " )
print(f"Alerts: {alerts}")






