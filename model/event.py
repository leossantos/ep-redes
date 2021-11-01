# from types import prepare_class
import uuid


class Event:

    def __init__(self, name, size, price, owner) -> None:
        self._id = uuid.uuid4()
        self._name = name
        self._size = size
        self._price = price
        self._tickets = []
        self._owner = owner

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > 0:
            self._size = size

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price > 0:
            self._price = price

    @property
    def available_tickets(self):
        return self._size - len(self._tickets)

    def book_ticket(self, ticket):
        self._tickets.append(ticket)

    @property
    def owner(self):
        return self._owner

    def to_dict(self):
        return {"id": self._id.int, "name": self._name, "size": self._size, "price": self._price,
                "available_tickets": self.available_tickets}
