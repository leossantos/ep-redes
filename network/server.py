import uuid

from model.admin import Admin
from model.customer import Customer
from model.event import Event

class Server:
    def __init__(self):
        self._users = {}
        self._events = {}
        self._sessions = {}

    def create_user(self, name, username, password, user_type):
        if user_type == 'admin':
            user = Admin(username, name, password)
        else:
            user = Customer(name, username, password)
        self._users[user.id] = user

    def create_event(self, name, size, price, owner):
        event = Event(name, size, price, owner)
        self._events[event.id] = event

    def sign_in(self, username, password):
        for user_id, user in self._users.items():
            if user.username == username and user.password == password:
                session_id = uuid.uuid4()
                user_type = 'customer' if type(user) == Customer else 'admin'
                self._sessions[session_id] = user
                return {'session_id': session_id.int, 'user_type': user_type, 'name': user.name}
        return None

    def sign_up(self, username, password, name, user_type):
        if username in self._users:
            return None
        if user_type == 'admin':
            user = Admin(username, name, password)
        else:
            user = Customer(username, password, name)
        session_id = uuid.uuid4()
        self._sessions[session_id] = user
        self._users[user.id] = user
        return {'session_id': session_id.int, 'user_type': user_type, 'name': user.name}

    def username_exists(self, username):
        return

