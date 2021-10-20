import uuid


class User:
    def __init__(self, nome, username, password) -> None:
        self._id = uuid.uuid4()
        self._nome = nome
        self._username = username
        self._password = password
