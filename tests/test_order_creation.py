import allure
import requests
import data
from helpers import get_ingredients_list


class TestOrderCreationAPI:
    @allure.title("Create order with authorization and valid ingredients")
    @allure.step("Send POST request with valid token and valid ingredients to create an order")
    def test_create_order_with_auth_and_with_ingredients(self, create_user_with_token):
        _, _, _, access_token = create_user_with_token
        ingredients = get_ingredients_list()
        ingredients_data = {"ingredients": ingredients}

        response = requests.post(data.Url.ORDER_URL, headers={"Authorization": f'{access_token}'},
                                 json=ingredients_data)

        assert response.status_code == 200, f'Status code is {response.status_code}'
        assert response.json()["success"] is True, f'Body={response.json()}'

    @allure.title("Create order with authorization and without ingredients")
    @allure.step("Send POST request with valid token and without ingredients to create an order")
    def test_create_order_with_auth_and_without_ingredients(self, create_user_with_token):
        _, _, _, access_token = create_user_with_token

        response = requests.post(data.Url.ORDER_URL, headers={"Authorization": f'{access_token}'})

        assert response.status_code == 400, f'Status code is {response.status_code}'
        assert response.json()["message"] == data.Messages.MISSING_INGREDIENTS_ERROR

    @allure.title("Create order with authorization and invalid ingredient hash")
    @allure.step("Send POST request with valid token and invalid ingredients' hash to create an order")
    def test_create_order_with_auth_and_with_invalid_hash_ingredients(self, create_user_with_token):
        _, _, _, access_token = create_user_with_token
        ingredients = get_ingredients_list()
        ingredients = [ingredient + "modified" for ingredient in ingredients]
        ingredients_data = {"ingredients": ingredients}

        response = requests.post(data.Url.ORDER_URL, headers={"Authorization": f'{access_token}'},
                                 json=ingredients_data)

        assert response.status_code == 500, f'Status code is {response.status_code}'

    @allure.title("Create order without authorization and without ingredients")
    @allure.step("Send POST request without token and without ingredients to create an order")
    def test_create_order_without_auth_and_without_ingredients(self):
        response = requests.post(data.Url.ORDER_URL)

        assert response.status_code == 400, f'Status code is {response.status_code}'
        assert response.json()["message"] == data.Messages.MISSING_INGREDIENTS_ERROR

    @allure.title("Create order without authorization and with invalid ingredients' hash")
    @allure.step("Send POST request without token and with invalid ingredients' hash to create an order")
    def test_create_order_without_auth_and_with_invalid_hash_ingredients(self):
        ingredients = get_ingredients_list()
        ingredients = [ingredient + "modified" for ingredient in ingredients]
        ingredients_data = {"ingredients": ingredients}

        response = requests.post(data.Url.ORDER_URL, json=ingredients_data)

        assert response.status_code == 500, f'Status code is {response.status_code}'

    @allure.title("Create order without authorization and with valid ingredients' hash")
    @allure.step("Send POST request with token and with valid ingredients' hash to create an order")
    def test_create_order_without_auth_and_with_valid_hash_ingredients(self):
        ingredients = get_ingredients_list()
        ingredients_data = {"ingredients": ingredients}

        response = requests.post(data.Url.ORDER_URL, json=ingredients_data)

        assert response.status_code == 200, f'Status code is {response.status_code}'
        assert response.json()["success"] is True, f'Body={response.json()}'
