import matplotlib.pyplot as plt
import pandas as pd

data_1 = pd.read_csv('nwaa_data_wisc_PSC1.csv')
data_2 = pd.read_csv('nwaa_data_wisc_PSC2.csv')
data_3 = pd.read_csv('nwaa_data_wisc_PSC3.csv')
data_4 = pd.read_csv('nwaa_data_wisc_PSC4.csv')

df1 = pd.concat([data_1, data_2, data_3, data_4], ignore_index = True)
#print(df1.head())

data_5 = pd.read_csv('nwaa_data_wisc_HSM1.csv')
data_6 = pd.read_csv('nwaa_data_wisc_HSM2.csv')
data_7 = pd.read_csv('nwaa_data_wisc_HSM3.csv')
data_8 = pd.read_csv('nwaa_data_wisc_HSM4.csv')

df2 = pd.concat([data_5, data_6, data_7, data_8], ignore_index = True)
#print(df2.head())

df = pd.merge(df2, df1)
print(df[0:20])