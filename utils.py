from prettytable import PrettyTable
import json

# find keys with specific value and return as str
def get_keys(dict:dict) ->str:
    val = max(dict.values())
    if val == 0:
        return 'None'

    res = ''
    for key in dict.keys():
        if val == dict.get(key):
            res += key + ", "
    
    return res[:-2]


def create_table(dict:dict, col1:str, col2:str) -> PrettyTable:
    table = PrettyTable([col1, col2])
    for key in dict:
        table.add_row([key, dict[key]])

    table.sortby = col2
    table.reversesort = True
    return table


def create_other_table(dict:dict, col1:str, col2:str) -> PrettyTable:
    table = PrettyTable([col1, col2])
    for key in dict:
        table.add_row([key, dict[key]])

    return table

# saves json data to csv
def save_json_data( dict:dict):
    with open("sample.json", "w") as outfile: 
        json.dump(dict, outfile, indent=4)
