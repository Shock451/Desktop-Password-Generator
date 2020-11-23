import string
import random
import pyperclip

special_char = [33,35,36,37,38]
elements = "".join(map(chr, special_char))
print(elements)
# character = string.ascii_letters + string.digits + elements
# password = "".join(random.choice(character) for i in range(random.randint(8, 15)))

# print(password)
