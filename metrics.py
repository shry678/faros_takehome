import requests 
import numpy as np
from urllib.parse import parse_qs, urlparse
from urllib.request import urlopen, Request
import json
import csv
from github import Github
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import termplotlib as tpl
import plotext as pltx
from prettytable import PrettyTable

base_url = 'https://api.github.com/'
access_token = "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"
user = 'shry678'


# verify username exists and retrieve user's repo data
def authenticate(username:str) -> json:
    try:
        repo_data = requests.get(base_url + 'users/' + username + '/repos', auth=(user,access_token))
        repo_data.raise_for_status()
    
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return repo_data.json()


# returns total number of public repositories for a user
def get_total_repos(username:str) -> int:
    url = base_url + 'users/' + username
    response = requests.get(url, auth=(user, access_token))
    return response.json()['public_repos']


# returns the most frequently used programming languages
def get_freq_used_lang(username:str, repo_data:json) -> dict:
    lang_freq = dict()
    for repo in repo_data:
        url = base_url + 'repos/' + username + '/' + repo['name'] + '/languages'
        lang_data = requests.get(url, auth=(user, access_token))
        for lang in lang_data.json():
            lang_freq[lang] = lang_freq.get(lang, 0) + 1
        
    return lang_freq


# returns most starred repositories
def get_most_starred(repo_data:json) -> dict:
    star_count = dict()
    for repo in repo_data:
        count = repo['stargazers_count']
        star_count[repo['name']] = count

    return star_count


# returns most forked repositories
def get_most_forked(repo_data:json) -> dict:
    fork_count = dict()
    for repo in repo_data:
        count = repo['forks_count']
        fork_count[repo['name']] = count
        
    return fork_count



def main(): 

if __name__ == '__main__':
    main()