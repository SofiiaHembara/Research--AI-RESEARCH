import unittest
from correct_code import caesar_encode, caesar_decode

class TestCaesar(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(caesar_encode('computer', 3), 'frpsxwhu')
        self.assertEqual(caesar_encode('hello world', 5), 'mjqqt btwqi')
        self.assertEqual(caesar_encode('abc', 1), 'bcd')
        self.assertEqual(caesar_encode('xyz', 5), 'cde')

    def test_decode(self):
        self.assertEqual(caesar_decode('frpsxwhu', 3), 'computer')
        self.assertEqual(caesar_decode('mjqqt btwqi', 5), 'hello world')
        self.assertEqual(caesar_decode('bcd', 1), 'abc')
        self.assertEqual(caesar_decode('cde', 5), 'xyz')

    def test_circular_encode_decode(self):
        self.assertEqual(caesar_decode(caesar_encode('hello world', 5), 5), 'hello world')
        self.assertEqual(caesar_decode(caesar_encode('abc', 1), 1), 'abc')

if __name__ == '__main__':
    unittest.main()
