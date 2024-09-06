# Stellar Burgers API Tests

This project contains automated API tests for the **Stellar Burgers** application. It verifies various user actions like creating an account, logging in, updating user data, creating and fetching orders using the **pytest** framework and **Allure** for reporting.


## Project Structure

The tests are organized into different classes based on the API functionality. Each test verifies specific API interactions, including:

1. **TestUserCreationAPI**: Tests for user registration.
2. **TestUserLoginAPI**: Tests for user login.
3. **TestUserDataUpdateAPI**: Tests for updating user data.
4. **TestOrderCreationAPI**: Tests for creating orders.
5. **TestGetOrdersAPI**: Tests for retrieving user orders.

## Tested Scenarios

### User Registration
- Create a unique user.
- Attempt to create a user with an existing email.
- Create a user with missing required fields.

### User Login
- Login with valid credentials.
- Attempt login with invalid credentials.

### User Data Update
- Update user data with valid authorization.
- Attempt to update user data without authorization.

### Order Creation
- Create an order with valid ingredients and authorization.
- Create an order without ingredients or authorization.
- Create an order with invalid ingredients' hash.

### Fetching Orders
- Fetch orders for an authorized user.
- Attempt to fetch orders without authorization.