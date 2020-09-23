import random

def sort_it(random_list):
    if len(random_list) < 2:
        return random_list

    else:
        middle_list = len(random_list) // 2
        left = random_list[:middle_list]
        right = random_list[middle_list:]

        sort_it(left)
        sort_it(right)
    
    # TODO Segunda parte, ordenar las listas pequeñitas
    
    print(f'left {left} and right {right}')


if __name__ == '__main__':
    # list_length = int(input("What is the length of your list?  "))
    list_length = 2
    random_list =[random.randint(0, 100) for i in range(list_length)]
    print(random_list)
    sort_it(random_list)