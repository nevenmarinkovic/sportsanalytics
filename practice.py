import pandas as pd

df = pd.read_csv("students.csv")

print("View the name column")
print(df['Name'])

print("row at index 1")
print(df.loc[1])

print("get rows where the age > 13")
print(df[df["Age"] > 13])

#Adding a new column
df["Pass/Fail"] = ["Pass", "Pass", "Pass", "Fail"]
print(df)

#Group Data by a column and compute the average age
grouped = df.groupby("Grade")["Age"].mean()
print(grouped)