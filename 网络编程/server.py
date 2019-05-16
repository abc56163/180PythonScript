import socket
import configparser
import os
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('局域网消息广播')
window.geometry('1100x500+500+50')
window.resizable(width=False, height=False)

# menubar = tk.Menu(window)
# window.config(menu=menubar)
# menu1 = tk.Menu(menubar,tearoff=False)
# # menu1.add_separator()
# menu1.add_command(label='地址修改')
# menubar.add_cascade(label='设置',menu=menu1)

config = configparser.ConfigParser()
config.read(os.path.dirname(__file__)+'/config.ini')
config.sections()
host = (config.get('DEFAULT', 'host'), int(config.get('DEFAULT', 'port')))

def socket_server1(host,msg):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(host)
    server.listen(1000)
    print('等待客户端连接……')
    connection,address = server.accept()
    print('客户段连接成功')
    print(connection,address)

    with connection:
        print('connected by', address)
        while True:
            connection.sendall(msg.encode())
            data = connection.recv(1024)
            print(data)
            if msg == 'q':
                break



