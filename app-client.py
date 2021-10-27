import sys
import socket
import selectors
import traceback
import json

from network.libclient import Message

sel = selectors.DefaultSelector()


def create_request(action, value):
    if action in ("search", "login"):
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
    else:
        return dict(
            type="binary/custom-client-binary-type",
            encoding="binary",
            content=bytes(action + value, encoding="utf-8"),
        )


def start_connection(host, port, request):
    addr = (host, port)
    print("starting connection to", addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


def send_message():
    start_connection(host, port, request)

    try:
        while True:
            events = sel.select(timeout=1)
            for key, mask in events:
                message = key.data
                try:
                    message.process_events(mask)
                except Exception:
                    print(
                        "main: error: exception for",
                        f"{message.addr}:\n{traceback.format_exc()}",
                    )
                    message.close()
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sel.close()


# if len(sys.argv) != 5:
#     print("usage:", sys.argv[0], "<host> <port> <action> <value>")
#     sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
action = sys.argv[3]
request = None
if action == 'login':
    username = sys.argv[4]
    password = sys.argv[5]
    value = {"username": username, "password": password}
    request = create_request(action, json.dumps(value))
    send_message()
    resp = input("Deu certo?")
    if resp == 'Sim': sys.exit()
