import random
import string


def generate_login():
    number = random.randint(100, 999)
    login = "elenabochkova131" + str(number) + "@yandex.ru"
    return login


def generate_password(length: int):
    text = [random.choice(string.ascii_lowercase + string.digits if i != 5 else string.ascii_uppercase) for i in
            range(length)]
    return ''.join(text)