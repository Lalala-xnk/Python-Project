from tkinter import *

# window = Tk()
shift_update = 2 #create global variable shift update


from tkinter import messagebox #warming message
from encode_new import encode, decode


# window.title ("Group 9 Project: Password Manager")

#Each of these characters is represented in computer memory using a number called ASCII code which is an n 8-bit number
def encrypt (data, shift):
    encrypted = ""
    for i in range(len(data)):
        char = data[i]
        if(char.isupper()):#check if it's an uppercase character
            encrypted += chr((ord(char) + shift - 65) %26 + 65)  #shift the current character by key positions
        elif(char.islower()):#check if its a lowecase character
            encrypted += chr((ord(char) + shift - 97) %26 + 97) # lowercase characters’ representation begins with the number 97.
        elif(char.isdigit()): # if it's a number,shift its actual value
            number = (int(char) + shift )% 10#digit
            encrypted += str(number)
        else: # if its neither alphabetical nor a number, just leave it like that
            encrypted += char
    return encrypted

def decrypt (data, shift): #negative shift
    decrypted = ""
    for i in range(len(data)):
        char = data[i]
        if(char.isupper()):
            decrypted += chr((ord(char) - shift - 65) %26 + 65)
        elif(char.islower()):
            decrypted += chr((ord(char) - shift - 97) %26 + 97)
        elif(char.isdigit()):
            number = (int(char) - shift )% 10
            decrypted += str(number)
        else:
            decrypted += char
    return decrypted


def addScreen(tk):
    window = Toplevel(tk)
    window.title("Group 9 Project: Password Manager")

    window.geometry("450x450")
    # Label Frame
    lbl_website_Name = Label(window, text="Please enter the service name: ")
    lbl_website_Name.config(anchor=CENTER)
    lbl_website_Name.pack()

    # Create Entry Box To Designate service name
    txt_website_Name = Entry(window, width=20)
    txt_website_Name.pack()
    txt_website_Name.focus()

    lbl_user_Name = Label(window, text="Enter your username: ")
    lbl_user_Name.config(anchor=CENTER)
    lbl_user_Name.pack()

    # Create Entry Box To Designate username
    txt1_user_Name = Entry(window, width=20)
    txt1_user_Name.pack()
    txt1_user_Name.focus()


    lbl_FPassword = Label(window, text="Enter your Password :")
    lbl_FPassword.config(anchor=CENTER)
    lbl_FPassword.pack()

    # Create Entry Box To Designate Password
    txt_FPassword = Entry(window, width=20, show="*") # hide the input password
    txt_FPassword.pack()
    txt_FPassword.focus()


    label1_RPassword = Label(window, text="Re-enter Password :")
    label1_RPassword.pack()

    # Create Entry Box To Designate reentry Password
    txt_RPassword = Entry(window, width=20, show="*")
    txt_RPassword.pack()
    txt_RPassword.focus()

    def SavePassword():
        #check if customer input all the information
        if len(txt_website_Name.get()) != 0 and len(txt1_user_Name.get()) != 0 and len(txt_FPassword.get()) != 0 and len(txt_RPassword.get()) != 0 :

            #check whether password match
            if txt_FPassword.get() == txt_RPassword.get():

                print("Right password")
                print(txt_website_Name.get())

                file = open("securePasword.txt", "a")
                file.write(txt_website_Name.get() + ";|" + txt1_user_Name.get() + ";|" + encode(txt_FPassword.get()).decode('utf-8') + "\n")
                file.close()
                password_Save(window)

                window.geometry('550x450')
                window.resizable(height=None, width=None)

                #list out all the password stored in the txt file
                lbl = Label(window, text="service name \t  Username \t Password", fg='red', font=("Helvetica", 12))
                #lbl = Label(window, text="{}\t\t  {} \t\t {}".format("service", "Username", "Password"),font=("Helvetica", 12))
                lbl.grid(row=1, column=1, padx=80)
                count = 1
                file = open("securePasword.txt", "r")
                for i in file:
                    count +=1
                    data = i.split(";|")
                    # list out all the saved data
                    # print( decrypt(data[0], shift_update), "---", decrypt(data[1], shift_update), "---", decrypt(data[2], shift_update))
                    lbl = Label(window, text="{}\t\t  {} \t\t {}"
                                .format(decode(data[0]), decode(data[1]), decode(data[2])),
                                fg='black', font=("Helvetica", 12))
                    lbl.grid(row=int(count), column=1, padx=100)


            else:
                #move cursor back to the first line
                txt_website_Name.focus()

                # Clear Our Entry Box
                txt_website_Name.delete(0, 'end')
                txt1_user_Name.delete(0, 'end')
                txt_FPassword.delete(0, 'end')
                txt_RPassword.delete(0, 'end')
                messagebox.showerror("showerror", "Password do not match.")
                #label1_RPassword.config(text="Password do not match")
                print("Wrong password")
        else:
            messagebox.showerror("showerror", "Please fill in all the information.")
            print("please fill all information in the form")

    btn = Button(window, text="Save", command=SavePassword)
    btn.pack(pady=10)

def password_Save(window):
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("700x500")



# firstScreen()
# window.mainloop()
