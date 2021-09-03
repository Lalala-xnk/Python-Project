from tkinter import *
#window = Tk()
shift_update = 2 #create global variable shift update

#window.title ("Group 9 Project: Password Manager")

def encrypt (data, shift):
    encrypted = ""
    for i in range(len(data)):
        char = data[i]
        if(char.isupper()):
            encrypted += chr((ord(char) + shift - 65) %26 + 65)
        elif(char.islower()):
            encrypted += chr((ord(char) + shift - 97) %26 + 97)
        elif(char.isdigit()):
            number = (int(char) + shift )% 10
            encrypted += str(number)
        else:
            encrypted += char
    return encrypted

def decrypt (data, shift):
    decrypted = ""
    for i in range(len(data)):
        char = data[i]
        if(char.isupper()):
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        elif(char.islower()):
            decrypted += chr((ord(char) - shift - 97) % 26 + 97)
        elif(char.isdigit()):
            number = (int(char) - shift )% 10
            decrypted += str(number)
        else:
            decrypted += char
    return decrypted


def addScreen(tk):
    window = Toplevel(tk)
    shift_update = 2  # create global variable shift update

    window.title("Group 9 Project: Password Manager")
    window.geometry("450x450")
    lbl_website_Name = Label(window, text="Please enter the service name: ")
    lbl_website_Name.config(anchor=CENTER)
    lbl_website_Name.pack()

    txt_website_Name = Entry(window, width=20)
    txt_website_Name.pack()
    txt_website_Name.focus()

    lbl_user_Name = Label(window, text="Enter your username: ")
    lbl_user_Name.config(anchor=CENTER)
    lbl_user_Name.pack()

    txt1_user_Name = Entry(window, width=20)
    txt1_user_Name.pack()
    txt1_user_Name.focus()

    lbl_FPassword = Label(window, text="Enter your Password :")
    lbl_FPassword.config(anchor=CENTER)
    lbl_FPassword.pack()

    # txt_FPassword = Entry(window, width=20)
    txt_FPassword = Entry(window, width=20, show="*") # hide the input password
    txt_FPassword.pack()
    txt_FPassword.focus()

    label1_RPassword = Label(window, text="Re-enter Password")
    label1_RPassword.pack()

    txt_RPassword = Entry(window, width=20, show="*")
    txt_RPassword.pack()
    txt_RPassword.focus()

    def SavePassword(window):
        if txt_FPassword.get() == txt_RPassword.get():

            print("Right password")
            print(txt_website_Name.get())

            file = open("securePasword.txt", "a")
            file.write(encrypt(txt_website_Name.get(), shift_update) + ";|" + encrypt(txt1_user_Name.get(), shift_update) + ";|" + encrypt(txt_FPassword.get(),shift_update) + "\n")
            file.close()
            password_Save(window)

            window.geometry('750x550')
            window.resizable(height=None, width=None)
            lbl = Label(window, text="Password Manager", fg='red', font=("Helvetica", 12))
            lbl.grid(column=1)
            lbl = Label(window, text="service name", fg='red', font=("Helvetica", 12))
            lbl.grid(row=2, column=0, padx=80)
            lbl = Label(window, text="Username", fg='red', font=("Helvetica", 12))
            lbl.grid(row=2, column=1, padx=80)
            lbl = Label(window, text="Password", fg='red', font=("Helvetica", 12))
            lbl.grid(row=2, column=2, padx=80)

            file = open("securePasword.txt", "r")
            for i in file:
                data = i.split(";|")
                print( decrypt(data[0], shift_update), "---", decrypt(data[1], shift_update), "---", decrypt(data[2], shift_update))
        else:
            label1_RPassword.config(text="Password do not match")
            print("Wrong password")

    btn = Button(window, text="Save", command=lambda:SavePassword(window))
    btn.pack(pady=10)

def password_Save(window):
    for widget in window.winfo_children():
            widget.destroy()
    window.geometry("700x500")


# if __name__ == '__main__':
#     window = Tk()
#     addScreen(window)
#     window.mainloop()
