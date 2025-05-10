import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('Jobs', 'Steve')
        self.assertEqual(formatted_name, 'Steve Jobs','字符串对不上！！')

if __name__ == '__main__':
    unittest.main()