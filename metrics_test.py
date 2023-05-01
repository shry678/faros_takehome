import metrics
import requests
import unittest


base_url = metrics.base_url
access_token = metrics.access_token
user = metrics.user
# tc = unittest.TestCase()


class MetricsTest(unittest.TestCase):
    def test_authenticate(self):
        response = metrics.authenticate(user)
        self.assertTrue(response.ok)

    
    def test_get_total_repos():
    

    # def test_get_freq_used_lang():



    # def test_get_most_starred():


    # def test_get_most_forked():


    # def test_get_commit_freq():


if __name__ == '__main__':
    unittest.main()








# assert response.status_code == 200

# python3 -m unittest metrics_test.py



