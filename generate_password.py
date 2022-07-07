import random


characters = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!?#$%&()*+,-./:;<>_?@[]{}|~',
              '1234567890']


def generate_random_password():
    password = ''
    for i in range(16):
        random_number = random.randint(0, 3)
        random_string_list = characters[random_number]
        random_character = random.randint(0, len(random_string_list) - 1)
        password += random_string_list[random_character]
    return password


def generate_random_num():
    final_number = ''
    for i in range(6):
        random_num = random.randint(0, 9)
        while str(random_num) in final_number:
            random_num = random.randint(0, 9)
        final_number += str(random_num)
    return final_number


def generate_key():
    key = ''
    for i in range(30):
        random_number = random.randint(0, 3)
        random_string_list = characters[random_number]
        random_character = random.randint(0, len(random_string_list) - 1)
        key += random_string_list[random_character]
    return key
