import sys

from network.utils import send_message


class CustomerView:
    def __init__(self, client):
        self._client = client
        self.main_menu()

    def main_menu(self):
        again = True
        while again:
            main_options = {"0": ["Encerrar Aplicativo", sys.exit],
                            "1": ["Listar Eventos", self.listing_events],
                            "2": ["Listar Meus Ingressos", self.listing_my_tickets],
                            }
            print(f"Olá {self._client.name}!! ")
            for key, item in main_options.items():
                print(f"{key}: {item[0]}")
            option = input("")
            func = main_options[option][1]
            again = func()

    def listing_events(self):
        content = {'session_id': self._client.session}
        while True:
            content['show'] = "all events"
            response = send_message('list events', content)
            result = response.response.get("result")
            i = 1
            print('0: Voltar ao menu anterior')
            for item in result:
                print(
                    f"{i}: {item['name']}\tPreço: {item['price']}\tIngressos disponíveis: {item['available_tickets']}")
                i = i + 1
            option = input("Número do evento: ")
            if option == '0':
                return True
            else:
                self.buy_tickets(result[int(option) - 1])

        pass

    def listing_my_tickets(self):
        content = {'session_id': self._client.session}
        response = send_message('list my tickets', content)
        result = response.response.get("result")
        for event_name, quantity in result.items():
            print(f"{event_name}\tQuantidade: {quantity}")
        input("Aperte Qualquer botão para voltar ao menu anterior!")
        return True

    def buy_tickets(self, event):
        print(f"Nome: {event['name']}")
        print(f"Quantidade de Ingressos: {event['size']}")
        print(f"Preço: {event['price']}")
        print(f"Ingressos disponíveis: {event['available_tickets']}")
        print("Para comprar digite um valor maior que 0")
        quantity = input()
        if int(quantity) <= 0:
            return
        else:
            content = {"session_id": self._client.session, "quantity": int(quantity), "event_id": event['id']}
            response = send_message('buy tickets', content)
            result = response.response.get("result")
            if result:
                print(f"Compra realizada com sucesso!")
            else:
                print(f"Não foi possível realizar a compra!")
        self.listing_my_tickets()
