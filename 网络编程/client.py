import socket


client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect(('localhost', 5566))

while True:
    data = client2.recv(1024)
    if data != b'':
        print('received', data)
    else:
        pass




