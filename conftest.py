import allure
import pytest
import requests
import data
from helpers import generate_user_data


@allure.step("Setup and teardown for user creation: create a new user and provide credentials")
@pytest.fixture
def create_user():
    user_data = generate_user_data()
    response = requests.post(data.Url.REGISTER_URL, json=user_data)
    access_token = response.json()["accessToken"]
    yield user_data["email"], user_data["password"]

    requests.delete(data.Url.DELETE_URL, headers={"Authorization": f'{access_token}'})


@pytest.fixture
def create_user_with_token():
    user_data = generate_user_data()
    response = requests.post(data.Url.REGISTER_URL, json=user_data)
    access_token = response.json()["accessToken"]
    yield user_data["email"], user_data["password"], user_data["name"], access_token

    requests.delete(data.Url.DELETE_URL, headers={"Authorization": f'{access_token}'})
