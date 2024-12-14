import os
import pandas as pd
# from pandas import dataframe
from dataclasses import dataclass
from enum import Enum
class fodmap(Enum):
    low = 1
    high = 2
    na = 3

@dataclass
class food:
    name: str
    fodmap_type: str
    category: str
    weight: int

    def __str__(self):
        base = f"Food: {self.name}\nFODMAP: {self.fodmap_type}\nCategory: {self.category}\nWeight: {self.weight}"
        return base

def look_up_by_food_name(food_name, dict):
    # food = foods_dict.get(food_name, 'na')
    results = []
    # if food != 'na':
    for key in dict.keys():
        if food_name in key:
            results.append(dict[key])
    return results

def read_food_catalog(dir_name):
    print(f"{dir_name=}")
    foods = {}
    data_df = pd.read_csv(dir_name)
    data_df = data_df.ffill()

    foods_dict = {}

    for index, row in data_df.iterrows():
        if row['high'] != 'na':
            food_h = food(name=row['high'],
                fodmap_type='high',
                category=row['category'],
                weight=row['weight_h'])
            foods_dict[row['high'].lower()] = food_h

        if row['low'] != 'na':  
            food_l = food(name=row['low'],
                fodmap_type='low',
                category=row['category'],
                weight=row['weight_l'])
            foods_dict[row['low'].lower()] = food_l
    print(f"{len(foods_dict)} foods read")
    return foods_dict

if __name__ == "__main__":
    pass
    # foods_dict = read_food_catalog("food_catalog.csv")
    # print(len(foods_dict))
    # # print(foods_dict)
    # # print(foods_dict.get('грис', 'Not found'))
    # found = look_up_by_food_name('банан', foods_dict)
    # for f in found:
    #     print(f)
    #     print('---')
