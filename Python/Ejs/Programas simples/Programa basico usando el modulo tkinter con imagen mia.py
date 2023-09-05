print("Hola usuario!")
name=input("Como es su nombre?\n")
from tkinter import *
from PIL import ImageTk, Image
if name.startswith("N") or name.startswith("n"):
    root=Tk()
    root.title("Este sos vos?")
    root.geometry("1280x720")
    # img=Image.open(r"C:\Users\NAZA\Desktop\Codigo\Python\Ejs\Archivos importables\Yo en una imagen.jpg")
    # img.show()
    img=ImageTk.PhotoImage(Image.open(r"C:\Users\NAZA\Desktop\Codigo\Python\Ejs\Archivos importables\Yo.jpg"))
    label=Label(im=img)
    label.pack()
    root.mainloop()