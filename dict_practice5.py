delivery_1 = {"pen": 12, "book": 5, "bag": 2}
delivery_2 = {"book": 4, "ruler": 10, "pen": 3}
total = 0
for key, value in delivery_2.items():
        if key in delivery_1:
                delivery_1[key] +=value 
        if key not in delivery_1:
                delivery_1[key]= value
for key, value in delivery_1.items():
        total += value

print("Updated dictionary:", delivery_1)
print("Grand total:", total)