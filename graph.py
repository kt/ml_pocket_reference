# Graph some data

import os
import pandas as pd
import matplotlib.pyplot as plt

os.system('clear')

# Step 1: Load the CSV file and check it looks OK
data = pd.read_csv("CO2 emission by countries.csv", encoding='unicode_escape')
print(f'Data has {data.shape[0]} rows, {data.shape[1]} columns')
print('first row')
print(data.head(0))

# Step 2: Filter the data for a given country
country_name = 'Germany'
country_data = data[data['Country'] == country_name]

# Step 3: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(country_data['Year'], country_data['CO2 emission (Tons)'], marker='.')
plt.title(f'CO2 Emissions in {country_name} (since 1700)')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (Tons)')
plt.grid(True)
plt.show()

# Step 4: save the plot as an image file
plt.savefig('emissions.png')
