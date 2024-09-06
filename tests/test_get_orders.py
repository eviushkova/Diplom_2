import allure
import requests
import data


class TestGetOrdersAPI:
    @allure.title("Get orders for authorized user")
    @allure.step("Send GET request to fetch orders for an authorized user")
    def test_get_orders_for_authorized_user(self, create_user_with_token):
        _, _, _, access_token = create_user_with_token

        response = requests.get(data.Url.ORDER_URL, headers={"Authorization": f'{access_token}'})

        assert response.status_code == 200, f'Status code is {response.status_code}'
        assert response.json()["success"] is True, f'Body={response.json()}'

    @allure.title("Get orders for unauthorized user")
    @allure.step("Send GET request to fetch orders without authorization")
    def test_get_orders_for_unauthorized_user(self):
        response = requests.get(data.Url.ORDER_URL)

        assert response.status_code == 401, f'Status code is {response.status_code}'
        assert response.json()["message"] == data.Messages.AUTHORIZATION_ERROR
