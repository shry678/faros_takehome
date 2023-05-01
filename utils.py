from prettytable import PrettyTable
import json
import matplotlib.pyplot as plt

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


def create_sorted_table(dict:dict, col1:str, col2:str) -> PrettyTable:
    table = PrettyTable([col1, col2])
    for key in dict:
        table.add_row([key, dict[key]])

    table.sortby = col2
    table.reversesort = True
    return table


def create_table(dict:dict, col1:str, col2:str) -> PrettyTable:
    table = PrettyTable([col1, col2])
    for key in dict:
        table.add_row([key, dict[key]])

    return table

def create_bar_graph(dict:dict):
    labels, values = zip(*dict.items())
    plt.bar(labels, values)
    # plt.show()
    plt.savefig('foo.png', bbox_inches='tight')


# saves json data to csv
def save_json_data( dict:dict):
    with open("sample.json", "w") as outfile: 
        json.dump(dict, outfile, indent=4)
