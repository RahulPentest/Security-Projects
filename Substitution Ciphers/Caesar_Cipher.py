def encrypt_message(message: str, shift: int):
    message_characters = [character for character in message]
    encrypted_message = ''
    
    try:
        for character in message_characters:
            if ord(character) >= ord("A") and ord(character) <= ord('Z'):
                new_position = (ord(character) - ord('A') + shift) % 26
                encrypted_message += chr(new_position + ord('A'))
            elif ord(character) >= ord("a") and ord(character) <= ord("z"):
                new_position = (ord(character) - ord('a') + shift) % 26
                encrypted_message += chr(new_position + ord('a'))
            else:
                encrypted_message += character
        
        return f"The encrypted message is: {encrypted_message}"
    
    except Exception as error:
        return f"The error: {error} occurred"
    
def decrypt_message(message: str, shift: int):
    message_characters = [character for character in message]
    decrypted_message = ''

    try:
        for character in message_characters:
            if ord(character) >= ord("A") and ord(character) <= ord('Z'):
                new_position = (ord(character) - ord('A') - shift) % 26
                decrypted_message += chr(new_position + ord('A'))
            elif ord(character) >= ord("a") and ord(character) <= ord("z"):
                new_position = (ord(character) - ord('a') - shift) % 26
                decrypted_message += chr(new_position + ord('a'))
            else:
                decrypted_message += character
        
        return f"The decrypted message is: {decrypted_message}"
    except Exception as error:
        return f"The error: {error} occurred"

# < ------------ NOTES ------------ >
# new_position = (ord(character) - ord('A') - shift) % 26
#   the + shift and - shift depends on whether the message is being encrypted or decrypted