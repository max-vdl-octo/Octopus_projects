import numpy as np
import pandas as pd
import os


os.chdir(r'C:\Users\Max\Documents\Projects\Feasibility Automation\Consumption Data Prep')
df_cons = pd.read_excel('Type_1.xlsx')


#print(df_cons.head())

transformed = [{'Date', 'Attribute', 'Hour', 'Consumption', 'Generation', 'Export (kWh)', 'Import (kWh)'}]
df_transformed = pd.DataFrame(columns=['Date', 'Attribute', 'Hour', 'Consumption', 'Generation', 'Export (kWh)', 'Import (kWh)'])


attribute_list = []
for hour in range(24):
    for minute in range(0, 60, 15):
        times.append('{:02d}:{:02d}'.format(hour, minute))

def get_date(df_cons, n):
    date = df_cons.iloc[n,0].date()
    return date

def get_attribute(df_cons, n):

    return attribute

def get_hour(df_cons, n):

    return hour

def get_consumtion(df_cons, n):

    return consumption

def add_row(df_transformed, df_cons, m):

    date = get_date(df_cons,m)
    attribute = get_attribute(df_cons, m)

    df2 = pd.DataFrame({'Date': [date],
                        'Attribute': [attribute],
                        'Hour': [3],
                        'Consumption': [4],
                        'Generation': [5],
                        'Export (kWh)': [6],
                        'Import (kWh)': [7]})


    df_transformed = pd.concat([df_transformed,df2], ignore_index=True, axis = 0)

    return df_transformed

n = 1
print(df_cons.head(2))

df_transformed = add_row(df_transformed, df_cons)
print(df_transformed.head(2))
#date = get_date(df_cons, n)
#print(date)

#out = add_row(df_transformed, df_cons)
#print(out)