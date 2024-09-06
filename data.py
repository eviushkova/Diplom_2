class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    REGISTER_ENDPOINT = "/auth/register"
    LOGIN_ENDPOINT = "/auth/login"
    DELETE_ENDPOINT = "/auth/user"
    UPDATE_ENDPOINT = "/auth/user"
    ORDER_ENDPOINT = "/orders"
    GET_INGREDIENTS_ENDPOINT = "/ingredients"
    GET_ALL_ORDERS_ENDPOINT = "/orders/all"

    REGISTER_URL = f'{BASE_URL}{REGISTER_ENDPOINT}'
    LOGIN_URL = f'{BASE_URL}{LOGIN_ENDPOINT}'
    DELETE_URL = f'{BASE_URL}{DELETE_ENDPOINT}'
    UPDATE_URL = f'{BASE_URL}{UPDATE_ENDPOINT}'
    ORDER_URL = f'{BASE_URL}{ORDER_ENDPOINT}'
    GET_INGREDIENTS_URL = f'{BASE_URL}{GET_INGREDIENTS_ENDPOINT}'


class Messages:
    LOGIN_ERROR = "email or password are incorrect"
    UPDATE_ERROR = "You should be authorised"
    MISSING_INGREDIENTS_ERROR = "Ingredient ids must be provided"
    AUTHORIZATION_ERROR = "You should be authorised"
