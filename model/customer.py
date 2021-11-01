from model.ticket import Ticket
from model.user import User


class Customer(User):
    def __init__(self, username, password, name) -> None:
        super().__init__(name, username, password)
        self._tickets = {}

    def buy_ticket(self, event, quantity):
        if quantity <= event.available_tickets:
            if event.name not in self._tickets:
                self._tickets[event.name] = []
            for i in range(0, quantity):
                ticket = Ticket(event=event, owner=self)
                self._tickets[event.name].append(ticket)
                event.book_ticket(ticket)

        else:
            print('Não há ingressos suficientes')
