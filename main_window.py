from tkinter import *
import tkinter as tk
import os
import sys
from PIL import Image,ImageTk
import csv

import mysql.connector
my=mysql.connector.connect(host='localhost',user='root',database='project',password='')
cursor=my.cursor()
if my.is_connected():
    print('Database connected')



cid=open('current_user.txt')
currentID=cid.read()
cid.close()

#DELETE    

def delete():
    global root1
    root1=Tk()
    root1.title('delete')
    root1.geometry('270x80')

    customer_id_label=Label(root1, text='Are you sure you want to delete your account?')
    customer_id_label.grid(row=0,column=0)

    delete_btn=Button(root1,text='Yes',command=delete1)
    delete_btn.grid(row=20,column=0,columnspan=2,pady=10,ipadx=100)


def delete1():
    cursor.execute("delete from customer where customer_id='"+ currentID +"'")
    my.commit()
    root1.destroy()
    main_screen.destroy()


cursor.execute("select * from customer where customer_id='"+ currentID +"'")
while True:
    data=cursor.fetchone()
    if data==None:
        break
    else:
        print(data)
        r=list(data)
print(r)
#VIEW
def view():
    global root2
    root2=Tk()
    root2.title('View your Info')
    root2.geometry('400x400')

    cursor.execute("select * from customer where customer_id='"+ currentID +"'")
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            print(data)
            r=list(data)

    

    customer_id1_label=Label(root2, text=r[0])
    customer_id1_label.grid(row=0,column=1)

    f_name1_label=Label(root2, text=r[3])
    f_name1_label.grid(row=1,column=1)

    l_name1_label=Label(root2, text=r[4])
    l_name1_label.grid(row=2,column=1)

    date_of_birth1_label=Label(root2, text=r[5])
    date_of_birth1_label.grid(row=3,column=1)

    contact_number1_label=Label(root2, text=r[6])
    contact_number1_label.grid(row=4,column=1)

    address1_label=Label(root2, text=r[7])
    address1_label.grid(row=5,column=1)

    city1_label=Label(root2, text=r[8])
    city1_label.grid(row=6,column=1)

    state1_label=Label(root2, text=r[9])
    state1_label.grid(row=7,column=1)

    zipcode1_label=Label(root2, text=r[10])
    zipcode1_label.grid(row=8,column=1)

    gender1_label=Label(root2, text=r[11])
    gender1_label.grid(row=9,column=1)


    username1_label=Label(root2, text=r[1])
    username1_label.grid(row=11,column=1)

    password1_label=Label(root2, text=r[2])
    password1_label.grid(row=12,column=1)





    customer_id_label=Label(root2, text='CID')
    customer_id_label.grid(row=0,column=0)

    f_name_label=Label(root2, text='First name')
    f_name_label.grid(row=1,column=0)

    l_name_label=Label(root2, text='last name')
    l_name_label.grid(row=2,column=0)

    date_of_birth_label=Label(root2, text='date of birth')
    date_of_birth_label.grid(row=3,column=0)

    contact_number_label=Label(root2, text='contact number')
    contact_number_label.grid(row=4,column=0)

    address_label=Label(root2, text='address')
    address_label.grid(row=5,column=0)

    city_label=Label(root2, text='city')
    city_label.grid(row=6,column=0)

    state_label=Label(root2, text='state')
    state_label.grid(row=7,column=0)

    zipcode_label=Label(root2, text='zipcode')
    zipcode_label.grid(row=8,column=0)

    gender_label=Label(root2, text='Gender')
    gender_label.grid(row=9,column=0)


    username_label=Label(root2, text='Username')
    username_label.grid(row=11,column=0)

    password_label=Label(root2, text='Password')
    password_label.grid(row=12,column=0)

    close_btn=Button(root2,text='Close',command=delete2)
    close_btn.grid(row=20,column=0,columnspan=2,pady=10,ipadx=100)
    
def delete2():
    root2.destroy()

#UPDATE    
def update():
    global root3
    root3=Tk()
    root3.title('Review and Update profile')
    root3.geometry('400x400')


    #creating text boxes
    
    global box_customer_id
    global box_f_name
    global box_l_name
    global box_date_of_birth
    global box_contact_number
    global box_address
    global box_city
    global box_state
    global box_zipcode
    global box_gender
    global box_username
    global box_password

    
    box_customer_id=Label(root3, text=r[0])
    box_customer_id.grid(row=0,column=1,padx=20)
