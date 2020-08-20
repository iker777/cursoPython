import random


#It gets a list of 5 characters
def randomize_list(list):
    counter = 0
    character_list = [ ]

    while counter != 5:
        counter += 1
        random_number = random.randrange(0, 9) 
        character_list.append(list[random_number])

    return character_list

def generate_password():
    #Random Character list
    letter_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    letter_upper = ["A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_character = ['!', '"', '·', '$', '%', '&', '/', '(', ')']

    #I have 4 lists of random Characters
    inner_lower = randomize_list(letter_lower)
    inner_upper = randomize_list(letter_upper)
    inner_number = randomize_list(number)
    inner_character = randomize_list(special_character)

    #It gets 5 lower letter list
    password_list = inner_lower + inner_upper + inner_number + inner_character
    password_inner = ""
    password_inner = password_inner.join(password_list)

    return password_inner


def run():
    password = generate_password()
    print("Tu contraseña secreta es:\n" + password)


if __name__ == '__main__':
    run()