import sys

from network.utils import send_message


class AdminView:
    def __init__(self, client):
        self._client = client
        self.main_menu()

    def main_menu(self):
        again = True
        while again:
            main_options = {"0": ["Encerrar Aplicativo", sys.exit],
                            "1": ["Listar Eventos", self.listing_events],
                            "2": ["Listar Meus Eventos", self.listing_my_events],
                            "3": ["Criar Evento", self.create_event]
                            }
            print(f"Olá {self._client.name}!! ")
            for key, item in main_options.items():
                print(f"{key}: {item[0]}")
            option = input("")
            func = main_options[option][1]
            again = func()

    def update_event(self, event):
        print("Apenas aperte Enter caso não queira editar um dos campos:")
        print("Não é possível editar o preço, caso o evento já tenha realizado uma venda!")
        name = input(f"Nome ({event['name']}): ")
        size = input(f"Quantidade de ingressos ({event['size']}): ")
        price = ''
        if event['available_tickets'] == event['size']:
            price = input(f"Preço ({event['price']}): ")
        content = {}
        if name != '':
            content['name'] = name
            print(f"{event['name']} -> {name}")
        if size != '':
            size = int(size)
            content['size'] = size
            print(f"{event['size']} -> {size}")
        if price != '':
            price = float(price)
            content['price'] = price
            print(f"{event['price']} -> {price}")
        if content != {}:
            content['session_id'] = self._client.session
            content['event_id'] = event['id']
            response = send_message('update event', content)
            result = response.response.get("result")
            if result:
                print(f"Evento {event['name']} atualizado com sucesso!")
            else:
                print(f"Não foi possível atualizar o evento {event['name']} ")

    def detail_event(self, event):
        print(f"Id: {event['id']}")
        print(f"Quantidade de Ingressos: {event['size']}")
        print(f"Preço: {event['price']}")
        print(f"Ingressos disponíveis: {event['available_tickets']}")
        print("0: Voltar ao menu Anterior")
        print("1: Editar")
        print("2: Deletar")
        option = input("")
        if option == "0":
            return
        if option == '1':
            self.update_event(event)
        else:
            self.delete_event(event)

    def listing_events(self, my_events=False):
        content = {'session_id': self._client.session}
        while True:
            if my_events:
                content['show'] = "my events"
                print("Para editar/deletar escolha um dos eventos:")
            else:
                content['show'] = "all events"
            response = send_message('list events', content)
            result = response.response.get("result")
            i = 1
            print('0: Voltar ao menu anterior')
            for item in result:
                print(
                    f"{i}: {item['name']}")

            option = input("")
            if option == '0':
                return True
            else:
                self.detail_event(result[int(option) - 1])

    def listing_my_events(self):
        return self.listing_events(True)

    def create_event(self):
        name = input(f"Nome: ")
        size = int(input(f"Quantidade de ingressos: "))
        price = float(input(f"Preço: "))
        content = {"name": name, "size": size, "price": price, 'session_id': self._client.session}
        response = send_message('create event', content)
        result = response.response.get("result")
        if result:
            print(f"Evento {name} criado com sucesso!")
        else:
            print(f"Não foi possível criar o evento {name}")
        return True

    def delete_event(self, event):
        content = {"event_id": event['id'], "session_id": self._client.session}
        response = send_message('delete event', content)
        result = response.response.get("result")
        if result:
            print(f"Evento {event['name']} deletado com sucesso!")
        else:
            print(f"Não foi possível deletar o evento {event['name']} ")
