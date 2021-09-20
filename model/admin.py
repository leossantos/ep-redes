import uuid

class Admin:
    def __init__(self, name, username) -> None:
        self._id = uuid.uuid4()
        self._name = name
        self._username = username