import unittest
from correct_code import caesar_encode, caesar_decode

class CaesarTests(unittest.TestCase):
  def test_encode_simple(self):
    self.assertEqual(caesar_encode("hello", 3), "khoor")
  
  def test_encode_wrap(self):
    self.assertEqual(caesar_encode("zebra", 3), "abcde")
  
  def test_encode_spaces(self):
    self.assertEqual(caesar_encode("hello world", 5), "jlmmp yaxpa")
  
  def test_decode_simple(self):
    self.assertEqual(caesar_decode("khoor", 3), "hello")
  
  def test_decode_wrap(self):
    self.assertEqual(caesar_decode("abcde", 3), "zebra")
  
  def test_decode_spaces(self):
    self.assertEqual(caesar_decode("jlmmp yaxpa", 5), "hello world")

if __name__ == "__main__":
  unittest.main()