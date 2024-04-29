import pandas as pd
import matplotlib.pyplot as plt
import sys

yearTested = sys.argv[1]

# Step 1: Read the CSV files
population_data = pd.read_csv('data/world_population.csv')
military_spending_data = pd.read_csv('data/military_spending.csv')

#Filtering out countries that don't exist / different names, fix this

military_spending_data[yearTested] = pd.to_numeric(military_spending_data[yearTested], errors='coerce')


military_spending_data.dropna(subset=[yearTested], inplace=True)

valid_countries = set(military_spending_data['Country'])
population_data = population_data[population_data['Country Name'].isin(valid_countries)]

valid_countries = set(population_data['Country Name'])
military_spending_data = military_spending_data[military_spending_data['Country'].isin(valid_countries)]

print(len(population_data[yearTested + ' [YR' + yearTested + ']']))
print(len(military_spending_data[yearTested]))





# Step 2: Normalize military spending

max_spending = military_spending_data[yearTested].max()
min_spending = military_spending_data[yearTested].min()
data_range = max_spending - min_spending

print("Max Military Spending:", max_spending)
print("Min Military Spending:", min_spending)


mean_spending = military_spending_data[yearTested].mean()
std_spending = military_spending_data[yearTested].std()

print("Mean Military Spending:", mean_spending)

military_spending_data.loc[:, 'z-score-' + yearTested] = ((military_spending_data[yearTested] - mean_spending) / (data_range / 2)) -1

#print(len(military_spending_data['z-score-' + yearTested]))
#military_spending_data.loc[:, 'z-score-' + yearTested] = (2 * (military_spending_data['z-score-' + yearTested] - min_spending) / (max_spending - min_spending)) - 1

# Step 3: Merge the datasets
# merged_data = pd.merge(population_data, military_spending_data, on='Country')

# Step 4: Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(military_spending_data[yearTested], population_data[yearTested + ' [YR' + yearTested + ']'])

for i, txt in enumerate(military_spending_data['Country']):
    plt.text(military_spending_data[yearTested].iloc[i], population_data[yearTested + ' [YR' + yearTested + ']'].iloc[i], txt)

plt.title('Normalized Military Spending vs Population: ' + yearTested)
plt.xlabel('Normalized Military Spending')
plt.ylabel('Population')
plt.grid(True)
plt.show()
