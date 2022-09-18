import unittest
from unittest.mock import patch
from web_request import WebRequest

class WebRequestTest(unittest.TestCase):
    #always remember that that patch refrence the function you want to mock 
    #IN the module where it is located, in this case, 
    #the urlopen was imported directly into the web_request file, so it exists independently in the file
    @patch('web_request.urlopen')
    def test_execute_with_success_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "SUCCESS")

    @patch('web_request.urlopen')
    def test_execute_with_failure_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 404
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "FAILURE")


if __name__ == "__main__":
    unittest.main()