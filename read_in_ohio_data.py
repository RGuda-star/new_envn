import matplotlib.pyplot as plt
import pandas as pd

data_1 = pd.read_csv('nwaa_data_1_of_3.csv')
data_2 = pd.read_csv('nwaa_data_2_of_3.csv')
data_3 = pd.read_csv('nwaa_data_3_of_3.csv')

df = pd.concat([data_1, data_2, data_3], ignore_index = True)
print(df.head())