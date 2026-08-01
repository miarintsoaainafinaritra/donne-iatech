import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Creer le dossier images
os.makedirs('images', exist_ok=True)

df = pd.read_csv('clean_data.csv', parse_dates=['timestamp_utc'])

# 1. Evolution AQI
plt.figure(figsize=(12, 6))
for city in df['city_name'].unique():
    city_data = df[df['city_name'] == city]
    plt.plot(city_data['timestamp_utc'], city_data['aqi'], label=city, alpha=0.7)
plt.title('Evolution AQI par ville', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/evolution_aqi.png', dpi=150)
plt.close()
print("✅ evolution_aqi.png")

# 2. Distribution AQI
plt.figure(figsize=(10, 6))
df.boxplot(column='aqi', by='city_name')
plt.title('Distribution AQI par ville', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/distribution_aqi.png', dpi=150)
plt.close()
print("✅ distribution_aqi.png")

# 3. Correlation polluants
pollutants = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
corr = df[pollutants].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f', square=True)
plt.title('Correlation polluants', fontsize=14)
plt.tight_layout()
plt.savefig('images/correlation_polluants.png', dpi=150)
plt.close()
print("✅ correlation_polluants.png")

# 4. AQI par heure
hourly = df.groupby(df['timestamp_utc'].dt.hour)['aqi'].mean()
plt.figure(figsize=(10, 6))
plt.bar(hourly.index, hourly.values, color='steelblue')
plt.title('AQI moyen par heure', fontsize=14)
plt.xlabel('Heure')
plt.ylabel('AQI')
plt.grid(True, alpha=0.3)
plt.xticks(range(0, 24, 2))
plt.tight_layout()
plt.savefig('images/aqi_par_heure.png', dpi=150)
plt.close()
print("✅ aqi_par_heure.png")

# 5. Dashboard complet (4 graphiques en 1)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for city in df['city_name'].unique():
    city_data = df[df['city_name'] == city]
    axes[0,0].plot(city_data['timestamp_utc'], city_data['aqi'], label=city, alpha=0.7)
axes[0,0].set_title('Evolution AQI par ville')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)
axes[0,0].tick_params(axis='x', rotation=45)

df.boxplot(column='aqi', by='city_name', ax=axes[0,1])
axes[0,1].set_title('Distribution AQI par ville')
axes[0,1].set_xlabel('')
plt.xticks(rotation=45, ha='right')

pollutants = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
corr = df[pollutants].corr()
im = axes[1,0].imshow(corr, cmap='coolwarm', aspect='auto')
axes[1,0].set_title('Correlation polluants')
axes[1,0].set_xticks(range(len(pollutants)))
axes[1,0].set_yticks(range(len(pollutants)))
axes[1,0].set_xticklabels(pollutants, rotation=45, ha='right', fontsize=8)
axes[1,0].set_yticklabels(pollutants, fontsize=8)
for i in range(len(pollutants)):
    for j in range(len(pollutants)):
        axes[1,0].text(j, i, f'{corr.iloc[i,j]:.2f}', ha='center', va='center', fontsize=7)
plt.colorbar(im, ax=axes[1,0])

hourly = df.groupby(df['timestamp_utc'].dt.hour)['aqi'].mean()
axes[1,1].bar(hourly.index, hourly.values, color='steelblue')
axes[1,1].set_title('AQI moyen par heure')
axes[1,1].set_xlabel('Heure')
axes[1,1].set_ylabel('AQI')
axes[1,1].grid(True, alpha=0.3)
axes[1,1].set_xticks(range(0, 24, 2))

plt.tight_layout()
plt.savefig('images/dashboard_complet.png', dpi=150)
plt.close()
print("✅ dashboard_complet.png")

print("\n✅ Toutes les images sont dans le dossier 'images/'")
