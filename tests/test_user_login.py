import allure
import requests
import data


class TestUserLoginAPI:
    @allure.title("Successful login with valid credentials")
    @allure.step("Send POST request to login with valid credentials and verify the response")
    def test_login_user_success(self, create_user):
        email, password = create_user
        response = requests.post(data.Url.LOGIN_URL, json={
            "email": email,
            "password": password
        })

        assert response.status_code == 200, f'Status code is {response.status_code}'
        assert response.json()["success"] is not None, f'Body={response.json()}'

    @allure.title("Login attempt with invalid credentials")
    @allure.step("Send POST request with invalid credentials and verify the response")
    def test_login_user_invalid_credentials(self, create_user):
        email, password = create_user
        response = requests.post(data.Url.LOGIN_URL, json={
            "email": email,
            "password": f'{password}test'
        })

        assert response.status_code == 401, f'Status code is {response.status_code}'
        assert response.json()["message"] == data.Messages.LOGIN_ERROR
