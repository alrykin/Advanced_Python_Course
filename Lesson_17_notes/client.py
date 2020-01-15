import socket

server_address = ("127.0.0.1", 8090)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(server_address)

while True:
    data_to_sent = input().encode('utf-8')

    if len(data_to_sent) < 1:
        continue

    if data_to_sent == b"exit":
        soc.close()
        break

    soc.send(data_to_sent)

    data = soc.recv(1024)
    print(data)
