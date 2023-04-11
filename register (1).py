from tkinter import *
import tkinter as tk
import os
import sys
from PIL import Image,ImageTk
import mysql.connector
my=mysql.connector.connect(host='localhost',user='root',database='project',password='password')
cursor=my.cursor()
if my.is_connected():
    print('Database connected')
def f():
    import gui
    delete_login()
    delete_login_success()
    delete_main()
##    manage.manage()
    

# Designing window for registration
def register():
     f()
##    global register_screen
##    register_screen = Toplevel(main_screen)
##    register_screen.title("Register")
##    register_screen.geometry("300x250")
## 
##    global username
##    global password
##    global username_entry
##    global password_entry
##    global canvas2
##    username = StringVar()
##    password = StringVar()
##    # Read the Image
##    image = Image.open("download.jpg")
##      
##    # Reszie the image using resize() method
##    resize_image = image.resize((300, 250))
##    img = ImageTk.PhotoImage(resize_image)
##    
##    # Create Canvas
##    canvas2= tk.Canvas(register_screen, width = 400,height = 400)
##      
##    canvas2.pack(fill = "both", expand = True)
##      
##    # Display image
##    canvas2.create_image( 0, 0, image = img, anchor = "nw")
##    
##    # Add Text
##    canvas2.create_text(150,25, text = "Please enter details below",font=("david",12))
##    canvas2.create_text(120,58, text="Username * ",font=("david", 12))
##    canvas2.create_text(120,112, text="Password * ",font=("david", 12))
##    #entry box
##    username_entry = tk.Entry(register_screen,textvariable=username)
##    canvas2.create_window(140,80, window=username_entry)
##    password_entry = tk.Entry(register_screen,textvariable=password, show='*')
##    canvas2.create_window(140,130, window=password_entry)
##    #add buttons
##    button1=Button(register_screen,text="Register", height="1", width="10",command = register_user,font=("david", 10))
##    button2=Button(register_screen,text="Done", height="1", width="10",command=delete_register and login,font=("david", 10))
##    # Display Buttons
##    button1_canvas = canvas2.create_window( 96, 160,anchor = "nw",window = button1)
##    button2_canvas = canvas2.create_window( 96, 210,anchor = "nw",window = button2)
##    register_screen.mainloop()
## 
##    Label(register_screen, text="Please enter details below", bg="light blue").pack()
##    Label(register_screen, text="").pack()
##    username_lable = Label(register_screen, text="Username * ")
##    username_lable.pack()
##    username_entry = Entry(register_screen, textvariable=username)
##    username_entry.pack()
##    password_lable = Label(register_screen, text="Password * ")
##    password_lable.pack()
##    password_entry = Entry(register_screen, textvariable=password, show='*')
##    password_entry.pack()
##    Label(register_screen, text="").pack()
##    Button(register_screen, text="Register", width=10, height=1, bg="light blue", command = register_user).pack()
##    Button(register_screen, text="Done", width=10, height=1, bg="light blue", command = delete_register).pack()
# Designing window for login 
 
def login():
    global canvas3
    global login_screen
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")


    # Read the Image
    image = Image.open("download.jpg")
      
    # Reszie the image using resize() method
    resize_image = image.resize((300, 250))
    img = ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas3= tk.Canvas(login_screen, width = 400,height = 400)
      
    canvas3.pack(fill = "both", expand = True)
      
    # Display image
    canvas3.create_image( 0, 0, image = img, anchor = "nw")
    
    # Add Text
    canvas3.create_text(150,25, text = "Please enter details below to login",font=("david",12))
    canvas3.create_text(120,58, text="Username * ",font=("david", 12))
    canvas3.create_text(120,112, text="Password * ",font=("david", 12))
    #entry box
    username_login_entry = tk.Entry(login_screen,textvariable=username_verify)
    canvas3.create_window(140,80, window=username_login_entry)
    password_login_entry= tk.Entry(login_screen,textvariable=password_verify, show='*')
    canvas3.create_window(140,130, window=password_login_entry)
    #add buttons
    button1=Button(login_screen,text="Login", height="1", width="10",command = login_verify,font=("david", 10))
    # Display Buttons
    button1_canvas = canvas3.create_window(96, 170,anchor = "nw",window = button1)
    login_screen.mainloop()

