import tkinter
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")


Button(root,text="C",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)

root.mainloop()