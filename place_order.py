from tkinter import *
import tkinter as tk
import os
import sys
from PIL import Image,ImageTk
import csv

import mysql.connector
my=mysql.connector.connect(host='localhost',user='root',database='project',password='password')
cursor=my.cursor()
if my.is_connected():
    print('Database connected')



cid=open('current_user.txt')
currentID=cid.read()
cid.close()

