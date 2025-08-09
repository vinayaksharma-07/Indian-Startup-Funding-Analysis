import pandas as pd
df = pd.read_csv('/content/startup_funding.csv')
display(df.head())



df['Date dd/mm/yyyy'] = pd.to_datetime(df['Date dd/mm/yyyy'], errors='coerce')
df['Amount in USD'] = df['Amount in USD'].astype(str).str.replace(',', '', regex=False)
df['Amount in USD'] = pd.to_numeric(df['Amount in USD'], errors='coerce')
funding_trend = df.resample('M', on='Date dd/mm/yyyy')['Amount in USD'].sum()
display(funding_trend)


top_sectors = df['Industry Vertical'].value_counts().head(5)
display(top_sectors)


top_cities = df['City  Location'].value_counts().head(5)
display(top_cities)


top_startups = df['Startup Name'].value_counts().head(5)
display(top_startups)


top_startups = df['Startup Name'].value_counts().head(5)
display(top_startups)


import matplotlib.pyplot as plt
import seaborn as sns

# Visualize funding trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=funding_trend)
plt.title('Startup Funding Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Amount in USD')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize top sectors
plt.figure(figsize=(10, 6))
sns.barplot(x=top_sectors.index, y=top_sectors.values)
plt.title('Top 5 Industry Verticals by Count')
plt.xlabel('Industry Vertical')
plt.ylabel('Number of Startups')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Visualize top cities
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.index, y=top_cities.values)
plt.title('Top 5 Cities by Funding Amount')
plt.xlabel('City')
plt.ylabel('Total Funding in USD')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Visualize top startups
plt.figure(figsize=(12, 6))
sns.barplot(x=top_startups.index, y=top_startups.values)
plt.title('Top 5 Startups by Funding Amount')
plt.xlabel('Startup Name')
plt.ylabel('Total Funding in USD')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Visualize investment type distribution
plt.figure(figsize=(12, 6))
sns.barplot(x=investment_type_distribution.index, y=investment_type_distribution.values)
plt.title('Distribution of Investment Types')
plt.xlabel('Investment Type')
plt.ylabel('Count')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()


