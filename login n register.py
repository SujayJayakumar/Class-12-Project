from tkinter import *
import tkinter as tk
import os
import sys
from PIL import Image,ImageTk
import mysql.connector
mycon=mysql.connector.connect(host='localhost',
                              user='root',
                              database='project',
                              password='password')
if mycon.is_connected():
    print('Database connected')

def f():
    import gui
    delete_login()
    delete_login_success()
    delete_main()
    
'''root=Tk()
root.title('database gui')
root.geometry('400x400')'''

#cursor=mycon.cursor()


#creating customer table
#sql='''CREATE TABLE customer
#       (customer_id char(4) PRIMARY KEY,    
#        first_name varchar(100),
#        last_name varCHAR(100),
#        date_of_purchase DATE,
#        contact_number INT(10),
#        address varCHAR(200),
#        city varCHAR(100),
#        state varCHAR(100),
#        zipcode INT(6)
#        gender varchar(6));'''
#cursor.execute(sql)'''
#mycon.commit()
#mycon.close()



#creating submit funtion
def submit():
    customer_id=customer_id.get()
    f_name=f_name.get()
    l_name=f_name.get()
    date_of_purchase=date_of_purchase.get()
    contact_number=contact_number.get()
    address=address.get()
    city=city.get()
    state=state.get()
    zipcode=zipcode.get()
    gender=gender.get()
    mycon=mysql.connector.connect(host='localhost',
                              user='root',
                              database='project',
                              password='password')
    cursor=mycon.cursor()
    #insert into table
    sql=('''INsert TABLE customer values
       (customer_id ,    
        first_name,
        last_name,
        date_of_purchase,
        contact_number,
        address,
        city ,
        state,
        zipcode,
        gender);''')
    cursor.execute(sql)
                   
                



                       
                       
    
    mycon.commit()
    mycon.close()
    


    
    #clear text boxes already
    customer_id.delete(0,END)
    f_name.delete(0,END)
    l_name.delete(0,END)
    date_of_purchase.delete(0,END)
    contact_number.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    gender.delete(0,END)


    
'''#creating text boxes
customer_id=Entry(width=30)
customer_id.grid(row=0,column=1,padx=20)

f_name=Entry(width=30)
f_name.grid(row=1,column=1)

l_name=Entry(width=30)
l_name.grid(row=2,column=1)

date_of_purchase=Entry(width=30)
date_of_purchase.grid(row=3,column=1)

contact_number=Entry(width=30)
contact_number.grid(row=4,column=1)

address=Entry(width=30)
address.grid(row=5,column=1)

city=Entry(width=30)
city.grid(row=6,column=1)

state=Entry(width=30)
state.grid(row=7,column=1)

zipcode=Entry(width=30)
zipcode.grid(row=8,column=1)

gender=Entry(width=30)
gender.grid(row=9,column=1)

#creating text box labels
customer_id_label=Label(text='CID')
customer_id_label.grid(row=0,column=0)

f_name_label=Label(text='First name')
f_name_label.grid(row=1,column=0)

l_name_label=Label(text='last name')
l_name_label.grid(row=2,column=0)

date_of_purchase_label=Label(text='date of purchase')
date_of_purchase_label.grid(row=3,column=0)

contact_number_label=Label(text='contact number')
contact_number_label.grid(row=4,column=0)

address_label=Label(text='address')
address_label.grid(row=5,column=0)

city_label=Label(text='city')
city_label.grid(row=6,column=0)

state_label=Label(text='state')
state_label.grid(row=7,column=0)

zipcode_label=Label(text='zipcode')
zipcode_label.grid(row=8,column=0)

gender_label=Label(text='Gender(M/F)')
gender_label.grid(row=9,column=0)'''

#creating submit button
submit_btn=Button(text='Add record to database',command=submit)
submit_btn.grid(row=20,column=0,columnspan=2,pady=10,ipadx=100)


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
 

