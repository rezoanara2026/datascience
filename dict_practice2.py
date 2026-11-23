list = {"pen": 15, "book": 120, "bag": 850}
requested_items = ["book", "ruler", "pen"]
for i in requested_items:
    price = list.get(i)
    if price is not None:
        print(f"{i}: Tk {price}") 
    else:
        print(f"{i}: Not found")
        
    
    
        
