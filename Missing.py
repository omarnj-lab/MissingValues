# Data Preprocessing
# Importing the libraries
import pandas as pd

# Importing the dataset
df = pd.read_csv('Data.csv')
df

# Using Interpolate to replace missing values: 

new_df =  df.interpolate()
new_df

new_df.interpolate(method='polynomial', order=2)

new_df.interpolate(method='pad', limit=2)
