# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

import pyperclip
from add_func import decrypt
from encode_new import encode, decode

LARGE_FONT = ("Verdana", 13)
BUTTON_FONT = ("Batang", 13, "bold")
PWD = {}

shift_update = 2


class List(Toplevel):
    def __init__(self, *args):
        Toplevel.__init__(self, *args)
        self.title('Password List')
        self.frame = GetFrame(self, bd=3)
        self.frame.pack()


class GetFrame(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.display()
        # self.tree = ttk.Treeview()

    def display(self):
        pwd_list = self.get_list()
        headings = ['Service', 'Username']

        if pwd_list:
            self.tree = ttk.Treeview(self, columns=headings, show='headings')

            Label(self, text='Double click to copy password', bd=2, font=LARGE_FONT).pack(side='top')
            scrollbar = ttk.Scrollbar(self, orient=VERTICAL, takefocus=True)
            scrollbar.config(command=self.tree.yview())
            self.tree.configure(yscroll=scrollbar.set(0, 1))
            scrollbar.pack(side=RIGHT, fill=Y)
            self.tree.pack(side=LEFT, fill=BOTH, expand=1)

            for item in headings:
                self.tree.heading(item, text=item)
                self.tree.column(item, width=200)

            for item in pwd_list:
                self.tree.insert('', END, values=item)

            self.tree.bind('<Double-1>', self.copy_pwd)
        else:
            err_msg = 'No password stored'
            label = Label(self, text=err_msg, font=LARGE_FONT, bd=3, width=30)
            label.pack(side='top', fill='x', pady=10)
            ret_bt = ttk.Button(self, text='OK', command=self.master.destroy)
            ret_bt.pack(pady=10)

    def get_list(self, *args):
        # PWD = {}
        path = 'securePasword.txt'
        pwd_list = []

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
                pwd_list.append((tmp[0], tmp[1]))
                PWD[tmp[0]] = tmp[2]
        return pwd_list

    def copy_pwd(self, *args):
        pyperclip.copy(decode(PWD[self.tree.item(self.tree.focus(), 'values')[0]]))
