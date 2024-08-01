import unittest
import os

class TestData(unittest.TestCase):
    def test_data_directories_exist(self):
        self.assertTrue(os.path.exists('data/raw'))
        self.assertTrue(os.path.exists('data/processed'))
        self.assertTrue(os.path.exists('data/scripts'))

if __name__ == '__main__':
    unittest.main()