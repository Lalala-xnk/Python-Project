# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

from add_func import decrypt, encrypt
from encode_new import encode, decode

LARGE_FONT = ("Verdana", 13)
BUTTON_FONT = ("Batang", 13, "bold")


# Deletion class def
class Deletion(Toplevel):
    def __init__(self, *args):
        Toplevel.__init__(self, *args)
        self.title('Delete Entry')
        self.frame = GetFrame(self, bd=3)
        self.frame.pack()


# func to traverse saved service names
def get_service(path):
    service_list = []

    # return none if file doesn't exist
    try:
        data = open(path, 'r').read()
    except IOError:
        return None

    # return none if file's empty
    if not data:
        return None

    # read entries
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
        # get all service names
        self.service_list = get_service('securePasword.txt')

        # check empty entries
        if self.service_list:
            self.lbl_service = Label(self, text='Please enter the service you want to delete: ')
            self.lbl_service.config(anchor=CENTER)
            self.lbl_service.pack()

            self.entry_service = Entry(self, width=20)
            self.entry_service.pack()
            self.entry_service.focus()

            self.del_bt = Button(self, text='Delete', command=self.del_entry)
            self.del_bt.pack(pady=10)
        else:
            # show err msg when empty
            err_msg = 'No password stored'
            label = Label(self, text=err_msg, font=LARGE_FONT, bd=3, width=30)
            label.pack(side='top', fill='x', pady=10)
            ret_bt = Button(self, text='OK', command=self.master.destroy)
            ret_bt.pack(pady=10)

    def del_entry(self, *args):
        # get input service name
        service = self.entry_service.get()
        # flag to identify result
        # 0 for success
        # 1 for no input
        # 2 for no entry
        flag = 0
        if service:
            if service in self.service_list:
                with open('securePasword.txt', 'r+') as fl:
                    lines = fl.readlines()
                    fl.seek(0)
                    for txt in lines:
                        if txt.split(';|')[0] != service:
                            fl.write(txt)
                    fl.truncate()
            else:
                flag = 2
        else:
            flag = 1

        # gen msg according to flag
        if flag == 0:
            msg = 'Service ' + service + ' deleted'
        elif flag == 1:
            msg = 'Please enter service name'
        else:
            msg = 'Service ' + service + ' does not exist'
        # clear frame
        self.entry_service.destroy()
        self.lbl_service.destroy()
        self.del_bt.destroy()
        # show msg
        label = Label(self, text=msg, font=LARGE_FONT, bd=3, width=30)
        label.pack(side='top', fill='x', pady=10)
        ret_bt = Button(self, text='OK', command=self.master.destroy)
        ret_bt.pack(pady=10)
