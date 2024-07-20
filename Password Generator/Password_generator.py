import random
def generate(letters, special_characters, numbers, password_length):

    generated_password = ''
    try:
        for i in range(password_length):

            options = ["L", "SC", "N"]
            chosen_option = random.choice(options)

            if chosen_option == "L":
                use_upper = True if random.randint(0, 1) == 1 else False
                generated_password += random.choice(letters).upper() if use_upper else random.choice(letters)
            elif chosen_option == "SC":
                generated_password += random.choice(special_characters)
            elif chosen_option == "N":
                generated_password += random.choice(numbers)
    except:
        print("Incorrect arguments may have been passed")
        return None

    return generated_password

# < ------------ NOTES ------------ >
# .randint(<number>, <another number>) will choose a number between the given numbers (which may be chosen)
# .choice(<list or tuple or string>) will choose an element from the list, tuple, or string