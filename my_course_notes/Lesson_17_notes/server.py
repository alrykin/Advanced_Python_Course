import socket
from threading import Thread

server_address = ("127.0.0.1", 8090)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(server_address)

soc.listen(5)


def client_handler(client_socket, client_address):
    while True:
        data = client_socket.recv(1024)
        print(f"new message from {client_address}")
        print(data)
        client_socket.send(data[::-1])

        if not data:
            break


while True:
    client, address = soc.accept()
    print(f'Client {address}')
    Thread(target=client_handler, args=(client, address),
        name=address).start()

#     while True:
#         data = client.recv(1024)
#         print(data)
#         client.send(data[::-1])
#
#         if not data:
#             break
