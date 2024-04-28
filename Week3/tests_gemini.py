import unittest
from correct_code import caesar_encode, caesar_decode

class CaesarTests(unittest.TestCase):
  TEST_DATA = [
      ("hello", 3, "khoor"),
      ("zebra", 3, "abcde"),
      ("hello world", 5, "jlmmp yaxpa"),
  ]

  def test_caesar(self):
    for message, key, expected_result in self.TEST_DATA:
      self.assertEqual(caesar_encode(message, key), expected_result)
      self.assertEqual(caesar_decode(message, key), expected_result[::-1])  # decode with reverse

if __name__ == "__main__":
  unittest.main()