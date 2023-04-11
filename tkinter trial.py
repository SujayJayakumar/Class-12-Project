#basic gui
'''from tkinter import *
root=Tk()

#creating label widget
myLabel=Label(root,text='Hello World')
#packing it off into screen
myLabel.pack()

root.mainloop()'''

#grid system
'''from tkinter import *
root=Tk()

myLabel1=Label(root,text='Hello World').grid(row=0,column=0)
myLabel2=Label(root,text='My name is Sujay').grid(row=1,column=1)

#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1,column=1)

root.mainloop()'''

#adding buttons
'''from tkinter import *
root=Tk()

def myclick():
    myLabel=Label(root,text='yay, u clicked a button')
    myLabel.pack()
    
myButton=Button(root,text='click me',command=myclick,fg='blue',bg='black')
#myButton=Button(root,text='click me',state=DISABLED)
#myButton=Button(root,text='click me',padx=50)
#myButton=Button(root,text='click me',pady=70)
myButton.pack()

root.mainloop()'''

#entry input box
'''from tkinter import *
root=Tk()

e=Entry(root,width=50,borderwidth=5,bg='yellow',fg='white')
e.pack()
root.mainloop()'''

#using entry box n buttons
from tkinter import *
root=Tk()
e=Entry(root,width=50,borderwidth=3)
e.pack()
#e.insert(0,'enter ur name')
e.get()
def myclick():
    Hello='hello '+e.get()
    myLabel=Label(root,text=Hello)
    #myLabel=Label(root,text='Hello '+e.get())
    myLabel.pack()
myButton=Button(root,text='Enter ur name above n click me',command=myclick)
myButton.pack()

root.mainloop()
