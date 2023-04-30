import requests 
import json
import csv
import argparse
import matplotlib.pyplot as plt
import termplotlib as tpl
import plotext as pltx
from urllib.parse import parse_qs, urlparse
from urllib.request import urlopen, Request
from colored import fg
from utils import get_keys
from utils import create_table
from utils import create_other_table

base_url = 'https://api.github.com/'
access_token = "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"
user = 'shry678'


# verify username exists and retrieve user's repository data
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

    # look at each repo to count frequency of each language 
    for repo in repo_data:
        url = base_url + 'repos/' + username + '/' + repo['name'] + '/languages'
        lang_data = requests.get(url, auth=(user, access_token))
        for lang in lang_data.json():
            lang_freq[lang] = lang_freq.get(lang, 0) + 1
        
    return lang_freq


# returns dict to track 
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


# returns weekly frequency of commits over one year period
def get_commit_freq(username:str, repo_data:json) -> dict:
    weekly_commit = dict()

    # for each repo, parse 
    for repo in repo_data:
        url = base_url + 'repos/' + username + '/' + repo['name'] + '/stats/participation'
        commit_data = requests.get(url, auth=(username, access_token))
        count = 1
        for stat in commit_data.json()['owner']:
            curr_week = 'W' + str(count)
            weekly_commit[curr_week] = weekly_commit.get(curr_week, 0) + stat
            count += 1

    return weekly_commit


def main(): 
    # Create the parser and add arguments
    green = "\033[1;32m "
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='username', type=str, help="Enter GitHub username")

    # Parse and print the results
    args = parser.parse_args()
    username = args.username
    data = authenticate(username)

    print(fg('magenta') + "Total number of public repositories: " + green +  str(get_total_repos(username)) + '\n\n')

    lang_freq = get_freq_used_lang(username, data)
    print(fg('magenta') + "Most frequently used programming language(s): " + green + get_keys(lang_freq))
    print(fg('white') + str(create_table(lang_freq, 'Language', 'Frequency')) + '\n \n')

    fork_count = get_most_forked(data)
    print(fg('magenta')  + "Most forked repositories: " + green + get_keys(fork_count))
    print(fg('white') + str(create_table(fork_count, 'Repository', 'Fork Count')) + '\n \n')

    star_count = get_most_starred(data)
    print(fg('magenta') + "Most starred repositories: " + green + get_keys(star_count))
    print(fg('white') + str(create_table(star_count, 'Repository', 'Star Count')) + '\n \n')

    weekly_commit = get_commit_freq(username, data)
    print(fg('magenta') + 'Weekly Commits \n' + 
        fg('white') + str(create_other_table(weekly_commit, 'Week', 'Commit Count')))


if __name__ == '__main__':
    main()