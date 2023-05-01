import metrics
import requests
import unittest
import test
import json


base_url = metrics.base_url
access_token = metrics.access_token
user = metrics.user
# tc = unittest.TestCase()


class MetricsTest(unittest.TestCase):
    def test_authenticate(self):
        with open('test_data.json') as user_file:
            data = user_file.read()
        
        mock_json = json.loads(data)
        response = metrics.authenticate(user)
        assert response[0]['owner']['login'] == mock_json[0]['owner']['login']

    
    # def test_get_total_repos(self):
    #     with open('test_data.json') as user_file:
    #         data = user_file.read()
        
    #     mock_json = json.loads(data)

    #     assert metrics.get_total_repos(user) == mock_json['public_repos']


    

    # def test_get_freq_used_lang(self):



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

        mock_count = next(iter(mock_commit.values()))
        count = next(iter(weekly_commit.values()))
        assert count == mock_count


if __name__ == '__main__':
    unittest.main()








# assert response.status_code == 200

# python3 -m unittest metrics_test.py



