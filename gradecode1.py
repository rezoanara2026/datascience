while True:
    try:
        x = int(input("Enter a num= "))
    except ValueError:
            print("Please enter an integer")
            continue
    
    if 97 <= x <= 100:
            print("A+")
    elif 93 <= x <= 96:
            print("A")
    elif 90 <= x <= 92:
            print("A-")
    elif 87 <= x <= 89:
            print("B+")
    elif 83 <= x <= 86:
            print("B")
    elif 80 <= x <= 82:
            print("B-")
    elif 77 <= x <= 79:
            print("C+")
    elif 73 <= x <= 76:
            print("C")
    elif 70 <= x <= 72:
            print("C-")
    else:
            print("F")
    break

    