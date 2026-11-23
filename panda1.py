import pandas as pd

data = {
    "Name": ["Ayesha", "Sara", "Nadia", "Fatima"],
    "Marks": [85, 90, 78, 92],
    "Grade": ["A", "A+", "B", "A"],
    "Passed": [True, True, True, True]
}

df = pd.DataFrame(data)

print(df)
