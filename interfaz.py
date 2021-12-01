from tkinter import *
from lex import analizarLex
from sintactico import *

def getTextInputLex():
    texto = TextoCodigo.get(1.0, END)
    LabelResultado["text"] = analizarLex(texto)


def getTextInputSin():
    texto = TextoCodigo.get(1.0, END)
    LabelResultado["text"] = analizarSin(texto)

raiz =Tk()
raiz.title("Analizador")
raiz.resizable(0,0)
miFrame = Frame(raiz, width="650", height="700", bg="lightgreen")
miFrame.pack()

Label(miFrame, text="Ingrese algo para el analisis", fg="darkred", bg="lightgreen",font=("Arial", 22)).place(x=325, y=50, anchor="center")

TextoCodigo = Text(miFrame, width=70, height=15, padx=10, pady=10)
TextoCodigo.place(x=325, y=200, anchor="center")
LabelResultado=Label(miFrame, text="Aqui ira el resultado del analisis", fg="darkred", bg="lightgreen",font=("Arial Novas", 12))
LabelResultado.place(x=325, y=500, anchor="center")


botonLexico = Button(miFrame, text="Analizador Lexico",command=getTextInputLex).place(x=150, y=600)
botonSintactico = Button(miFrame, text="Analizador Sintactico/semantico",command=getTextInputSin).place(x=350, y=600)

raiz.mainloop()