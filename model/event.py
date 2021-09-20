# from types import prepare_class
import uuid

class Event:

    def __init__(self, name, size, price) -> None:
        self._id = uuid.uuid4()
        self._name = name
        self._size = size
        self._price = price
        self._tickets = []

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def price(self):
        return self._price

    @property
    def available_tickets(self):
        return self._size - len(self._tickets)

    def book_ticket(self, ticket):
        self._tickets.append(ticket)

    