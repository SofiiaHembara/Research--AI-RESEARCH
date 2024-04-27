def caesar_encode(message, key):
    encrypted_message = ""
    for char in message:
        if char == ' ':
            encrypted_message += ' '
        else:
            shifted = ord(char) + key
            if shifted > ord('z'):
                shifted -= 26
            encrypted_message += chr(shifted)
    return encrypted_message

def caesar_decode(message, key):
    decrypted_message = ""
    for char in message:
        if char == ' ':
            decrypted_message += ' '
        else:
            shifted = ord(char) - key
            if shifted < ord('a'):
                shifted += 26
            decrypted_message += chr(shifted)
    return decrypted_message
