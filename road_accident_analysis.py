
# -------------------------------------------------------------
# Road Accident Analysis - Python Script
# Author: Vatsal Porwal
# -------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. Load Dataset
# -------------------------------------------------------------
file_path = "road_accident.csv"  # update the path if needed
df = pd.read_csv(file_path)

print("✅ Dataset Loaded Successfully!")
print(f"Total Records: {len(df)}\n")

# -------------------------------------------------------------
# 2. Data Overview and Cleaning
# -------------------------------------------------------------
print("Columns in dataset:\n", df.columns.tolist(), "\n")
df.info()

df.columns = df.columns.str.strip().str.replace(" ", "_")
df.drop_duplicates(inplace=True)
df.dropna(how="all", inplace=True)

# -------------------------------------------------------------
# 3. Key Metrics
# -------------------------------------------------------------
total_accidents = len(df)
total_casualties = df["Casualties"].sum()
fatal_casualties = df[df["Severity"] == "Fatal"]["Casualties"].sum()
serious_casualties = df[df["Severity"] == "Serious"]["Casualties"].sum()
slight_casualties = df[df["Severity"] == "Slight"]["Casualties"].sum()

print("===== Key Performance Indicators (KPIs) =====")
print(f"Total Accidents: {total_accidents}")
print(f"Total Casualties: {total_casualties}")
print(f"Fatal Casualties: {fatal_casualties}")
print(f"Serious Casualties: {serious_casualties}")
print(f"Slight Casualties: {slight_casualties}\n")

# -------------------------------------------------------------
# 4. Analysis by Different Categories
# -------------------------------------------------------------
casualties_by_vehicle = df.groupby("Vehicle_Type")["Casualties"].sum().sort_values(ascending=False)
print("Casualties by Vehicle Type:\n", casualties_by_vehicle, "\n")

casualties_by_area = df.groupby("Urban_or_Rural_Area")["Casualties"].sum()
print("Casualties by Area:\n", casualties_by_area, "\n")

casualties_by_light = df.groupby("Light_Conditions")["Casualties"].sum()
print("Casualties by Light Conditions:\n", casualties_by_light, "\n")

casualties_by_road = df.groupby("Road_Type")["Casualties"].sum().sort_values(ascending=False)
print("Casualties by Road Type:\n", casualties_by_road, "\n")

casualties_by_day = df.groupby("Day_of_Week")["Casualties"].sum()
print("Casualties by Day of Week:\n", casualties_by_day, "\n")

# -------------------------------------------------------------
# 5. Visualization
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
casualties_by_vehicle.plot(kind='bar', color='skyblue')
plt.title("Casualties by Vehicle Type")
plt.ylabel("Total Casualties")
plt.xlabel("Vehicle Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
casualties_by_area.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Urban vs Rural Casualties")
plt.ylabel("")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
casualties_by_light.plot(kind='bar', color='orange')
plt.title("Casualties by Light Conditions")
plt.ylabel("Total Casualties")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
casualties_by_day.plot(kind='bar', color='green')
plt.title("Casualties by Day of the Week")
plt.ylabel("Total Casualties")
plt.tight_layout()
plt.show()

# -------------------------------------------------------------
# 6. Yearly Comparison (if Accident_Year column exists)
# -------------------------------------------------------------
if "Accident_Year" in df.columns:
    yearly_stats = df.groupby("Accident_Year")["Casualties"].sum()
    print("Casualties by Year:\n", yearly_stats, "\n")

    plt.figure(figsize=(8, 6))
    yearly_stats.plot(kind='line', marker='o', color='purple')
    plt.title("Yearly Casualties Trend")
    plt.ylabel("Total Casualties")
    plt.xlabel("Accident Year")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------
# 7. Summary Export
# -------------------------------------------------------------
summary = {
    "Metric": ["Total Accidents", "Total Casualties", "Fatal", "Serious", "Slight"],
    "Value": [total_accidents, total_casualties, fatal_casualties, serious_casualties, slight_casualties]
}
summary_df = pd.DataFrame(summary)
summary_df.to_csv("road_accident_summary.csv", index=False)
print("✅ Summary exported to 'road_accident_summary.csv'")
