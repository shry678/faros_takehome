import metrics
import requests
import unittest
import test
import json


base_url = metrics.base_url
access_token = metrics.access_token
user = metrics.user


class MetricsTest(unittest.TestCase):
    def test_authenticate(self):
        with open('test_data.json') as user_file:
            data = user_file.read()
        
        mock_json = json.loads(data)
        response = metrics.authenticate(user)
        assert response[0]['owner']['login'] == mock_json[0]['owner']['login']

    
    def test_get_total_repos(self):
        with open('test_data.json') as user_file:
            data = user_file.read()
        
        mock_json = json.loads(data)

        assert metrics.get_total_repos(user) == len(mock_json)


    def test_get_freq_used_lang(self):
        with open('test_data.json') as user_file:
            data = user_file.read()
        
        mock_json = json.loads(data)
        response = metrics.authenticate(user)
        mock_lang = metrics.get_freq_used_lang(user, mock_json)
        lang = metrics.get_freq_used_lang(user, response)

        assert mock_lang == lang


    def test_get_most_starred(self):
        with open('test_data.json') as user_file:
            data = user_file.read()
        
        mock_json = json.loads(data)
        response = metrics.authenticate(user)
        star_dict = metrics.get_most_forked(response)

        assert  next(iter(star_dict.values())) == mock_json[0]['stargazers_count']


    def test_get_most_forked(self):
        with open('test_data.json') as user_file:
            data = user_file.read()
        
        mock_json = json.loads(data)
        response = metrics.authenticate(user)
        fork_dict = metrics.get_most_forked(response)

        assert next(iter(fork_dict.values())) == mock_json[0]['forks_count']


    def test_get_commit_freq(self):
        with open('test_data.json') as user_file:
            data = user_file.read()
        
        mock_json = json.loads(data)
        mock_commit = metrics.get_commit_freq(user, mock_json)

        response = metrics.authenticate(user)
        weekly_commit = metrics.get_commit_freq(user, response)

        assert mock_commit == weekly_commit


if __name__ == '__main__':
    unittest.main()








# assert response.status_code == 200

# python3 -m unittest metrics_test.py



