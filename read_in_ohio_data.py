import matplotlib.pyplot as plt
import pandas as pd

data_1 = pd.read_csv('nwaa_data_ohio_PSC1.csv')
data_2 = pd.read_csv('nwaa_data_ohio_PSC2.csv')
data_3 = pd.read_csv('nwaa_data_ohio_PSC3.csv')

df1 = pd.concat([data_1, data_2, data_3], ignore_index = True)
#print(df1.head())

data_4 = pd.read_csv('nwaa_data_ohio_HSM1.csv')
data_5 = pd.read_csv('nwaa_data_ohio_HSM2.csv')
data_6 = pd.read_csv('nwaa_data_ohio_HSM3.csv')

df2 = pd.concat([data_4, data_5, data_6], ignore_index = True)
#print(df2.head())

df = pd.merge(df2, df1)
print(df[0:14])