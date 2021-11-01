import sys

from network.utils import send_message


def delete_event(event):
    response = send_message('delete event', event['id'])
    result = response.response.get("result")
    if result:
        print(f"Evento {event['name']} deletado com sucesso!")
    else:
        print(f"Não foi possível deletar o evento {event['name']} ")


def update_event(event):
    print("Apenas aperte Enter caso não queira editar um dos campos:")
    print("Não é possível editar o preço, caso o evento já tenha realizado uma venda!")
    name = input(f"Nome ({event['name']}: ")
    size = int(input(f"Quantidade de ingressos ({event['size']}: "))
    price = ''
    if event['available_tickets'] == event['size']:
        price = float(input(f"Preço ({event['price']}: "))
    content = {}
    if name != '':
        content['name'] = name
        print(f"{event['name']} -> {name}")
    if size != '':
        content['size'] = name
        print(f"{event['size']} -> {size}")
    if price != '':
        content['price'] = name
        print(f"{event['price']} -> {price}")
    if content != {}:
        response = send_message('update event', content)
        result = response.response.get("result")
        if result:
            print(f"Evento {event['name']} atualizado com sucesso!")
        else:
            print(f"Não foi possível atualizar o evento {event['name']} ")


def create_event():
    name = input(f"Nome: ")
    size = int(input(f"Quantidade de ingressos: "))
    price = float(input(f"Preço: "))
    content = {
        "name": name,
        "size": size,
        "price": price
    }
    response = send_message('update event', content)
    result = response.response.get("result")
    if result:
        print(f"Evento {name} criado com sucesso!")
    else:
        print(f"Não foi possível criar o evento {name} ")


def detail_event(event):
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
        update_event(event)
    else:
        delete_event(event)


def listing_events(my_events=False):
    while True:
        if my_events:
            response = send_message('list events', "my events")
            print("Para editar/deletar escolha um dos eventos:")
        else:
            response = send_message("list events", "all events")
        result = response.response.get("result")
        i = 1
        options = {'0': 'Voltar ao menu anterior'}
        for key, item in result.items():
            print(
                f"{i}:\t{item['name']}")

        option = input("")
        if option == '0':
            return
        else:
            detail_event(result[int(option) - 1])


def listing_my_events():
    return listing_events(True)


class AdminView:
    def __init__(self, client):
        self._client = client
        self.main_menu()

    def main_menu(self):
        again = True
        while again:
            main_options = {"0": ["Encerrar Aplicativo", sys.exit],
                            "1": ["Listar Eventos", listing_events],
                            "2": ["Listar Meus Eventos", listing_my_events],
                            "3": ["Criar Evento", create_event]
                            }
            print(f"Olá {self._client.name}!! ")
            for key, item in main_options.items():
                print(f"{key}: {item[0]}")
            option = input("")
            func = main_options[option]
            again = func()
