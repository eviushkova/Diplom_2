class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    REGISTER_ENDPOINT = "/auth/register"
    LOGIN_ENDPOINT = "/auth/login"
    DELETE_ENDPOINT = "/auth/user"
    UPDATE_ENDPOINT = "/auth/user"

    REGISTER_URL = f"{BASE_URL}{REGISTER_ENDPOINT}"
    LOGIN_URL = f"{BASE_URL}{LOGIN_ENDPOINT}"
    DELETE_URL = f"{BASE_URL}{DELETE_ENDPOINT}"
    UPDATE_URL = f"{BASE_URL}{UPDATE_ENDPOINT}"


class Messages:
    MESSAGE_LOGIN_ERROR = "email or password are incorrect"
    MESSAGE_UPDATE_ERROR = "You should be authorised"
