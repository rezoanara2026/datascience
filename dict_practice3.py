stock = {"pen": 12, "book": 3, "bag": 2, "ruler": 9, "calculator": 1}
low_stock= {}
sum= 0
for key, value in stock.items():
    sum += value
    if value < 5:
        low_stock[key] = value
 
print(f"Total unit price: {sum}")
print(low_stock)
