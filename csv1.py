
import pandas as pd

df = pd.read_csv(r"G:\datascience\Book1.csv")

print("Student Data:")
print(df)

print("Bangla Total:", df["Bangla"].sum())
print("Bangla Average:", df["Bangla"].mean())
print("Bangla Standard Deviation:", df["Bangla"].std())

print("English Total:", df["English"].sum())
print("English Average:", df["English"].mean())
print("English Standard Deviation:", df["English"].std())
