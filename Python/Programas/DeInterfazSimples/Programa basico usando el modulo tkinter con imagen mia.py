print("Hola usuario!")
name=input("Como es su nombre?\n")
from tkinter import *
from tkinter.tix import IMAGETEXT
if name.startswith("N") or name.startswith("n"):
    root=Tk()
    root.title("Este sos vos?")
    root.geometry("1280x720")
    img=IMAGETEXT.PhotoImage(Image.open(r"C:\Users\Naza\Documents\Codigo\CodPersonal\Python\Programas\Importables"))
    label=Label(im=img)
    label.pack()
    root.mainloop()