makeup = {"Dior_foundation": 50, "YSL_lipstick": 40, "Huda Beauty": 25, "Fenty Beauty": 30, "NARS_blush": 35}

product = input("Enter product name: ")

if product in makeup:
    print("Price:", makeup[product])
else:
    price = int(input("Product not found. Enter price: "))
    makeup[product] = price
    print("Product added successfully.")

print(makeup)