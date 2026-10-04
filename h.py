import random
import string

character_pool = string.ascii_lowercase + string.digits
random_characters = ''.join(random.choices(character_pool, k=6))


