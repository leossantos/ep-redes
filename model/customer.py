import uuid
from model.ticket import Ticket


class Customer:
    def __init__(self, nome) -> None:
        self._id = uuid.uuid4()
        self._nome = nome
        self._tickets = {}

    def buy_ticket(self, event, quantity):
        if (quantity <= event.available_tickets):
            if event.name in self._tickets:
                self._tickets[event.name] = []
            for i in range(0, quantity):
                ticket = Ticket(event=event, owner=self)
                self._tickets[event.name].append(ticket)
                event.book_ticket(ticket)

        else:
            print('Não há ingressos suficientes')
