def process_message(message: str):
    message_characters = [character for character in message]
    final_message = ''

    try:
        for character in message_characters:
            if ord(character) >= ord("A") and ord(character) <= ord('Z'):
                new_decimal_code = ord("Z") - (ord(character) - ord("A"))
                final_message += chr(new_decimal_code)
            elif ord(character) >= ord("a") and ord(character) <= ord("z"):
                new_decimal_code = ord("z") - (ord(character) - ord("a"))
                final_message += chr(new_decimal_code)
            else:
                final_message += character
        
        return f"The message is: {final_message}"
    
    except Exception as error:
        return f"The error: {error} occurred"

# < ------------ NOTES ------------ >
# new_decimal_code = ord("Z") - (ord(character) - ord("A"))
#   the same forumla can be used to encrypt and decrypt the message