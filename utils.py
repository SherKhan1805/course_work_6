
from random import random
import string

NULLABLE = {'blank': True, 'null': True}


def generate_password():
    length = 6
    characters = string.ascii_letters + string.digits + string.punctuation

    password = '8989'
    # password = ''.join(random.choice(characters) for i in range(length))

    return password



