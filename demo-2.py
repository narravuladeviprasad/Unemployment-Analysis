import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# ✅ Optional: Ensure font doesn't try to render emojis
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

# 🧩 Load and Clean Data
df = pd.read_csv('Unemployment in India.csv', encoding='utf-8', skipinitialspace=True)

# Clean column names
df.columns = [col.strip().replace(' ', '_').replace('(', '').replace(')', '') for col in df.columns]

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')

# Drop rows with invalid dates or missing data
df = df[df['Date'].notna()]
df.dropna(inplace=True)

# 📌 View basic info
print("✅ Cleaned Dataset Info:")
print(df.info())
print("\n🧾 First 5 Rows:")
print(df.head())

# 🎯 Plot: Unemployment Rate Over Time by Region
plt.figure(figsize=(14, 6))
for region in df['Region'].unique():
    regional_data = df[df['Region'] == region]
    plt.plot(regional_data['Date'], regional_data['Estimated_Unemployment_Rate_%'], label=region)

plt.title("Unemployment Rate Over Time by Region")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend(loc='upper right', fontsize='small')
plt.tight_layout()
plt.show()

# 🔥 Heatmap: Unemployment Rate by Region and Date
pivot = df.pivot_table(values='Estimated_Unemployment_Rate_%', index='Region', columns='Date')
plt.figure(figsize=(16, 10))
sns.heatmap(pivot, cmap='viridis', linewidths=0.5)
plt.title("Heatmap of Unemployment Rate (%) by Region and Date")
plt.xlabel("Date")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

# 🏙️ Boxplot: Compare Urban vs Rural Unemployment Rates
plt.figure(figsize=(8, 5))
sns.boxplot(x='Area', y='Estimated_Unemployment_Rate_%', data=df)
plt.title("Urban vs Rural Unemployment Rate Comparison")
plt.xlabel("Area")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# 🦠 Impact of COVID-19 (around March 2020 onwards)
covid_period = df[df['Date'] >= '2020-03-01']
plt.figure(figsize=(12, 6))
sns.lineplot(data=covid_period, x='Date', y='Estimated_Unemployment_Rate_%', hue='Region', legend=False)
plt.title("Impact of COVID-19 on Unemployment (Mar 2020 onwards)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ✅ DONE
print("✅ Unemployment analysis completed.")
