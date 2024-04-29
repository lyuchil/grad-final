import pandas as pd
import matplotlib.pyplot as plt
import sys

yearTested = sys.argv[1]

# Step 1: Read the CSV files
population_data = pd.read_csv('data/world_population_clean.csv')
military_spending_data = pd.read_csv('data/military_spending_clean.csv')

yearData = {'Country': population_data['Country'], 'Military': military_spending_data[yearTested], 'Population': population_data[yearTested]}

dataFrameYear = pd.DataFrame(yearData)

print(dataFrameYear)

dataFrameYear.to_csv( 'graphOutputs/' + yearTested + '-output.csv', index=False)

