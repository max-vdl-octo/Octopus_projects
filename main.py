import numpy as np
import pandas as pd
import os

os.chdir(r'C:\Users\Max\Documents\Projects\Feasibility Automation\Generation capacity calculation')
df_postcode_lookup = pd.read_csv('Area Lookup.csv')

#print(df_postcode_lookup.head())

postcode = "SW34 3ls"
slope = 2
tilt = 5
kwp = 100

"""losses = 10%
area =........**********************************"""




def find_area_code(postcode, df_postcode_lookup):

    postcode = postcode.replace(" ","").upper()
    len_postcode = len(postcode)

    if len_postcode>7 or len_postcode == 5:
        print("postcode entered incorrectly")
    elif len_postcode == 7 or len_postcode == 6:
        postcode = postcode[0:-3]
    else:
        pass

    print("District code is ", postcode)

    lengths = [1, 2, None]

    for length in lengths:
        try:
            abv = postcode[:length]
            #print(abv)
            area_code = df_postcode_lookup.loc[df_postcode_lookup['Postcode'].str.match(abv)].iloc[0]['Areacode']
            print("For ", abv, "Area code is , ",area_code)
        except IndexError:
            pass
            #print("Postcode not found.")

    return area_code

def find_irradiance(area_code, slope, tilt):
    df_irradiance = pd.read_excel('Irradiance.xlsx', sheet_name=area_code)
    df_irradiance = df_irradiance.reset_index(drop=True)

    slope_index = int(slope) - 1
    tilt_index = int(np.divide(int(tilt), 5))

    irradiance = df_irradiance.iloc[slope_index,tilt_index]


    return irradiance

def find_generation(kwp, irradiance):
    generation = kwp * irradiance
    return generation

try:
    area_code = find_area_code(postcode, df_postcode_lookup)
    irradiance = find_irradiance(area_code, slope, tilt)
    generation = find_generation(kwp, irradiance)
except UnboundLocalError or NameError:
    print("Postcode not found")





print(generation)
#print(area_code)

