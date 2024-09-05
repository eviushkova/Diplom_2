import allure
import requests
import data


class TestUserDataUpdateAPI:
    @allure.title("Update registered user data")
    @allure.step("Send PATCH request to update registered user's data with new email, password, and name")
    def test_registered_user_data_update(self, create_user_with_token):
        email, password, name, access_token = create_user_with_token
        response = requests.patch(data.Url.UPDATE_URL, headers={"Authorization": f'{access_token}'}, json={
            "email": f'{email}new',
            "password": f'{password}new',
            "name": f'{name}new'
        })

        assert response.status_code == 200, f'Status code is {response.status_code}'
        assert response.json()["success"] is True, f'Body={response.json()}'

    @allure.title("Update unregistered user data")
    @allure.step("Send PATCH request to update user data without authorization")
    def test_unregistered_user_data_update(self, create_user_with_token):
        email, password, name, _ = create_user_with_token
        response = requests.patch(data.Url.UPDATE_URL, json={
            "email": f'{email}new',
            "password": f'{password}new',
            "name": f'{name}new'
        })

        assert response.status_code == 401, f'Status code is {response.status_code}'
        assert response.json()["message"] == data.Messages.MESSAGE_UPDATE_ERROR
