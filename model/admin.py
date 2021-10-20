import uuid

from model.event import Event
from model.user import User


class Admin(User):
    def __init__(self, username, nome, password) -> None:
        super().__init__(nome, username, password)

    def create_event(self, name, size, price):
        event = Event(name=name, size=size, price=price, owner=self)
        return event
