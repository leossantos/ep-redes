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

    def create_event(self, name, size, price, session_id):
        owner = self._sessions[session_id]
        event = Event(name, size, price, owner)
        self._events[event.id.int] = event
        return {"Success": True}

    def sign_in(self, username, password):
        for user_id, user in self._users.items():
            if user.username == username and user.password == password:
                session_id = uuid.uuid4()
                user_type = 'customer' if type(user) == Customer else 'admin'
                self._sessions[session_id.int] = user
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
        self._sessions[session_id.int] = user
        self._users[user.id] = user
        return {'session_id': session_id.int, 'user_type': user_type, 'name': user.name}

    def update_event(self, query):
        event_id = query.get("event_id")
        event = self._events[event_id]
        session_id = query.get("session_id")
        admin = self._sessions[session_id]
        if event.owner == admin:
            if "name" in query:
                event.name = query.get("name")
            if "size" in query:
                event.size = query.get("size")
            if "price" in query:
                event.price = query.get("price")
            return {"Success": True}
        return {"Success": False}

    def delete_event(self, query):
        event_id = query.get("event_id")
        event = self._events[event_id]
        session_id = query.get("session_id")
        admin = self._sessions[session_id]
        if event.owner == admin:
            del self._events[event_id]
            return {"Success": True}
        return {"Success": False}

    def list_events(self, session_id, show):
        admin = self._sessions[session_id]
        if show == 'my events':
            events = {}
            for event_id, event in self._events.items():
                if event.owner == admin:
                    print(event_id)
                    events[event_id] = event
        else:
            events = self._events
        result = []
        for event_id, event in events.items():
            result.append(event.to_dict())
        return result

    def list_my_tickets(self, session_id):
        customer = self._sessions[session_id]
        return customer.tickets
        pass

    def buy_tickets(self, session_id, event_id, quantity):
        customer = self._sessions[session_id]
        event = self._events[event_id]
        content = {"Success": customer.buy_ticket(event, quantity)}
        return content

