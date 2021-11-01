from network.utils import send_message
from network.client import Client
from view.admin import AdminView


def sign_up():
    while True:
        username = input("Username: ")
        name = input("Nome: ")
        password = input("Senha: ")
        user_type = input("Tipo de usuário(admin/cliente): ")
        value = {"username": username, "password": password, "name": name, "user_type": user_type}
        response = send_message("sign_up", value)
        result = response.response.get("result")
        if result:
            session = result.get("session_id")
            user_type = result.get("user_type")
            name = result.get("name")
            print("Cadastro realizado com sucesso")
            return Client(session, user_type, name)
        print("Username já existente!!")


def sign_in():
    while True:
        username = input("Username: ")
        password = input("Senha: ")
        value = {"username": username, "password": password}
        response = send_message("sign in", value)
        result = response.response.get("result")
        if result:
            session = result.get("session_id")
            user_type = result.get("user_type")
            name = result.get("name")
            print("Login Realizado com Sucesso!!")
            return Client(session, user_type, name)
        print("Username ou senhas estão incorretos!!!")


# if len(sys.argv) != 5:
#     print("usage:", sys.argv[0], "<host> <port> <action> <value>")
#     sys.exit(1)

host = '127.0.0.1'
port = 65432
registered = input("Já tem cadastro?(s/n)\n")

if registered == 's':
    client = sign_in()
else:
    client = sign_up()
print(f"{client.name}\t{client.session}")
if client.user_type == 'admin':
    AdminView(client)
else:
    pass

# if resp == 'Sim': sys.exit()
