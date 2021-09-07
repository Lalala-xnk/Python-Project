from tkinter import *

from add_func import *
from ListNew import *
from Deletion import *


LARGE_FONT = ("Verdana", 13)
BUTTON_FONT = ("Batang", 13, "bold")
shift_update = 2
RIGHT_PASSWORD = False


class Login(Tk):
    """docstring for Login"""

    def __init__(self, *args):
        Tk.__init__(self, *args)

        Tk.wm_title(self, "Password Manager")
        self.state = {
            "text": "Login to access password database.", "valid_user": False
        }

        self.addLoginFrame()

        # Adding frames

    def addLoginFrame(self, *kwargs):
        login = Frame(self, padx=2, pady=2, bd=2)
        login.pack()

        #loginLabel = Label(login, text=self.state['text'],bd=10, width=30)
        pswdFile = open("login_pwd.txt", "r+")
        password = pswdFile.read()

        if password == '':
            loginLabel = Label(login, text="Please setup your password", bd=10, font=LARGE_FONT, width=30)
        else:
            loginLabel = Label(login, text="Please input your password", bd=10, font=LARGE_FONT, width=30)
        loginLabel.grid(row=0, columnspan=3)
        pswdFile.close()
        entry = Entry(login, show="*")
        entry.config(cursor='pencil', bd=10, relief=GROOVE,)
        entry.grid(row=1, columnspan = 3, pady=3)
        # _ marks an unused variable; used for lambda compatibility
        # Bind event for when enter is pressed in the Entry
        entry.bind('<Return>', lambda _: self.checkPwd(
            login, label=loginLabel, entry=entry, btn=submitBtn))
        entry.focus_set()

        submitBtn = Button(login, text="Submit",
                               command=lambda: self.checkPwd(
                                   login, label=loginLabel, entry=entry,
                                   btn=submitBtn))
        submitBtn.config(bd=10, relief=RAISED)
        submitBtn.grid(row=3, column=1)



    """Kwargs = loginLabel, password entry, and submit button"""

    def checkPwd(self, frame, **kwargs):
        chk = kwargs['entry'].get()
        # if passwords match
        #we save the login password in the login_pwd.txt
        pswdFile = open("login_pwd.txt", "r+")
        password = pswdFile.read()
        # print("line 62 :input_psd = {} pasword={}".format(chk, password))
        #if there isn't password in login_pwd.txt,we should save the input password as the register password in the file
        if len(password) == 0:
            print("line 65input_psd = {} pasword={}".format(chk,decrypt(password,shift_update)))
            pswdFile.write(encrypt(chk, shift_update) if len(chk) > 0 else encrypt('\n', shift_update))
            RIGHT_PASSWORD = True
            self.state['text'] = "Logged In"
            self.state['valid_user'] = True
            # Using .config() to modift the args
            kwargs['label'].config(text=self.state['text'])
            kwargs['entry'].config(state=DISABLED)
            kwargs['btn'].config(state=DISABLED)
            # adding buttons
            self.addConfigBtn(frame)
            messagebox.showinfo('showinfo', 'New password set!')
            # self.destroy()

            # self.addlistBtn(frame)
            # msg = 'New password set'
            # label = Label(self, text=msg, font=LARGE_FONT, bd=3, width=30)
            # label.pack(side='top', fill='x', pady=10)
            # ret_bt = Button(self, text='OK', command=self.master.destroy)
            # ret_bt.pack(pady=10)


        elif chk == decrypt(password, shift_update) or (not chk and decrypt(password, shift_update) == '\n'):
            RIGHT_PASSWORD = True
            print("line 78 :pasword={}".format(decrypt(password, shift_update)))
            self.state['text'] = "Logged In"
            self.state['valid_user'] = True
            # Using .config() to modift the args
            kwargs['label'].config(text=self.state['text'])
            kwargs['entry'].config(state=DISABLED)
            kwargs['btn'].config(state=DISABLED)

            # adding buttons
            self.addConfigBtn(frame)
            #self.addlistBtn(frame)

        # If passwords don't match
        else:
            errorTk = Toplevel(self)
            errorTk.wm_title("Error Message")
            errorMsg = Message(errorTk, text="Password don't match!!\nTry Again!!!")
            errorMsg.config(bd=10, fg='red',font=('Verdana',12, 'italic'),width=200)
            errorMsg.pack(fill= X, expand=YES)
            kwargs['entry'].delete(0, 'end')
        pswdFile.close()



    def addConfigBtn(self, login):
        # configured buttons
        # btnList = (addBtn, listBtn, getBtn)

        # Creating temp references to images using temp1,2 so as to disallow
        # garbage collection problems
        btnList = ["Add", "List", 'Delete']
        btnCmdList = [lambda: addScreen(self),
                      lambda: List(self),
                      lambda: Deletion(self)]
        f = []  # Frames array
        img = []  # image array
        self.temp = []  # temp array


        for i in range(3):
            f.append(Frame(login, padx=60, width=200, height=100))
            f[i].grid(row=3, column=i)
            img.append(PhotoImage(
                file=btnList[i] + ".gif", width=70, height=70))
            self.temp.append(img[i])
            Button(f[i], image=img[i], text=btnList[i],
                   command=btnCmdList[i]).grid(row=3)


if __name__ == '__main__':
    new = Login()
    new.mainloop()
