import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

yearTested = "2001"

# Step 1: Read the CSV files
population_data = pd.read_csv('data/world_population.csv')
military_spending_data = pd.read_csv('data/military_spending.csv')

#Filtering out countries that don't exist / different names, fix this

# military_spending_data[yearTested] = pd.to_numeric(military_spending_data[yearTested], errors='coerce')


# military_spending_data.dropna(subset=[yearTested], inplace=True)

# valid_countries = set(military_spending_data['Country'])
# population_data = population_data[population_data['Country Name'].isin(valid_countries)]

# valid_countries = set(population_data['Country Name'])
# military_spending_data = military_spending_data[military_spending_data['Country'].isin(valid_countries)]

# print(len(population_data[yearTested + ' [YR' + yearTested + ']']))
# print(len(military_spending_data[yearTested]))





# Step 2: Normalize military spending

# max_spending = military_spending_data[yearTested].max()
# min_spending = military_spending_data[yearTested].min()
# data_range = max_spending - min_spending

# print("Max Military Spending:", max_spending)
# print("Min Military Spending:", min_spending)


# mean_spending = military_spending_data[yearTested].mean()
# std_spending = military_spending_data[yearTested].std()

# print("Mean Military Spending:", mean_spending)

#military_spending_data.loc[:, 'z-score-' + yearTested] = ((military_spending_data[yearTested] - mean_spending) / (data_range / 2)) -1

#print(len(military_spending_data['z-score-' + yearTested]))
#military_spending_data.loc[:, 'z-score-' + yearTested] = (2 * (military_spending_data['z-score-' + yearTested] - min_spending) / (max_spending - min_spending)) - 1

# Step 3: Merge the datasets
# merged_data = pd.merge(population_data, military_spending_data, on='Country')



military_row_index_loc = military_spending_data.loc[military_spending_data["Country"] == "United States of America"].index[0]

pop_row_index_loc = population_data.loc[population_data["Country Name"] == "United States"].index[0]

row_country = military_spending_data.columns.tolist()[1:]

print(len(row_country))

row_military = military_spending_data.iloc[military_row_index_loc].values[1:]

print(len(row_military))
row_pop = population_data.iloc[pop_row_index_loc].values[1:-1]

row_pop = row_pop.astype(np.float64)

data = {'Year': row_country, 'Military': row_military, 'Population': row_pop}
data_frame = pd.DataFrame(data)

data_frame['Military'] = pd.to_numeric(data_frame['Military'], errors='coerce')
data_frame['Population'] = pd.to_numeric(data_frame['Population'], errors='coerce')

data_frame.dropna(inplace=True)

data_min = data_frame['Military'].min()
data_max = data_frame['Military'].max()
data_frame.loc[:, 'z-score'] = ((data_frame['Military'] - data_min) / (data_max -  data_min ) ) * 2 - 1

print(data_frame)


# print(row_military.dtype)
# print(row_pop.dtype)


# Step 4: Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(data_frame['z-score'], data_frame['Population'])

plt.xticks(data_frame['z-score'][::4])  # Adjust the step size as needed
plt.yticks(data_frame['Population'][::4])  # Adjust the step size as needed
for i, txt in enumerate(data_frame['Year']):
    plt.text(data_frame['z-score'].iloc[i], data_frame['Population'].iloc[i], txt)

plt.title('Military Spending vs Population: USA')
plt.xlabel('Normalized Military Spending')
plt.ylabel('Population')
plt.grid(True)
plt.show()
