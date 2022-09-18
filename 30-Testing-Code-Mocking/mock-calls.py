import unittest

from unittest.mock import MagicMock

class MockCallsTest(unittest.TestCase):
    def test_mock_calls(self):
        mock = MagicMock()
        mock()
        #this is checking that the mock has been called
        mock.assert_called()

    def test_mock_not_called(self):
        mock = MagicMock()
        #mock()
        #this is checking that the mock has been not called
        mock.assert_not_called()

    def test_called_with(self):
        mock = MagicMock()
        mock(1, 2, 3)
        #this is checking that the mock has been called with certain argument
        mock.assert_called_with(1, 2, 3)

    def test_mock_attributes(self):
        mock = MagicMock()
        print(mock.called)
        mock()
        mock(1, 2, 3)
        print(mock.called)
        print(mock.call_count)
        print(mock.mock_calls)

if __name__ == "__main__":
    unittest.main()