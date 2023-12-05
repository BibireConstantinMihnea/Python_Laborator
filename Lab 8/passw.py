import string
import random

def generate(length, special, numbers, mixed_case):
    characters = string.ascii_letters if mixed_case else string.ascii_lowercase
    characters += string.digits if numbers else ''
    characters += string.punctuation if special else ''

    for _ in range(length):
        password = ''.join(random.choice(characters))

    return password
