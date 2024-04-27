def caesar_encode(message, key):
  """
  Функція кодування тексту шифром Цезаря.

  Args:
    message (str): Повідомлення для кодування.
    key (int): Ключ шифру (зміщення літер).

  Returns:
    str: Зашифроване повідомлення.
  """
  encoded_message = ""
  for char in message:
    if char.isalpha():
      new_char = ord(char) + key
      if new_char > ord('z'):
        new_char -= 26
      encoded_message += chr(new_char)
    else:
      encoded_message += char
  return encoded_message

def caesar_decode(message, key):
  """
  Функція декодування тексту, закодованого шифром Цезаря.

  Args:
    message (str): Зашифроване повідомлення.
    key (int): Ключ шифру (зміщення літер).

  Returns:
    str: Розшифроване повідомлення.
  """
  decoded_message = ""
  for char in message:
    if char.isalpha():
      new_char = ord(char) - key
      if new_char < ord('a'):
        new_char += 26
      decoded_message += chr(new_char)
    else:
      decoded_message += char
  return decoded_message