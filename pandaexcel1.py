import pandas as pd
import openpyxl
df = pd.read_excel(r"C:\Users\rezoa\Downloads\student1.xlsx")


print("Student Data:")
print(df)

print("Total:", df["Marks"].sum())
print("Average:", df["Marks"].mean())
print("Standard Deviation:", df["Marks"].std())