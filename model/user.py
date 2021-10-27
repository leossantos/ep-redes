import uuid


class User:
    def __init__(self, name, username, password) -> None:
        self._id = uuid.uuid4()
        self._name = name
        self._username = username
        self._password = password

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def name(self):
        return self._name
