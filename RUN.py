from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector
my=mysql.connector.connect(host='localhost',user='root',database='project',password='')
cursor=my.cursor()
if my.is_connected():
    print('Database connected')

def main():
    import main_window

def f():
    import gui_RegisterWindow

def admin():
    import admin_window



def login():
    global canvas3
    global login_screen
    global username_verify
    global password_verify
    global cid_verify
    username_verify = StringVar()
    password_verify = StringVar()
    cid_verify = StringVar()
   
 
    global username_login_entry
    global password_login_entry
    global cid_login_entry
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("330x260")


    # Read the Image
    image = Image.open("loginpic.jpg")
      
    # Reszie the image using resize() method
    resize_image = image.resize((330, 260))
    img = ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas3= tk.Canvas(login_screen, width = 400,height = 400)
      
    canvas3.pack(fill = "both", expand = True)
      
    # Display image
    canvas3.create_image( 0, 0, image = img, anchor = "nw")
    
    # Add Text
    canvas3.create_text(170,25, text = "Please enter details below to log into ur acc",font=("david",12),fill='white')
    canvas3.create_text(120,58, text="Username * ",font=("david", 12),fill='white')
    canvas3.create_text(120,112, text="Password * ",font=("david", 12),fill='white')
    canvas3.create_text(120,170, text="Customer ID * ",font=("david", 12),fill='white')
    #entry box
    username_login_entry = tk.Entry(login_screen,textvariable=username_verify)
    canvas3.create_window(140,80, window=username_login_entry)
    password_login_entry= tk.Entry(login_screen,textvariable=password_verify, show='*')
    canvas3.create_window(140,130, window=password_login_entry)
    cid_login_entry= tk.Entry(login_screen,textvariable=cid_verify)
    canvas3.create_window(140,190, window=cid_login_entry)
    #add buttons
    button1=Button(login_screen,text="Login", height="1", width="10",command = login_verify,font=("david", 10))
    # Display Buttons
    button1_canvas = canvas3.create_window(96, 210,anchor = "nw",window = button1)
    login_screen.mainloop()


def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    cid1 = cid_verify.get()
    sql='''SELECT * FROM customer;'''
    cursor.execute(sql)
    my.close()
    data=cursor.fetchall()
    #print(data)
    for i in data:
        #print(i)
        #print(i[0])
        if i[0]==cid1:
            if password1==i[2]:
                login_sucess()
                current_user=open('current_user.txt','w')
                current_user.write(cid1)
                current_user.close()
                
                break
            else:
                password_not_recognised()
                current_user=open('current_user.txt','w')
                current_user.close()
                break
        else:
            continue
    else:
        user_not_found()
                
                
            
            




# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=main).pack()
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
    Label(user_not_found_screen, text="Register yourself now!").pack()
 
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
    
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("2000x1500")
    # Read the Image
    image = Image.open("download.jpg")
      
    # Reszie the image using resize() method
    resize_image = image.resize((1590, 840))
    img=ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas1 = Canvas(main_screen, width = 400,height = 400, relief=SUNKEN, bd=15)
      
    canvas1.pack(fill = "both", expand = True)
      
    # Display image
    canvas1.create_image( 0, 0, image=img, anchor = "nw")
    
    # Add Text
    canvas1.create_text(700,110, text = "Welcome to Shopezee",font=("david", 45, 'bold'),fill='purple')
    canvas1.create_text(650,380, text = "New here? Register now!",font=("david", 20))

    #add buttons
    button1=Button(main_screen,text="Login", height="2", width="20",command = login,font=("david", 25, 'bold'),fg="lawn green",bg='blue',bd=5)
    button2=Button(main_screen,text="Register", height="2", width="20",command=f,font=("david", 25, 'bold'),fg="lawn green",bg='blue',bd=5)
    button3=Button(main_screen,text="ADMIN", height="1", width="10",command=admin,font=("david", 15),fg="white",bg='dark blue',relief=RIDGE,bd=2)
    # Display Buttons
    button1_canvas = canvas1.create_window( 450, 200, anchor = "nw",window = button1)
    button2_canvas = canvas1.create_window( 450,420,anchor = "nw",window = button2)
    button3_canvas = canvas1.create_window( 1200, 630,anchor = "nw",window = button3)
    main_screen.mainloop()
main_account_screen()

'''#===============================================================================    
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("2000x1500")
    # Read the Image
    image = Image.open("download.png")
      
    # Reszie the image using resize() method
    resize_image = image.resize((1585, 830))
    img=ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas1 = Canvas(main_screen, width = 400,height = 400)
      
    canvas1.pack(fill = "both", expand = True)
      
    # Display image
    canvas1.create_image( 0, 0, image=img, anchor = "nw")
    
    # Add Text
    canvas1.create_text(740,30, text = "Welcome to Your space",font=("david", 35),fill='cyan')
    #canvas1.create_text(750,365, text = "New here? Register now",font=("david", 20))

    #add buttons
    button1=Button(main_screen,text="Update profile", height="1", width="15",command = "",font=("david", 20),fg="green",bg='light grey')
    button2=Button(main_screen,text="Delete account", height="1", width="15",command="",font=("david", 20),fg="green",bg='light grey')
    button3=Button(main_screen,text="View UserInfo", height="1", width="15",command = "",font=("david", 20),fg="green",bg='light grey')
    button4=Button(main_screen,text="View Item list", height="1", width="15",command = "",font=("david", 20),fg="green",bg='light grey')
    button5=Button(main_screen,text="Place order", height="1", width="15",command = "",font=("david", 20),fg="green",bg='light grey')
    
    # Display Buttons
    button1_canvas = canvas1.create_window( 300, 100, anchor = "nw",window = button1)
    button2_canvas = canvas1.create_window( 300, 200,anchor = "nw",window = button2)
    button3_canvas = canvas1.create_window( 300, 300, anchor = "nw",window = button3)
    button4_canvas = canvas1.create_window( 300, 400, anchor = "nw",window = button4)
    button5_canvas = canvas1.create_window( 300, 450, anchor = "nw",window = button4)
    main_screen.mainloop()
main_account_screen()'''
