# Physics Data Challenge Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Dataset
df = pd.read_csv('cart_flat.csv')

# 2. Data Cleaning

# 2.1 - Check for missing values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# 2.2 - Handle missing values using mean
missing_cols = ['Force (N)', 'Acceleration (m/s²)', 'Velocity (m/s)', 'Acceleration - resultant (m/s²)']
for col in missing_cols:
    df[col] = df[col].fillna(df[col].mean())

# 2.3 - Drop remaining NaNs
clean_df = df.dropna()
print("\n✅ Cleaned Data Preview:")
print(clean_df.describe())
print(clean_df.isnull().sum())

# 3. Visualizations

# 3.1 - Acceleration vs Force
plt.figure(figsize=(6, 4))
plt.scatter(clean_df['Acceleration (m/s²)'], clean_df['Force (N)'], alpha=0.6, color='blue')
plt.title('Acceleration vs Force')
plt.xlabel('Acceleration (m/s²)')
plt.ylabel('Force (N)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 3.2 - Acceleration vs Time
plt.figure(figsize=(6, 4))
sns.lineplot(data=clean_df, x='Time (s)', y='Acceleration (m/s²)')
plt.title('Acceleration vs Time')
plt.tight_layout()
plt.show()

# 3.3 - Velocity vs Time
plt.figure(figsize=(6, 4))
sns.lineplot(data=clean_df, x='Time (s)', y='Velocity (m/s)')
plt.title('Velocity vs Time')
plt.tight_layout()
plt.show()

# 4. Kinetic Energy Analysis

# 4.1 - Calculate Kinetic Energy
clean_df['Kinetic Energy (J)'] = 0.5 * clean_df['Velocity (m/s)'] ** 2

# 4.2 - KE vs Time
plt.figure(figsize=(6, 4))
sns.lineplot(data=clean_df, x='Time (s)', y='Kinetic Energy (J)')
plt.title('Kinetic Energy vs Time')
plt.tight_layout()
plt.show()

# 4.3 - KE vs Velocity
plt.figure(figsize=(6, 4))
sns.lineplot(data=clean_df, x='Velocity (m/s)', y='Kinetic Energy (J)')
plt.title('Kinetic Energy vs Velocity')
plt.tight_layout()
plt.show()