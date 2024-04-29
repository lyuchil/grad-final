import pandas as pd
import matplotlib.pyplot as plt
import sys

countryTested = sys.argv[1]

# Step 1: Read the CSV files
population_data = pd.read_csv('data/world_population_clean.csv')
military_spending_data = pd.read_csv('data/military_spending_clean.csv')


pop_row_index_loc = population_data.loc[population_data["Country"] == countryTested].index[0]
military_row_index_loc = military_spending_data.loc[military_spending_data["Country"] == countryTested].index[0]


countryData = {'Year': military_spending_data.columns.tolist()[1:],
               'Military': military_spending_data.iloc[military_row_index_loc, 1:],
               'Population': population_data.iloc[pop_row_index_loc, 1:],
               }


dataFrameCountry = pd.DataFrame(countryData)

print(dataFrameCountry)

dataFrameCountry.to_csv( 'graphOutputs/' + countryTested + '-output.csv', index=False)