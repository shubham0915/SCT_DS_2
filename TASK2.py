import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

df = pd.read_csv("train.csv")



df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df.drop(columns=["Cabin"], inplace=True)

# Summary statistics
print("Summary Statistics:")
print(tabulate(df.describe(), headers="keys", tablefmt="psql"))

# Survival rates by Pclass and Sex
survival_by_class_sex = df.groupby(["Pclass", "Sex"])["Survived"].mean() * 100
print("\nSurvival Rates by Class and Sex (%):")
print(tabulate(survival_by_class_sex.reset_index(), headers=["Pclass", "Sex", "Survival Rate"], tablefmt="psql"))

# Survival rates by Age group
bins = [0, 16, 30, 45, 60, 100]
labels = ["<16", "16-30", "31-45", "46-60", ">60"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)
survival_by_age = df.groupby("AgeGroup")["Survived"].mean() * 100
print("\nSurvival Rates by Age Group (%):")
print(tabulate(survival_by_age.reset_index(), headers=["Age Group", "Survival Rate"], tablefmt="psql"))

# Plot 1: Survival Rate by Pclass and Sex
plt.figure(figsize=(10, 6))
sns.barplot(x="Pclass", y="Survived", hue="Sex", data=df, palette="Set2")
plt.title("Survival Rate by Passenger Class and Sex")
plt.ylabel("Survival Rate")
plt.xlabel("Passenger Class")
plt.show()

# Plot 2: Age Distribution by Survival
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", hue="Survived", kde=True, palette=["#FF4C4C", "#4A90E2"])
plt.title("Age Distribution by Survival Status")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()