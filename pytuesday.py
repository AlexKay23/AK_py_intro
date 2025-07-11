
import pydytuesday
import pandas as pd

# Download files from the week, which you can then read in locally
pydytuesday.get_date('2025-07-01')

gas_df = pd.read_csv('weekly_gas_prices.csv')

highest_prices = gas_df.groupby('formulation')['price'].max().reset_index()

print(highest_prices)
