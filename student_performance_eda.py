import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Student Performance Data Explorer - AI/ML Internship Task 1

df = pd.read_csv("student_performance.csv")

print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Shape ---")
print(df.shape)

print("\n--- Data types ---")
print(df.dtypes)

print("\n--- Missing values ---")
print(df.isnull().sum())

print("\n--- Descriptive statistics ---")
print(df.describe())

plt.figure(figsize=(8, 5))
sns.histplot(df["final_score"], bins=8, kde=True)
plt.title("Final Score Distribution")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("final_score_distribution.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="study_hours", y="final_score", hue="gender")
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("study_hours_vs_final_score.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df[["study_hours", "previous_score", "final_score"]])
plt.title("Numeric Variables - Boxplot")
plt.tight_layout()
plt.savefig("numeric_boxplot.png")
plt.show()

numeric_df = df.select_dtypes(include=np.number)
plt.figure(figsize=(9, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

print("\n--- Findings ---")
print("Average final score:", round(df["final_score"].mean(), 2))
print("Average study hours:", round(df["study_hours"].mean(), 2))
print("Study hours/final score correlation:",
      round(df["study_hours"].corr(df["final_score"]), 2))
print("\nEDA completed successfully.")
