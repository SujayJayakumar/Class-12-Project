from tkinter import *
'''#Designing Main Screen So, first of all, you have to design the main screen.
#two buttons Login and Register.
def main_screen():
    mainscreen = Tk()   # create a GUI window 
    mainscreen.geometry("800x800") # set the configuration of GUI window 
    mainscreen.title(" Login Page") # set the title of GUI window
# create a Form label 
Label(text="Login / Register", bg="lightgreen", width="30", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 
# create Login Button 
Button(text="Login", height="2", width="30").pack() 
Label(text="").pack() 
# create a register button
Button(text="Register", height="2",width="30").pack()
 
mainscreen.mainloop() # start the GUI
main_screen() # call the main_account_screen() function'''


######## diff code for login page inside

from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Welcome to the Login Form ')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()
