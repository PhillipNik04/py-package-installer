import os
import tkinter as tk
from tkinter import *
import threading

#creation of the window/canva

root= tk.Tk()
root.resizable(0,0)
root.title("PY Packages Installer")

canvas1 = tk.Canvas(root,highlightthickness=0, width = 300, height = 400, bg="SteelBlue4", relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Libray Name:', bg="SteelBlue4", fg="white")
label1.config(font=('helvetica', 16))
canvas1.create_window(150, 60, window=label1)

label2 = tk.Label(root, text='Library:', bg="SteelBlue4", fg="white")
label2.config(font=('helvetica', 16))
canvas1.create_window(80, 140, window=label2)

label3 = tk.Label(root, text='Pip:', bg="SteelBlue4", fg="white")
label3.config(font=('helvetica', 16))
canvas1.create_window(220, 140, window=label3)

entry1 = tk.Entry (root, width =20)
entry1.config(font=("helvetica",16))
canvas1.create_window(150,100, window=entry1)

#commands for multithreading in the programm

def threading1():
   work1=threading.Thread(target=installPackage)
   work1.start()

def threading2():
   work1=threading.Thread(target=uninstallPackage)
   work1.start()

def threading3():
   work1=threading.Thread(target=updatePackage)
   work1.start()

def threading4():
   work1=threading.Thread(target=updatePipPackage)
   work1.start()

def threading5():
   work1=threading.Thread(target=listPackages)
   work1.start()

def threading6():
   work1=threading.Thread(target=versionPackage)
   work1.start()

#command for pip to work

def installPackage():
    global installPythonPackage
    installPythonPackage = 'pip install ' + entry1.get()
    
    os.system(' start cmd /k ' + installPythonPackage)
    
def uninstallPackage():
    global uninstallPythonPackage
    uninstallPythonPackage = 'pip uninstall -y ' + entry1.get()
    
    os.system('start cmd /k ' + uninstallPythonPackage)

def updatePackage():
    global updatePythonPackage
    updatePythonPackage = 'pip install --upgrade ' + entry1.get()
    os.system('start cmd /k ' + updatePythonPackage)

def updatePipPackage():
    global updatePIPpackage
    updatePIPpackage = 'python.exe -m pip install --upgrade pip'
    
    os.system('start cmd /k ' + updatePIPpackage)

def listPackages():
    global listPythonPackages
    listlibs= 'pip list'

    os.system('start cmd /k '+ listlibs)

def versionPackage():
    global versionPIPpackage
    versionPIPpackage = 'pip --version'
    
    os.system('start cmd /k ' + versionPIPpackage)

#all the buttons

button1 = tk.Button(text='      Install     ', command=threading1, bg='green', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(80, 180, window=button1)


button2 = tk.Button(text='   Uninstall   ', command=threading2, bg='crimson', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(80, 230, window=button2)

button3 = tk.Button(text='     Update    ', command=threading3, bg='maroon', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(80, 280, window=button3)

button4 = tk.Button(text='     Update    ', command=threading4, bg='blue', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(220, 180, window=button4)

button5 = tk.Button(text='Downloads ', command=threading5, bg='violet', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(220, 230, window=button5)

button6 = tk.Button(text='    Version    ', command=threading6, bg='orange', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(220.5, 280, window=button6)

#contex menu copy/paste/cut

def cut_text():
        entry1.event_generate(("<<Cut>>"))


def copy_text():
        entry1.event_generate(("<<Copy>>"))


def paste_text():
        entry1.event_generate(("<<Paste>>"))
        
menu = Menu(root, tearoff = 0) 
menu.add_command(label="Cut", command=cut_text) 
menu.add_command(label="Copy", command=copy_text) 
menu.add_command(label="Paste", command=paste_text)
def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
root.bind("<Button-3>", context_menu)    

root.mainloop()