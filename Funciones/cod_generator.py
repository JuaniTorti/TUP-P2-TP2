import random
import string

# get random password of length 5 with letters, digits, and symbols
def generar():
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(5))
    return cod