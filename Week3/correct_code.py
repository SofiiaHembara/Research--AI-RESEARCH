def caesar_encode(message, key):
    encrypted_message = ""
    for char in message:
        if char == ' ':
            encrypted_message += ' '
        else:
            shifted = ord(char) - ord('a') + key
            encrypted_message += chr((shifted % 26) + ord('a'))
    return encrypted_message

def caesar_decode(message, key):
    decrypted_message = ""
    for char in message:
        if char == ' ':
            decrypted_message += ' '
        else:
            shifted = ord(char) - ord('a') - key
            decrypted_message += chr((shifted % 26) + ord('a'))
    return decrypted_message
