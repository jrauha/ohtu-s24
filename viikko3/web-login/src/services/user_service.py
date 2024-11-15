from entities.user import User
from repositories.user_repository import user_repository as default_user_repository


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def _validate_username(self, username):
        # At least 3 characters long with only letters a-z
        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")

        if not username.isalpha():
            raise UserInputError("Username must only contain letters a-z")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is already in use")

    def _validate_password(self, password):
        # At least 8 characters long with at least one number
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")

        if all(char.isalpha() for char in password):
            raise UserInputError(
                "Password must contain at least one special character or number"
            )

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(User(username, password))

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if password != password_confirmation:
            raise UserInputError("Passwords do not match")

        self._validate_username(username)
        self._validate_password(password)


user_service = UserService()
