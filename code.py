from tkinter import *

def Toplama():
sonuc["text"]=int(s1.get()) + int(s2.get())

def Cikarma():
sonuc["text"]=int(s1.get()) - int(s2.get())

def Carpma():
sonuc["text"]=int(s1.get()) * int(s2.get())

def Bolme():
sonuc["text"] = int(s1.get()) / int(s2.get())

window=Tk()
window.geometry("400x500+300+200")
window.title("HESAP MAKİNESİ")

sonuc=Label(window, text="0",bg="beige", width=55,height=2)
sonuc.place(x=5,y=5)

sayi1=Label(window,text="Sayi1:")
sayi1.place(x=110,y=60)

s1=Entry(window, bd=3)
s1.place(x=150,y=60)

sayi2=Label(window,text="Sayi1:")
sayi2.place(x=110,y=85)

s2=Entry(window, bd=3)
s2.place(x=150,y=85)

toplama=Button(window, text="+", font=("Arial",8), bd=2,width=2, command=Toplama).place(x=130,y=140)
toplama=Button(window, text="-", font=("Arial",8), bd=2,width=2, command=Cikarma).place(x=160,y=140)
toplama=Button(window, text="*", font=("Arial",8), bd=2,width=2, command=Carpma).place(x=190,y=140)
toplama=Button(window, text="/", font=("Arial",8), bd=2,width=2, command=Bolme).place(x=220,y=140)

window.mainloop()
