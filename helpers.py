import requests
from faker import Faker
import data

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


def get_ingredients_list():
    response = requests.get(data.Url.GET_INGREDIENTS_URL).json()

    ingredient_ids = []

    for ingredient in response["data"]:
        ingredient_id = ingredient["_id"]
        ingredient_ids.append(ingredient_id)

    return ingredient_ids
