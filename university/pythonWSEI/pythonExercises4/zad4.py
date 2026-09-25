import random
import string


def generate_password(length, min_letters=1, min_digits=1):
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        letters_count = sum(c.isalpha() for c in password)
        digits_count = sum(c.isdigit() for c in password)
        if letters_count >= min_letters and digits_count >= min_digits:
            yield password


password_generator = generate_password(length=8, min_letters=4, min_digits=2)

for _ in range(5):
    print(next(password_generator))