import socket
import configparser
import os
import tkinter as tk
from tkinter import ttk

class QunFa():
    def __init__(self):
        window = tk.Tk()
        window.title('局域网消息广播')
        window.geometry('1100x500+500+50')
        window.resizable(width=False, height=False)
        self.frm = tk.Frame(window)
        self.frm.grid(sticky='nw', row=0)
        self.frm_l_1 = tk.Frame(self.frm)
        self.label1 = tk.Label(self.frm_l_1, text='IP/端口:').grid(row=0, padx=10, pady=10, sticky='nw')
        self.label2 = tk.Label(self.frm_l_1, text=self.host()).grid(row=0, column=1, padx=10, pady=10, sticky='nw')
        # self.button1 = tk.Button(self.frm_l_1, text='开始', command=self.socket_start).grid(row=0, column=2, padx=10, pady=10)
        self.frm_l_1.grid(sticky='nw')
        self.frm_l_2 = tk.Frame(self.frm)
        self.text = tk.Text(self.frm_l_2)
        self.msg = self.text.get('0.0', 'end')
        self.text.grid(row=2, padx=10, pady=10)
        self.button2 = tk.Button(self.frm_l_2, text='发送', command=self.start_server ).grid(row=3, padx=10, pady=10)
        self.frm_l_2.grid()
        self.frm_r = tk.Frame(window)
        self.frm_r.grid(sticky='ne', row=0, column=1)
        self.tree = ttk.Treeview(self.frm_r, show="headings", height=23)
        self.tree.grid(row=0, column=2, padx=10, pady=10)
        self.tree['columns'] = ('line', 'host', 'port')
        self.tree.column('line', width=100)
        self.tree.column('host', width=200)
        self.tree.column('port', width=100)
        self.tree.heading('line', text='序号')
        self.tree.heading('host', text='主机')
        self.tree.heading('port', text='端口')
        # for i in address(1):
        #     self.tree.insert('', i, values=(i[0], i[1], i, i))
        window.mainloop()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.host())
        self.server.listen(1000)


    def host(self):
        config = configparser.ConfigParser()
        config.read(os.path.dirname(__file__) + '/config.ini')
        config.sections()
        host = (config.get('DEFAULT', 'host'), int(config.get('DEFAULT', 'port')))
        return host

    def start_server(self):
        connection, address =self.server.accept()
        connection.sendall(self.msg.encode())




if __name__ == '__main__':
    QunFa()