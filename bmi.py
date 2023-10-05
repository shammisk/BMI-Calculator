from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


root= Tk()

root= Tk()
root.title('BMI calculator')
root.geometry('470x580+300+200')
root.resizable(False, False)
root.configure(bg="#f0f1f5")


def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)

#icon image
image_icon=PhotoImage(file="img/bmi.png")
root.iconphoto(False,image_icon)

#top image
top=PhotoImage(file="img/top.png")
top_image=Label(root,image=top,background='#f0f1f5')
top_image.place(x=20,y=5)

#main Label
Label(root,width=72,height=18,bg='lightblue').pack(side=BOTTOM)

#box image
box=PhotoImage(file="img/box.png")
Label(root,image=box).place(x=20,y=110)
Label(root,image=box).place(x=240,y=110)

#scale image
scale=PhotoImage(file='img/scale.png')
Label(root,image=scale,bg='lightblue').place(x=20,y=310)

#Height
current_value=tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))
    img=(Image.open('img/man.png'))
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70,y=550-size)
    secondimage.image=photo2

style=ttk.Style()
style.configure('TScale',background='white')
slider=ttk.Scale(root,from_=0,to=220,orient="horizontal",style='TScale', command=slider_changed,variable=current_value)
slider.place(x=80,y=250)

#Weight
current_value2=tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())
style2=ttk.Style()
style2.configure('TScale',background='white')
slider2=ttk.Scale(root,from_=0,to=200,orient="horizontal",style='TScale', command=slider_changed2,variable=current_value2)
slider2.place(x=300,y=250)

Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=5,font='arial 50', bg='#fff',fg='#000',bd=0, justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=5,font='arial 50', bg='#fff',fg='#000',bd=0, justify=CENTER)
weight.place(x=255,y=160)
Weight.set(get_current_value2())

#second image
secondimage=Label(root,bg='lightblue')
secondimage.place(x=70,y=530)

#button
Button(root,text='View Report',width=15,height=2,font='arial 10 bold',bg='darkblue',fg='white',command=BMI).place(x=255,y=320)

#Label
label1=Label(root,font='arial 60 bold', bg='lightblue',fg='#fff')
label1.place(x=240,y=360)

label2=Label(root,font='arial 20 bold', bg='lightblue',fg='black')
label2.place(x=260,y=450)

label3=Label(root,font='arial 10 bold', bg='lightblue',fg='black')
label3.place(x=180,y=500)

labelh=Label(root,text='Height (cm)',font='arial 10 bold', fg='black')
labelh.place(x=80,y=130)


labelw=Label(root,text='Weight (kg)',font='arial 10 bold', fg='black')
labelw.place(x=300,y=130)




root.mainloop()