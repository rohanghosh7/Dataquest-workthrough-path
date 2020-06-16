## 1. Reading CSV Files with Encodings ##

import pandas as pd
laptops = pd.read_csv('laptops.csv',encoding = "Latin-1")
laptops.info()

## 2. Cleaning Column Names ##

new_columns = []
for col in laptops.columns:
    clean_c = col.strip()
    new_columns.append(clean_c)
    
laptops.columns = new_columns

## 3. Cleaning Column Names Continued ##

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def change(s):
    s = s.strip()
    s = s.replace("Operating System","os")
    s = s.replace(" ","_")
    s = s.replace("(","")
    s = s.replace(")","")
    s = s.lower()
    return s
new_columns = []
for col in laptops.columns:
    clean_c = change(col)
    new_columns.append(clean_c)
    
laptops.columns = new_columns

## 4. Converting String Columns to Numeric ##

unique_ram = laptops.loc[:,"ram"].unique()

## 5. Removing Non-Digit Characters ##

laptops["ram"] = laptops["ram"].str.replace("GB","")
unique_ram = laptops["ram"].unique()


## 6. Converting Columns to Numeric Dtypes ##

laptops["ram"] = laptops["ram"].str.replace('GB','')
laptops["ram"] = laptops["ram"].astype(int)
dtypes = laptops.dtypes

## 7. Renaming Columns ##

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)
laptops.rename({"ram":"ram_gb"},axis = 1 , inplace = True)
ram_gb_desc = laptops["ram_gb"].describe()

## 8. Extracting Values from Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )
laptops["cpu_manufacturer"] = (laptops["cpu"]
                                       .str.split()
                                       .str[0]
                               )
cpu_manufacturer_counts = laptops["cpu_manufacturer"].value_counts()

## 9. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops["os"] = laptops["os"].map(mapping_dict)

## 10. Dropping Missing Values ##

laptops_no_null_rows = laptops.dropna()
laptops_no_null_cols = laptops.dropna(axis = 1)

## 11. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"
laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"
value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()

## 12. Challenge: Clean a String Column ##

laptops["weight"] = laptops["weight"].str.replace('kgs','')
laptops["weight"] = laptops["weight"].str.replace('kg','')
laptops["weight"] = laptops["weight"].astype(float)
laptops.rename({"weight":"weight_kg"},axis = 1,inplace = True)
laptops.to_csv('laptops_cleaned.csv',index = False)