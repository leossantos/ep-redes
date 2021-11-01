class Client:

    def __init__(self, session, user_type, name):
        self._session = session
        self._user_type = user_type
        self._name = name

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, session):
        self._session = session

    @property
    def user_type(self):
        return self._user_type

    @property
    def name(self):
        return self._name
