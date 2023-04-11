from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tempfile
import os
import csv

def product():
    global l
    global cost1
    l=[]
    cost1=[]
    f=open('products.csv','r',newline='')
    r=csv.reader(f)
    for i in r:
        l.append(i)
        cost1.append(i[1])
    print(l)
    print('cost1=',cost1)
product()

root=tk.Toplevel()
root.title('Billing Manangement System')
root.geometry('1280x720')
bg_color='#2D9290'


#=====================variables===================
Bread=IntVar()
Wine=IntVar()
Rice=IntVar()
Gal=IntVar()
Total=IntVar()

cb=StringVar()
cw=StringVar()
cr=StringVar()
cg=StringVar()
total_cost=StringVar()
# ===========Function===============
def change():
    f=open('products.csv','r+',newline='')
    csv_r=csv.reader(f)
    csv_w=csv.writer(f)
    l=[]
    b1=[b,w,r]
    i=0
    global fraud
    fraud=0
    for rec in csv_r:
        if b1[i]>int(rec[2]):
            messagebox.showerror('Error','Sufficient stock unavailable, \nPlease visit the item list ')
            i=i+1
            fraud=1
            root.destroy()
            import bil
            break
        else:
            #for rec in csv_r:
            rec[2]=int(rec[2])-int(b1[i])
            l.append(rec)
            i+=1
    if fraud==0:
        f.seek(0)
        csv_w.writerows(l)
        f.close()
    else:
        pass
    

q1=[]

def total():
    global b
    global w
    global r
    
    for i in q:
        s=int(i.get())
        q1.append(s)
   
    if q1==[] or len(q1)==2 or len(q1)==1:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        
        #messagebox.showinfo('Confirm','Are you sure u want to order the above items?',messageboxbuttons.yes/no)
        #if(MessageBox.Show("","",MessageBoxButtons.YesNo) == DialogResult.Yes):
        #result = messagebox.askyesno(title='Confirm',message='Are you sure u want to order the above items?',detail='Click NO to reset fields')
        #if result:
        
      
        b=q1[0]
        w=q1[1]
        r=q1[2]

        change()

        if fraud==0:
            t=int(b)*int(cost1[0])+int(w)*int(cost1[1])+int(r)*int(cost1[2])
            print(t)
            Total.set(b + w + r)
            total_cost.set('₹ ' + str(round(t, 2)))

            cb.set('₹ '+str(round(int(int(b)*int(cost1[0])),2)))
            cw.set('₹ '+str(round(int(int(w)*int(cost1[1])),2)))
            cr.set('₹ '+str(round(int(int(r)*int(cost1[2])),2)))

            

            messagebox.showinfo('Success','Your order has been confirmed')
            
        else:
            textarea.delete(1.0,END)
            Bread.set(0)
            Wine.set(0)
            Rice.set(0)
            Total.set(0)

            cb.set('')
            cw.set('')
            cr.set('')
            total_cost.set('')
        
    






def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,' Items\tNumber of Items\t  Cost of Items\n')
    textarea.insert(END,f'\nPhone\t\t{b}\t  {cb.get()}')
    textarea.insert(END,f'\n\nlaptop\t\t{w}\t  {cw.get()}')
    textarea.insert(END,f'\n\nHDD\t\t{r}\t  {cr.get()}')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END,f'\nTotal Price\t\t{Total.get()}\t{total_cost.get()}')
    textarea.insert(END, f"\n================================")


def print1():
    with open('Bill.txt', "w", encoding="utf-8") as f:
        q=textarea.get('1.0','end-1c')
        print(q)
        f.write(str(q))
    

    messagebox.showinfo('Success','Your receipt is saved')
    #filename=tempfile.mktemp('.txt')
    #open(filename,'w').write(q)
    #os.startfile(filename,'Print')


'''def reset():
    textarea.delete(1.0,END)
    for i in range (len(l)):
        textvar[i].set(0)
     
    Total.set(0)

    cb.set('')
    cw.set('')
    cr.set('')
    cg.set('')
    total_cost.set('')'''

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()

title=Label(root,pady=5,text="Billing Manangement System",bd=12,bg=bg_color,fg='white',font=('times new roman', 35 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#===============Product Details=================
F1 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color,bd=15,relief=RIDGE)
F1.place(x=5, y=90,width=800,height=500)

#=====================Heading==========================
itm=Label(F1, text='Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1, text='Number of Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=30,pady=15)

cost=Label(F1, text='Cost of Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=30,pady=15)

#===============Product============
p=1
q=[]
textvar=[cb,cw,cr]
jj=0
for j in range (len(l)):

    bread=Label(F1, text=l[j][0], font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
    bread.grid(row=p,column=0,padx=20,pady=15)

    b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable='',justify=CENTER)
    b_txt.grid(row=p,column=1,padx=20,pady=15)
    q.append(b_txt)
    cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=textvar[jj],justify=CENTER)
    cb_txt.grid(row=p,column=2,padx=20,pady=15)
    p+=1
    jj=jj+1

##wine=Label(F1, text='Wine', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
##wine.grid(row=2,column=0,padx=20,pady=15)
##w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Wine,justify=CENTER)
##w_txt.grid(row=2,column=1,padx=20,pady=15)
##cw_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cw,justify=CENTER)
##cw_txt.grid(row=2,column=2,padx=20,pady=15)
##
##rice=Label(F1, text='Rice', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
##rice.grid(row=3,column=0,padx=20,pady=15)
##r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Rice,justify=CENTER)
##r_txt.grid(row=3,column=1,padx=20,pady=15)
##cr_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cr,justify=CENTER)
##cr_txt.grid(row=3,column=2,padx=20,pady=15)
##
##gal=Label(F1, text='Milk', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
##gal.grid(row=4,column=0,padx=20,pady=15)
##g_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Gal,justify=CENTER)
##g_txt.grid(row=4,column=1,padx=20,pady=15)
##cg_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cg,justify=CENTER)
##cg_txt.grid(row=4,column=2,padx=20,pady=15)
##
t=Label(F1, text='Total', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
t.grid(row=5,column=0,padx=20,pady=15)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Total,justify=CENTER)
t_txt.grid(row=5,column=1,padx=20,pady=15)
totalcost_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=total_cost,justify=CENTER)
totalcost_txt.grid(row=5,column=2,padx=20,pady=15)

#=====================Bill areea====================
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)



#=====================Buttons========================
F3 =Frame(root,bg=bg_color,bd=15,relief=RIDGE)
F3.place(x=5, y=590,width=1270,height=120)

btn1 = Button(F3, text='Total', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=total)
btn1.grid(row=0,column=0,padx=20,pady=10)

btn2 = Button(F3, text='Receipt', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3 = Button(F3, text='Save recipt', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=print1)
btn3.grid(row=0,column=2,padx=10,pady=10)

'''btn4 = Button(F3, text='Reset', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=reset)
btn4.grid(row=0,column=3,padx=10,pady=10)'''

btn5 = Button(F3, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=exit)
btn5.grid(row=0,column=4,padx=10,pady=10)





root.mainloop()
