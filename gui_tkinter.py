import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('hello word')
window.geometry('1100x500+500+50')
window.resizable(width=False, height=False)

menubar = tk.Menu(window)
window.config(menu=menubar)
menu1 = tk.Menu(menubar,tearoff=False)
# menu1.add_separator()
menu1.add_command(label='地址修改')
menubar.add_cascade(label='设置',menu=menu1)

frm = tk.Frame(window)
frm.grid(sticky='nw',row=0)

frm_l_1 =tk.Frame(frm)
label1 = tk.Label(frm_l_1,text='IP/端口:').grid(row=0,padx=10,pady=10,sticky='nw')
label2 = tk.Label(frm_l_1,text='10.245.0.2:8099').grid(row=0,column=1,padx=10,pady=10,sticky='nw')
frm_l_1.grid(sticky='nw')
frm_l_2 =tk.Frame(frm)
text = tk.Text(frm_l_2).grid(row=2,padx=10,pady=10)
button2 = tk.Button(frm_l_2,text='发送').grid(row=3,padx=10,pady=10)
frm_l_2.grid()


frm_r = tk.Frame(window)
frm_r.grid(sticky='ne',row=0,column=1)
tree = ttk.Treeview(frm_r,show="headings",height=23)
tree.grid(row=0,column=2,padx=10,pady=10)
tree['columns'] = ('line','host','port','status')
tree.column('line',width=100)
tree.column('host',width=200)
tree.column('port',width=100)
tree.column('status',width=100)
tree.heading('line',text='序号')
tree.heading('host',text='主机')
tree.heading('port',text='端口')
tree.heading('status',text='状态')

for i in range(100):
    tree.insert('',i,values=(i,i,i,i))




window.mainloop()