import random

def generate_password():
    letter_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    letter_upper = ["A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_character = ['!', '"', '·', '$', '%', '&', '/', '(', ')']
    counter = 0
    inner_lower = [ ]
    inner_upper = [ ]
    inner_number = [ ]
    inner_character = [ ]

    #It takes 5 lower letter list
    while counter != 5:
        counter += 1
        random_number = random.randrange(0, 9) 
        inner_lower.append(letter_lower[random_number])
    print(inner_lower)

    counter = 0

    while counter != 5:
        counter += 1
        random_number = random.randrange(0, 9) 
        inner_upper.append(letter_upper[random_number])
    print(inner_upper)

    counter = 0

    while counter != 5:
        counter += 1
        random_number = random.randrange(0, 9) 
        inner_number.append(number[random_number])
    print(inner_number)

    counter = 0

    while counter != 5:
        counter += 1
        random_number = random.randrange(0, 9) 
        inner_character.append(special_character[random_number])
    print(inner_character)
    
    password_list = inner_lower + inner_upper + inner_number + inner_character
    password_inner = ""
    password_inner = password_inner.join(password_list)

    return password_inner




def run():
    password = generate_password()
    print(password)


if __name__ == '__main__':
    run()