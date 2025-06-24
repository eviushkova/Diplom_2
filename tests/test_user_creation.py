import allure
import pytest
import requests
import data
from helpers import generate_user_data


class TestUserCreationAPI:
    @allure.title("Successfully create a new user")
    @allure.step("Send POST request to create a user and verify the response")
    def test_create_unique_user(self):
        user_data = generate_user_data()
        response = requests.post(data.Url.REGISTER_URL, json=user_data)

        assert response.status_code == 200, f'Status code is {response.status_code}'
        assert response.json()["success"] is True, f'Body={response.json()}'

    @allure.title("Attempt to create user with duplicate login")
    @allure.step(
        "Send POST request to create a user, then send another request with the same data and verify the response")
    def test_create_existing_user(self):
        user_data = generate_user_data()
        response_1 = requests.post(data.Url.REGISTER_URL, json=user_data)

        assert response_1.status_code == 200, f'Status code is {response_1.status_code}'
        assert response_1.json()["success"] is True, f'Body={response_1.json()}'

        response_2 = requests.post(data.Url.REGISTER_URL, json=user_data)

        assert response_2.status_code == 403, f'Status code is {response_2.status_code}'
        assert response_2.json()["success"] is False, f'Body={response_2.json()}'

    @allure.title("Create user with missing required fields")
    @allure.step("Send POST request to create a user with missing fields and verify the response")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field(self, missing_field):
        user_data = generate_user_data()
        user_data.pop(missing_field, None)

        response = requests.post(data.Url.REGISTER_URL, json=user_data)

        assert response.status_code == 403, f'Status code is {response.status_code}'
        assert response.json()["success"] is False, f'Body={response.json()}'