##    Label(login_screen, text="Please enter details below to login").pack()
##    Label(login_screen, text="").pack()

##    Label(login_screen, text="Username * ").pack()
##    username_login_entry = Entry(login_screen,textvariable=username_verify)
##    username_login_entry.pack()
##    Label(login_screen, text="").pack()
##    Label(login_screen, text="Password * ").pack()
##    password_login_entry = Entry(login_screen,textvariable=password_verify, show= '*')
##    password_login_entry.pack()
##    Label(login_screen, text="").pack()
##    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
d={}
def register_user():

    username_info = username.get()
    password_info = password.get()
    #The method listdir() returns a list containing the names of the entries in the directory given by path.
    list_of_files = os.listdir()  
 
##    #defining verification's conditions 
##   if username_info in list_of_files:
    file=open(username_info, "w") 
##        verify=file1.read().splitlines()
##        username_used()
    data=cursor.fetchone()
##    while data != None:
    print(data)
    if username==data:
        username_used()
    else:
##        file = open(username_info, "w")
##        file.write(username_info + "\n")
##        file.write(password_info)
        key=username_info
        value=password_info   
        ##    username_entry.delete(0, END)
        ##    password_entry.delete(0, END)
        canvas2.create_text(150,198, text = "Registration Success!Now click on done.",font=("calibri", 12))
        SQL='INSERT INTO userinfo VALUES("{}","{}");'.format(key,value)
        cursor.execute(SQL)
        my.commit()
        print('uploaded')
    file.close()
    
def username_used():
    global username_used_screen
    username_used_screen = Toplevel(register_screen)
    username_used_screen.title("Error")
    username_used_screen.geometry("150x100")
    Label(username_used_screen, text="Username unavailable",fg="red").pack()
    Button(username_used_screen, text="Try another", command=delete_username_used).pack()
# Implementing event on login button    
def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
##    username_login_entry.delete(0, END)
##    password_login_entry.delete(0, END)
## 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=f).pack()
    #and link to manage screen
    #//////////////
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password",fg="red").pack()
    Button(password_not_recog_screen, text="Try Again", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found",fg="red").pack()
    Button(user_not_found_screen, text="Try Again", command=delete_user_not_found_screen).pack()
    Button(user_not_found_screen, text="Register ", command=register).pack()
 
# Deleting popups
def delete_username_used():
    username_used_screen.destroy()
 
def delete_login_success():
    login_success_screen.destroy()

def delete_login():
    login_screen.destroy()

def delete_register():
    register_screen.destroy()
    
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_main():
    main_account_screen_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("2000x1500")
    # Read the Image
    image = Image.open("download.jpg")
      
    # Reszie the image using resize() method
    resize_image = image.resize((2100, 1600))
    img=ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas1 = Canvas(main_screen, width = 400,height = 400)
      
    canvas1.pack(fill = "both", expand = True)
      
    # Display image
    canvas1.create_image( 0, 0, image=img, anchor = "nw")
    
    # Add Text
    canvas1.create_text(740,150, text = "Welcome to Codeleza",font=("david", 35),fill='purple')
    canvas1.create_text(750,365, text = "New here? Register now!",font=("david", 20))

    #add buttons
    button1=Button(main_screen,text="Login", height="3", width="30",command = login,font=("david", 20),fg="green",bg='light grey')
    button2=Button(main_screen,text="Register", height="3", width="30",command=f,font=("david", 20),fg="green",bg='light grey')
    # Display Buttons
    button1_canvas = canvas1.create_window( 500, 200, anchor = "nw",window = button1)
    button2_canvas = canvas1.create_window( 500, 400,anchor = "nw",window = button2)
    main_screen.mainloop()
main_account_screen()
print(d)
 
