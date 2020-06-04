# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:37:54 2020

@author: nehagupta13
"""
import os
#os.chdir('C:/Users/nehagupta13/Projects/learning/Image_Processong/')
import sys
import subprocess 
import pandas as pd

from playsound import playsound
import googletrans
from googletrans import Translator
translator = Translator()

#import pyodbc

from tkinter import *

import tkinter as tk

from subprocess import call
from flask import Flask
#import os
#from tkinter import *

from flask_cors import CORS

#import tkinter as tk

#app = Flask(__name__)

app = Flask( __name__, static_url_path='' )

port = int( os.getenv( 'PORT', 8000 ) ) 
CORS(app) 

fn = []
mn= []
ln = []
gn = 'Male'
mm = 'Yes'
ed= []
ps=[]
ss=[]
ad=[]
mo=[]
db=[]

@app.route("/VoiceApp")
def func1():
    top = tk.Tk()
    # Code to add widgets will go here...
    top.title("Form Filling GUI")
    top.geometry('1000x8000')
    #label = tk.Label(top, text = "Welcome to DataCamp's Tutorial on Tkinter!").pack()
    
    ###settnf connection key:
    
    #server = 'IN-NEHAGUPTA\SQLEXPRESS' 
    #uname =  'nehagupta13'
    #pword = 'Elf@1991'
    #db1 = 'Kamyaab_india'
    #tcon = 'yes'
    
      
    text_ent = tk.Label(top, text = 'Enter first name:',font = ('arial', 12) )
    text_ent.grid(row=2, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked()) #, command=m.destroy
    button.grid(row=2, column =5)
 
    #####
    text_ent = tk.Label(top, text = 'Enter Middle name:',font = ('arial', 12) )
    text_ent.grid(row=8, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked1()) #, command=m.destroy
    button.grid(row=8, column =5)
   
    #####
    text_ent = tk.Label(top, text = 'Enter Last Name:',font = ('arial', 12) )
    text_ent.grid(row=14, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked2()) #, command=m.destroy
    button.grid(row=14, column =5)
    
    text_ent = tk.Label(top, text = 'Enter Gender:',font = ('arial', 12) )
    text_ent.grid(row=22, columnspan = 2)
    
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    C1 = Checkbutton(top, text = "Male", variable = CheckVar1,
                      onvalue = 1, offvalue = 0).grid(row=23,column = 1, sticky=W)
    C2 = Checkbutton(top, text = "Female", variable = CheckVar2, 
                     onvalue = 1, offvalue = 0).grid(row=23, column = 2, sticky=W)
    C3 = Checkbutton(top, text = "Others", variable = CheckVar3, 
                     onvalue = 1, offvalue = 0).grid(row=23, column = 3, sticky=W)
    
    Button(top, text='Submit', command=var_states).grid(row=23, column = 4, sticky=W, pady=4)
    
    #####
    
    #####
    text_ent = tk.Label(top, text = 'Are you Married?:',font = ('arial', 12) )
    text_ent.grid(row=25, columnspan = 2)
   
    m1 = IntVar()
    m2 = IntVar()
    
    C1 = Checkbutton(top, text = "Yes", variable = m1).grid(row=26,column = 1, sticky=W)
    C2 = Checkbutton(top, text = "No", variable = m2, 
                     onvalue = 1, offvalue = 0).grid(row=26, column = 2, sticky=W)
    
    Button(top, text='Submit', command=var_states1).grid(row=26, column = 4, sticky=W, pady=4)

    #####
    text_ent = tk.Label(top, text = 'Enter Educational Qualification:',font = ('arial', 12) )
    text_ent.grid(row=28, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked3()) #, command=m.destroy
    button.grid(row=28, column =5)
    
    
    text_ent = tk.Label(top, text = 'Enter Primary skills:',font = ('arial', 12) )
    text_ent.grid(row=32, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked4()) #, command=m.destroy
    button.grid(row=32, column =5)
    
    #####
    text_ent = tk.Label(top, text = 'Enter Secondary skills:',font = ('arial', 12) )
    text_ent.grid(row=36, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked5()) #, command=m.destroy
    button.grid(row=36, column =5)
    
    text_ent = tk.Label(top, text = 'Enter Aadhar number:',font = ('arial', 12) )
    text_ent.grid(row=40, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked6()) #, command=m.destroy
    button.grid(row=40, column =5)
    
        
    text_ent = tk.Label(top, text = 'Enter Mobile number:',font = ('arial', 12) )
    text_ent.grid(row=44, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked7()) #, command=m.destroy
    button.grid(row=44, column =5)
    
    ##
    text_ent = tk.Label(top, text = 'Enter DOB',font = ('arial', 12) )
    text_ent.grid(row=48, columnspan = 2)
    
    button = tk.Button(top, text='Click', width=15, bg="orange", fg="black", command = lambda: clicked8()) #, command=m.destroy
    button.grid(row=48, column =5)
    
    button = tk.Button(top, text='Submit Details', width=15, bg="orange", fg="black", command = lambda: clicked9()) #, command=m.destroy
    button.grid(row=50, column = 7)
    
    top.mainloop()

def clicked():
    
    playsound('AUD-20200602-WA0019.wav') 
    a1 = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    
    print(a1)
    a1 = a1.decode('utf-8')
    fn.append(a1.replace('\r\n',''))
    a1r= translator.translate(a1, dest = 'hi')
    res = tk.Label(top, text = a1r.text,  font = ('arial', 18, 'bold'))
    res.grid(row = 4, column = 1)
   # a1r1= translator.translate(a1.decode('utf-8'), dest = 'en')
   # res1 = tk.Label(top, text = a1r1.text,  font = ('arial', 18, 'bold'))
   # res1.grid(row = 4, column = 4)


def clicked1():
    
    playsound('AUD-20200602-WA0019.wav')  
    a2 = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    print(a2)
    a2 = a2.decode('utf-8')
    mn.append(a2.replace('\r\n',''))
    a2r = translator.translate(a2, dest = 'hi')
    res = tk.Label(top, text = a2r.text, wraplength=1500, font = ('arial', 18, 'bold'))
    res.grid(row = 10, column = 1)
    #a2r1= translator.translate(a2, dest = 'en')
    #res1 = tk.Label(top, text = a2r1.text,  font = ('arial', 18, 'bold'))
    #res1.grid(row = 10, column = 4)


def clicked2():
    playsound('AUD-20200602-WA0019.wav') 
    a = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    print(a)
    a = a.decode('utf-8')
    ln.append(a.replace('\r\n',''))
    a2r = translator.translate(a, dest = 'hi')
    res = tk.Label(top, text = a2r.text, wraplength=1500,font = ('arial', 18, 'bold'))
    res.grid(row = 16, column = 1)


#####

def var_states():
   print("male: %d,\nfemale: %d,\nLGBT: %d" % (CheckVar1.get(), CheckVar2.get(),CheckVar3.get()))
   if(CheckVar1.get()==1):
       gn = 'Male'
       print(gn)
   if(CheckVar2.get()==1):
       gn = 'Female'
       print(gn)
   if(CheckVar3.get()==1):
       gn = 'Others'
       print(gn)
       


def var_states1():
  # print("male: %d,\nfemale: %d,\nLGBT: %d" % (CheckVar1.get(), CheckVar2.get()))
   if(m2.get()==1):
       mm = 'No'
       print(mm)
 

def clicked3():
    playsound('AUD-20200602-WA0019.wav') 
    a2 = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    print(a2)
    a2 = a2.decode('utf-8')
    ed.append(a2.replace('\r\n',''))
    a2r = translator.translate(a2, dest = 'hi')
    res = tk.Label(top, text = a2r.text, wraplength=1500, font = ('arial', 18, 'bold'))
    res.grid(row = 30, column = 1)
    a2r1= translator.translate(a2, dest = 'en')
    res1 = tk.Label(top, text = a2r1.text,  font = ('arial', 18, 'bold'))
    res1.grid(row = 30, column = 4)

#####

#####

def clicked4():
    playsound('AUD-20200602-WA0019.wav') 
    a2 = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    print(a2)
    a2 = a2.decode('utf-8')
    ps.append(a2.replace('\r\n',''))
    a2r = translator.translate(a2, dest = 'hi')
    res = tk.Label(top, text = a2r.text, wraplength=1500, font = ('arial', 18, 'bold'))
    res.grid(row = 34, column = 1)
    a2r1= translator.translate(a2, dest = 'en')
    res1 = tk.Label(top, text = a2r1.text,  font = ('arial', 18, 'bold'))
    res1.grid(row = 34, column = 4)

#####
    

def clicked5():
    playsound('AUD-20200602-WA0019.wav') 
    a2 = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    print(a2)
    a2 = a2.decode('utf-8')
    ss.append(a2.replace('\r\n',''))
    a2r = translator.translate(a2, dest = 'hi')
    res = tk.Label(top, text = a2r.text, wraplength=1500, font = ('arial', 18, 'bold'))
    res.grid(row = 38, column = 1)
    a2r1= translator.translate(a2, dest = 'en')
    res1 = tk.Label(top, text = a2r1.text,  font = ('arial', 18, 'bold'))
    res1.grid(row = 38, column = 4)

#####
    

def clicked6():
    playsound('AUD-20200602-WA0019.wav')  
    a = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    print(a)
    ad.append(a)
    res = tk.Label(top, text = a, wraplength=1500)
    res.grid(row = 42, column = 1)

#####

def clicked7():
    playsound('AUD-20200602-WA0019.wav') 
    a = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    print(a)
    mo.append(a)
    res = tk.Label(top, text = a, wraplength=1500)
    res.grid(row = 46, column = 1)


def clicked8():
    playsound('AUD-20200602-WA0019.wav') 
    a = subprocess.check_output([sys.executable, "speech_text_Google_API.py"])
    print(a)
    a = a.decode('utf-8')
    db.append(a.replace('\r\n',''))
    res = tk.Label(top, text = a.replace('\r\n',''), wraplength=1500)
    res.grid(row = 50, column = 1)
    
    

def clicked9():
    d = {'FIRST_NAME' :fn,'MIDDLE_NAME' : mn, 'LAST_NAME' : ln,'GENDER' : gn,
      'MARITAL_STATUS' : mm,
      'EDUCATION_DEGREE' :ed,
      'PRIMARY_SKILLS': ps,
      'SECONDARY_SKILLS' :ss,
      'AADHAR_NUMBER' : ad,
      'MOBILE_NUMBER' :mo,
      'DATE_OF_BIRTH' : db}
    d = {k: None if not v else v for k, v in d.items() }
    df = pd.DataFrame.from_dict(d)
    #df.to_csv('test.csv')
    
    #cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1, trusted_connection=tcon, user=uname, password=pword)
    #cursor = cnxn.cursor()
    #cols = ",".join([str(i) for i in df.columns.tolist()])
    #values = "','".join([str(i) for i in df.iloc[0].tolist()])
    #sql = "INSERT INTO Kamyaab_india.dbo.LND_EMPLOYEE_REGISTRATION (" +cols + ") VALUES ('" +values+ "')"
    #cursor.execute(sql)
    #cnxn.commit()
    
    messagebox.showinfo("Status", "Data submitted successfully!")
    
    
    
    
   
  
  
# creating column list for insertion


     
if __name__ == "__main__":
    
    #app.run(debug=True)
    app.run( host='0.0.0.0', port=port, debug=True) 
