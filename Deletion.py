# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

from add_func import decrypt, encrypt
from encode_new import encode, decode

LARGE_FONT = ("Verdana", 13)
BUTTON_FONT = ("Batang", 13, "bold")

shift_update = 2


class Deletion(Toplevel):
    def __init__(self, *args):
        Toplevel.__init__(self, *args)
        self.title('Delete Entry')
        self.frame = GetFrame(self, bd=3)
        self.frame.pack()


def get_service(path):
    service_list = []

    try:
        data = open(path, 'r').read()
    except IOError:
        return None

    if not data:
        return None

    data_list = data.split('\n')
    for item in data_list:
        if item:
            tmp = item.split(';|')
            service_list.append(tmp[0])
    return service_list


class GetFrame(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.del_func()

    def del_func(self):
        self.service_list = get_service('securePasword.txt')

        if self.service_list:
            self.lbl_service = Label(self, text='Please enter the service you want to delete: ')
            self.lbl_service.config(anchor=CENTER)
            self.lbl_service.pack()

            self.entry_service = Entry(self, width=20)
            self.entry_service.pack()
            self.entry_service.focus()

            self.del_bt = ttk.Button(self, text='Delete', command=self.del_entry)
            self.del_bt.pack(pady=10)
        else:
            err_msg = 'No password stored'
            label = Label(self, text=err_msg, font=LARGE_FONT, bd=3, width=30)
            label.pack(side='top', fill='x', pady=10)
            ret_bt = ttk.Button(self, text='OK', command=self.master.destroy)
            ret_bt.pack(pady=10)

    def del_entry(self, *args):
        service = self.entry_service.get()
        flag = 0
        if service:
            if service in self.service_list:
                with open('securePasword.txt', 'r+') as fl:
                    lines = fl.readlines()
                    fl.seek(0)
                    for txt in lines:
                        if txt[:len(service)] != service:
                            fl.write(txt)
                    fl.truncate()
            else:
                flag = 2
        else:
            flag = 1

        if flag == 0:
            msg = 'Service ' + service + ' deleted'
        elif flag == 1:
            msg = 'Please enter service name'
        else:
            msg = 'Service ' + service + ' does not exist'
        self.entry_service.destroy()
        self.lbl_service.destroy()
        self.del_bt.destroy()
        label = Label(self, text=msg, font=LARGE_FONT, bd=3, width=30)
        label.pack(side='top', fill='x', pady=10)
        ret_bt = ttk.Button(self, text='OK', command=self.master.destroy)
        ret_bt.pack(pady=10)