##    box_customer_id.insert('end', 'Cannot be changed, contact admin')
##    customer_id_label=Label(root3, text='CID')
##    customer_id_label.grid(row=0,column=0)

    
    box_f_name=Entry(root3, width=30)
    box_f_name.grid(row=1,column=1)
    box_f_name.insert('end', r[3])

    box_l_name=Entry(root3, width=30)
    box_l_name.grid(row=2,column=1)
    box_l_name.insert('end', r[4])

    box_date_of_birth=Entry(root3, width=30)
    box_date_of_birth.grid(row=3,column=1)
    box_date_of_birth.insert('end', r[5])

    box_contact_number=Entry(root3, width=30)
    box_contact_number.grid(row=4,column=1)
    box_contact_number.insert('end', r[6])

    box_address=Entry(root3, width=30)
    box_address.grid(row=5,column=1)
    box_address.insert('end', r[7])

    box_city=Entry(root3, width=30)
    box_city.grid(row=6,column=1)
    box_city.insert('end', r[8])

    box_state=Entry(root3, width=30)
    box_state.grid(row=7,column=1)
    box_state.insert('end', r[9])

    box_zipcode=Entry(root3, width=30)
    box_zipcode.grid(row=8,column=1)
    box_zipcode.insert('end', r[10])

    box_gender=Entry(root3,width=30)
    box_gender.grid(row=9,column=1)
    box_gender.insert('end', r[11])


    box_username=Entry(root3,width=30)
    box_username.grid(row=11,column=1)
    box_username.insert('end', r[1])

    box_password=Entry(root3,width=30)
    box_password.grid(row=12,column=1)
    box_password.insert('end', r[2])

    #creating text box labels
    customer_id_label=Label(root3, text='CID')
    customer_id_label.grid(row=0,column=0)

    f_name_label=Label(root3, text='First name')
    f_name_label.grid(row=1,column=0)

    l_name_label=Label(root3, text='last name')
    l_name_label.grid(row=2,column=0)

    date_of_birth_label=Label(root3, text='date of birth')
    date_of_birth_label.grid(row=3,column=0)

    contact_number_label=Label(root3, text='contact number')
    contact_number_label.grid(row=4,column=0)

    address_label=Label(root3, text='address')
    address_label.grid(row=5,column=0)

    city_label=Label(root3, text='city')
    city_label.grid(row=6,column=0)

    state_label=Label(root3, text='state')
    state_label.grid(row=7,column=0)

    zipcode_label=Label(root3, text='zipcode')
    zipcode_label.grid(row=8,column=0)

    gender_label=Label(root3, text='Gender')
    gender_label.grid(row=9,column=0)


    username_label=Label(root3, text='Username')
    username_label.grid(row=11,column=0)

    password_label=Label(root3, text='Password')
    password_label.grid(row=12,column=0)


    submit_btn=Button(root3,text='Update record in database',command=submit)
    submit_btn.grid(row=20,column=0,columnspan=2,pady=10,ipadx=100)

def submit():


    

    cursor.execute("delete from customer where customer_id='"+ currentID +"'")
    my.commit()
    customer_id=currentID
    f_name=box_f_name.get()
    l_name=box_l_name.get()
    date_of_birth=box_date_of_birth.get()
    contact_number=box_contact_number.get()
    address=box_address.get()
    city=box_city.get()
    state=box_state.get()
    zipcode=box_zipcode.get()
    gender=box_gender.get()
    username=box_username.get()
    password=box_password.get()
    
    #insert into table
    if(customer_id=='' or f_name=='' or username=='' or password==''):
        MessageBox.showinfo('Insert Status','All Fields are required')
    else:
        cursor.execute('''insert into customer values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'''.format(customer_id,username,password,f_name,l_name,date_of_birth,contact_number,address,city,state,zipcode,gender))
        my.commit()
    #clear text boxes already
    #box_customer_id.delete(0,END)
    box_f_name.delete(0,END)
    box_l_name.delete(0,END)
    box_date_of_birth.delete(0,END)
    box_contact_number.delete(0,END)
    box_address.delete(0,END)
    box_city.delete(0,END)
    box_state.delete(0,END)
    box_zipcode.delete(0,END)
    box_gender.delete(0,END)
    box_username.delete(0,END)
    box_password.delete(0,END)
    login_success_screen()
    
    '''except:
        global error_screen
        error_screen = Toplevel(main_screen)
        error_screen.title("Update Unsucessful")
        error_screen.geometry("150x100")
        Label(error_screen, text="Update failed, Try again").pack()
        Button(error_screen, text="OK", command=delete3).pack()

def delete3():
    error_screen.destroy()'''
