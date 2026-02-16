import matplotlib.pyplot as plt
import pandas as pd

data_1 = pd.read_csv('nwaa_data_1_of_4.csv')
data_2 = pd.read_csv('nwaa_data_2_of_4.csv')
data_3 = pd.read_csv('nwaa_data_3_of_4.csv')
data_4 = pd.read_csv('nwaa_data_4_of_4.csv')

df = pd.concat([data_1, data_2, data_3, data_4], ignore_index = True)
print(df.head())