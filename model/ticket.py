class Ticket:

    def __init__(self, event, owner) -> None:
        self._event = event
        self._price = event.price
        self._owner = owner

    @property
    def price(self):
        return self._price

    @property
    def owner(self):
        return self._owner
