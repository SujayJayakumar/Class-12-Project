import mysql.connector
from tkinter import *
import tkinter.messagebox as MessageBox
import tkinter as tk
mycon=mysql.connector.connect(host='localhost',
                              user='root',
                              database='project',
                              password='')
if mycon.is_connected():
    print('Database connected')
cursor=mycon.cursor()

root=Tk()
root.title('Register')
root.geometry('500x400')

#cursor=mycon.cursor()


#creating customer table
#sql='''CREATE TABLE customer
#       (customer_id char(4) PRIMARY KEY,
#        username varchar(50),
#        password varchar(30),
#        first_name varchar(100),
#        last_name varCHAR(100),
#        date_of_birth DATE,
#        contact_number varchar(10),
#        address varCHAR(200),
#        city varCHAR(100),
#        state varCHAR(100),
#        zipcode INT(6),
#        gender varchar(6));'''
#cursor.execute(sql)'''
#mycon.commit()
#mycon.close()




    
#creating text boxes
box_customer_id=Entry(root, width=30)
box_customer_id.grid(row=0,column=1,padx=20)

box_f_name=Entry(root, width=30)
box_f_name.grid(row=1,column=1)

box_l_name=Entry(root, width=30)
box_l_name.grid(row=2,column=1)

box_date_of_birth=Entry(root, width=30)
box_date_of_birth.grid(row=3,column=1)

box_contact_number=Entry(root, width=30)
box_contact_number.grid(row=4,column=1)

box_address=Entry(root, width=30)
box_address.grid(row=5,column=1)

box_city=Entry(root, width=30)
box_city.grid(row=6,column=1)

box_state=Entry(root, width=30)
box_state.grid(row=7,column=1)

box_zipcode=Entry(root, width=30)
box_zipcode.grid(row=8,column=1)

box_gender=Entry(root,width=30)
box_gender.grid(row=9,column=1)


box_username=Entry(root,width=30)
box_username.grid(row=11,column=1)

box_password=Entry(root,width=30)
box_password.grid(row=12,column=1)

#creating text box labels
customer_id_label=Label(root, text='CID (contact dealer for ur unique code)')
customer_id_label.grid(row=0,column=0)

f_name_label=Label(root, text='First name')
f_name_label.grid(row=1,column=0)

l_name_label=Label(root, text='last name')
l_name_label.grid(row=2,column=0)

date_of_birth_label=Label(root, text='date of birth(yyyy-mm-dd)')
date_of_birth_label.grid(row=3,column=0)

contact_number_label=Label(root, text='contact number (10 digit integer)')
contact_number_label.grid(row=4,column=0)

address_label=Label(root, text='address')
address_label.grid(row=5,column=0)

city_label=Label(root, text='city')
city_label.grid(row=6,column=0)

state_label=Label(root, text='state')
state_label.grid(row=7,column=0)

zipcode_label=Label(root, text='zipcode (6 digit integer)')
zipcode_label.grid(row=8,column=0)

gender_label=Label(root, text='Gender(M/F)')
gender_label.grid(row=9,column=0)


username_label=Label(root, text='Username')
username_label.grid(row=11,column=0)

password_label=Label(root, text='Password')
password_label.grid(row=12,column=0)


#creating submit funtion
def submit():
    customer_id=box_customer_id.get()
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
        MessageBox.showerror('Insert Status','All Fields are required')
    
#    elif mysql.connector.errors.DataError==True:
#        MessageBox.showerror('Insert Status','also check if \n1.phone number is 10 digit integer \n2.pincode is 6 digit integer')
    else:
        cursor.execute('''INsert INto customer values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'''.format(customer_id,username,password,f_name,l_name,date_of_birth,contact_number,address,city,state,zipcode,gender))
        print('uploaded')
        MessageBox.showinfo("Insert Status",'Inserted Succesfully''\n''Database Updated')
        root.destroy()
        mycon.commit()
        mycon.close()
   
        
    
#clear text boxes already
    box_customer_id.delete(0,END)
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


#creating submit button
submit_btn=Button(root,text='Add record to database',command=submit)
submit_btn.grid(row=20,column=0,columnspan=2,pady=10,ipadx=100)
