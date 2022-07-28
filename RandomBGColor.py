from tkinter import *
import random

root=Tk()

root.title("Background Color Frenzy")
root.geometry("500x400")
root.configure(bg="#9fbded")

bobl={"Colors":["#f23a3a","#fc8530","#ffe159","#c9f562","#7cf564","#6df2ab","#72c9f7","#77a6f2","#5658db","#ac6eeb","#e56eeb","#eb6eaa"]}

def changeBG():
    r=random.randint(0,11)
    root.configure(bg=bobl["Colors"][r])
    print(bobl["Colors"][r])

btn=Button(root,text="Change the BG",command=changeBG,bg="#fffcc2")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
