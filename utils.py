from prettytable import PrettyTable
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


def create_line_graph(dict:dict, name:str):
    labels, values = zip(*dict.items())
    fig, ax = plt.subplots()
    plt.plot(values)
    fig.autofmt_xdate()
    plt.xticks(fontsize = 'xx-small')
    plt.ylabel("Number of commits")
    plt.xlabel("Week")
    plt.savefig(name, bbox_inches='tight')


def create_bar_graph(dict:dict, name:str):
    labels, values = zip(*dict.items())
    fig, ax = plt.subplots()
    plt.bar(labels, values)
    fig.autofmt_xdate()
    plt.xticks(fontsize = 'xx-small')
    plt.ylabel(name)
    plt.savefig(name, bbox_inches='tight')


def create_pie_graph(dict:dict, name:str):
    labels = list(dict.keys())
    values = list(dict.values())
    plt.pie(values, labels=labels)
    plt.savefig(name, bbox_inches='tight')
