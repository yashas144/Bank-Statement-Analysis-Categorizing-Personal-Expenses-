import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("categorized_spending (version 1).csv") 
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")  

# Filter date range
start = "2024-08-01"
end = "2025-03-31"
df = df[(df["Date"] >= start) & (df["Date"] <= end)]

# Set seaborn style
sns.set_theme(style="whitegrid")

# ===============================
# 1. Bar Chart: Total by Category
# ===============================
category_totals = df.groupby("Category")["Amount"].sum().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=category_totals.values, y=category_totals.index, palette="pastel")
plt.title("Total Spending by Category (Aug 2024 – Mar 2025)")
plt.xlabel("Total Amount ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.show()

# =======================================
# 2. Line Chart: Monthly Trend per Category
# =======================================
df["Month"] = df["Date"].dt.to_period("M")
monthly = df.groupby(["Month", "Category"])["Amount"].sum().reset_index()
monthly["Month"] = monthly["Month"].dt.to_timestamp()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly, x="Month", y="Amount", hue="Category", marker="o")
plt.title("Monthly Spending Trend by Category")
plt.xlabel("Month")
plt.ylabel("Amount Spent ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ===============================
# 3. Pie Chart: Category Breakdown
# ===============================
plt.figure(figsize=(7, 7))
df.groupby("Category")["Amount"].sum().abs().plot.pie(autopct='%1.1f%%', startangle=140)
plt.title("Spending Distribution by Category")
plt.ylabel("")
plt.tight_layout()
plt.show()