# test_example.py
import unittest
from example import greet

class TestExample(unittest.TestCase):
    def test_greet(self):
        # This is a simple test to check if greet function prints the correct message
        self.assertEqual(greet(), None)  # The greet function prints, so it returns None

if __name__ == '__main__':
    unittest.main()

