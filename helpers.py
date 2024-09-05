from random import random
from faker import Faker

fake = Faker()


def generate_user_data():
    email = fake.email()
    password = fake.password()
    name = fake.first_name()

    return {
        "email": email,
        "password": password,
        "name": name
    }
