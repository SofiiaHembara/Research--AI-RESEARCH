import unittest
from correct_code import caesar_encode, caesar_decode

class TestCaesar(unittest.TestCase):
    def test_encode(self):
        test_cases = [('computer', 3, 'frpsxwhu'),
                      ('hello world', 5, 'mjqqt btwqi'),
                      ('abc', 1, 'bcd'),
                      ('xyz', 5, 'cde')]
        for message, key, expected in test_cases:
            with self.subTest(message=message, key=key):
                self.assertEqual(caesar_encode(message, key), expected)

    def test_decode(self):
        test_cases = [('frpsxwhu', 3, 'computer'),
                      ('mjqqt btwqi', 5, 'hello world'),
                      ('bcd', 1, 'abc'),
                      ('cde', 5, 'xyz')]
        for message, key, expected in test_cases:
            with self.subTest(message=message, key=key):
                self.assertEqual(caesar_decode(message, key), expected)

    def test_circular_encode_decode(self):
        test_cases = [('hello world', 5),
                      ('abc', 1)]
        for message, key in test_cases:
            with self.subTest(message=message, key=key):
                self.assertEqual(caesar_decode(caesar_encode(message, key), key), message)

if __name__ == '__main__':
    unittest.main()