def delete4():
    login_success_screen.destroy()
    root3.destroy()

def login_success_screen():
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title("Update status")
    login_success_screen.geometry("250x100")
    Label(login_success_screen, text="Update Success").pack()
    Button(login_success_screen, text="OK", command=delete4).pack()
    

   


#VIEW ITEM LIST
def viewlist():
    n=10
    root4=Tk()
    root4.title('ITEMS')
    root4.geometry('600x400')
    products=open('products.csv','r',newline='')
    csv_r=csv.reader(products)    
    for rec in csv_r:
        Title_label=Label(root4, text='The products are:    ', font=('times new roman', 30, 'bold'),fg='green',bg='yellow')
        Title_label.grid(row=0,column=5)
        heading1_label=Label(root4, text='         Item name                ', font=('times new roman', 24, 'bold'),fg='dark green',bg='light blue')
        heading1_label.grid(row=3,column=5)
        heading2_label=Label(root4, text='Price ', font=('times new roman', 24, 'bold'),fg='dark green',bg='light blue')
        heading2_label.grid(row=3,column=6)
        heading3_label=Label(root4, text='Quantity', font=('times new roman', 24, 'bold'),fg='dark green',bg='light blue')
        heading3_label.grid(row=3,column=7)
        
        product1_label=Label(root4, text=rec[0], font=('times new roman', 20),fg='dark blue')
        product1_label.grid(row=n,column=5)
        product2_label=Label(root4, text=rec[1], font=('times new roman', 20),fg='dark blue')
        product2_label.grid(row=n,column=6)
        product3_label=Label(root4, text=rec[2], font=('times new roman', 20),fg='dark blue')
        product3_label.grid(row=n,column=7)
        print(rec)
        n=n+1


#PLACE ORDER in
def place_order():
    import billing
    
    
        
        
    
#def calculator():
#    import calculator
    
    
    
            
    
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = tk.Toplevel()
    main_screen.geometry("2000x1500")
    # Read the Image
    image = Image.open("mainpic1.jpg")
      
    # Reszie the image using resize() method
    resize_image = image.resize((1585, 830))
    img=ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas1 = Canvas(main_screen, width = 400,height = 400)
      
    canvas1.pack(fill = "both", expand = True)
      
    # Display image
    canvas1.create_image( 0, 0, image=img, anchor = "nw")
    
    # Add Text
    canvas1.create_text(680,100, text = "Welcome to Your space",font=("david", 45),fill='cyan')
    #canvas1.create_text(750,365, text = "New here? Register now",font=("david", 20))

    #add buttons
    button1=Button(main_screen,text="Update profile", height="2", width="25",command = update,font=("david", 20),fg="green",bg='light grey')
    button2=Button(main_screen,text="Delete account", height="2", width="25",command=delete,font=("david", 20),fg="green",bg='light grey')
    button3=Button(main_screen,text="View UserInfo", height="2", width="25",command = view,font=("david", 20),fg="green",bg='light grey')
    button4=Button(main_screen,text="View Item list", height="2", width="25",command = viewlist,font=("david", 20),fg="green",bg='light grey')
    button5=Button(main_screen,text="Place order", height="2", width="25",command = place_order,font=("dasvid", 20),fg="green",bg='light grey')
#    button6=Button(main_screen,text="Calculator", height="1", width="15",command = calculator,font=("dasvid", 20),fg="green",bg='light grey')
    
    # Display Buttons
    button1_canvas = canvas1.create_window( 200, 200, anchor = "nw",window = button1)
    button2_canvas = canvas1.create_window( 200, 350,anchor = "nw",window = button2)
    button3_canvas = canvas1.create_window( 200, 500, anchor = "nw",window = button3)
    button4_canvas = canvas1.create_window( 800, 200, anchor = "nw",window = button4)
    button5_canvas = canvas1.create_window( 800, 350, anchor = "nw",window = button5)
#    button6_canvas = canvas1.create_window( 1000, 600, anchor = "nw",window = button6)
    main_screen.mainloop()
main_account_screen()
#print(d)


        
        
 
my.close()
