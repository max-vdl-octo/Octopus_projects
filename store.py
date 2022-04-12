try:
    it2 = postcode[0:2]
    area_code = df_postcode_lookup.loc[df_postcode_lookup['Postcode'].str.contains(it2, case=False)].iloc[0]['Areacode']
    print("Area code is , ", area_code)
except IndexError:
    print("Not 2")

try:
    it3 = postcode[0:1]
    area_code = df_postcode_lookup.loc[df_postcode_lookup['Postcode'].str.contains(it3, case=False)].iloc[0]['Areacode']
    print("Area code is , ", area_code)
except IndexError:
    print("Postcode not found.")