import urllib.request
import unittest
from unittest.mock import patch

class WebRequest():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        if response.status == 200:
            return "SUCCESS"
        else:
            return "FAILURE"

# wr = WebRequest("http://www.google.com")
# wr.execute()

class WebRequestTest(unittest.TestCase):
    def test_execute_with_success(self):
        with patch('urllib.request.urlopen') as mock_url_open:
            mock_url_open.return_value.status = 200
            wr = WebRequest("http://www.google.com")
            self.assertEqual(wr.execute(), "SUCCESS")

    def test_execute_with_failure(self):
        with patch('urllib.request.urlopen') as mock_url_open:
            mock_url_open.return_value.status = 404
            wr = WebRequest("http://www.google.com")
            self.assertEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()