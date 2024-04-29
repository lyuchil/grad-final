import pandas as pd 
import matplotlib.pyplot as plt

military_spending = pd.read_excel('C:\CS 573\Assignments\Surprise_Map_Scrollytelling_World_Data\Data\SIPRI-Milex-data-1949-2022.xlsx', sheet_name='Current US$')

world_population = pd.read_csv('C:/CS 573/Assignments/Surprise_Map_Scrollytelling_World_Data/Data/af1ae66d-b120-47f4-bbcf-c65c1d4e0912_Data.csv')


# cleaning and making it to be year 1960 or later
# alphabtically sorted as well
military_spending = military_spending.iloc[:, [0] + list(range(13, len(military_spending.columns)))]

military_spending.columns = military_spending.iloc[0]

military_spending = military_spending.drop(0)

military_spending = military_spending.sort_values(by='Country')


# population cleaning
# only keeping the countries
world_population = world_population.drop(columns=['Series Name', 'Series Code', 'Country Code'])

world_population = world_population.iloc[:217]


military_spending.to_csv('./Data/military_spending.csv', index=False)
world_population.to_csv('./Data/world_population.csv', index=False)






