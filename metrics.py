import requests 
import json
import argparse
from colored import fg
import utils


access_token = 'ENTER_ACCESS_TOKEN'
user = 'ENTER_YOUR_USERNAME'
base_url = 'https://api.github.com/'


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


# returns dict with frequency of each language
def get_lang_freq(username:str, repo_data:json) -> dict:
    lang_freq = dict()

    # for each repo, view the languages used 
    for repo in repo_data:
        url = base_url + 'repos/' + username + '/' + repo['name'] + '/languages'
        lang_data = requests.get(url, auth=(user, access_token))
        # update frequency of language
        for lang in lang_data.json():
            lang_freq[lang] = lang_freq.get(lang, 0) + 1
        
    return lang_freq


# returns dict with number of stars for each repo
def get_star_count(repo_data:json) -> dict:
    star_count = dict()
    for repo in repo_data:
        count = repo['stargazers_count']
        star_count[repo['name']] = count

    return star_count


# returns number of forks for each repo
def get_fork_count(repo_data:json) -> dict:
    fork_count = dict()
    for repo in repo_data:
        count = repo['forks_count']
        fork_count[repo['name']] = count
        
    return fork_count


# returns dict with weekly frequency of commits over one year period
def get_commit_freq(username:str, repo_data:json) -> dict:
    weekly_commit = dict()

    # for each repo, view weekly commit stats 
    for repo in repo_data:
        url = base_url + 'repos/' + username + '/' + repo['name'] + '/stats/participation'
        commit_data = requests.get(url, auth=(username, access_token))
        count = 1
        # sum commit number for each week across all repos
        for stat in commit_data.json()['owner']:
            curr_week = 'W' + str(count)
            weekly_commit[curr_week] = weekly_commit.get(curr_week, 0) + stat
            count += 1

    return weekly_commit


def main(): 
    gr = "\033[1;32m "
    mg = fg('magenta')
    wh = fg('white')
    
    # Create the parser and add arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='username', type=str, help="Enter GitHub username")
    parser.add_argument('--save', default=False, action='store_true', help = "optional flag to save retrieved data")
    parser.add_argument('--gr', default=False, action='store_true', help = "optional flag to generate and save graph images")

    # Parse the results
    args = parser.parse_args()
    username = args.username
    save = args.save
    graph = args.gr

    data = authenticate(username)

    # output results
    print(mg + "Total number of public repositories: " + gr +  str(get_total_repos(username)) + '\n\n')

    lang_freq = get_lang_freq(username, data)
    print(mg + "Most frequently used programming language(s): " + gr + utils.get_keys(lang_freq))
    print(wh + str(utils.create_sorted_table(lang_freq, 'Language', 'Frequency')) + '\n \n')

    fork_count = get_fork_count(data)
    print(mg  + "Most forked repositories: " + gr + utils.get_keys(fork_count))
    print(wh + str(utils.create_sorted_table(fork_count, 'Repository', 'Fork Count')) + '\n \n')

    star_count = get_star_count(data)
    print(mg + "Most starred repositories: " + gr + utils.get_keys(star_count))
    print(wh + str(utils.create_sorted_table(star_count, 'Repository', 'Star Count')) + '\n \n')

    weekly_commit = get_commit_freq(username, data)
    print(mg + 'Weekly Commits \n' + wh + str(utils.create_table(weekly_commit, 'Week', 'Commit Count')))
    
    # save and format retrieved dicts in JSON file
    if(save):
        all_dicts = {'lang_freq': lang_freq, 'fork_count': fork_count, 
                     'star_count': star_count, 'weekly_freq':weekly_commit}
        
        with open("retrieved_data.json", "w") as outfile: 
            json.dump(all_dicts, outfile, indent=4)

    # create graphs
    if(graph):
        utils.create_pie_graph(lang_freq, 'lang')
        utils.create_bar_graph(fork_count, 'forks')
        utils.create_bar_graph(star_count, 'stars')
        utils.create_line_graph(weekly_commit, 'weekly')


if __name__ == '__main__':
    main()
