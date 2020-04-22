import tkinter as tk
from tkinter import ttk
#from tkinter.ttk import *

window = tk.Tk()#creando el formulario
window.title("Sistemas Inteligentes")# colocandole un titulo
window.geometry('500x200')# dandole dimension al formulario
lbl1 = tk.Label(window,text="Ingrese primer valor: ")#creando un etiqueta
lbl1.grid(column=0,row=0)# asignando posicion a esa etiqueta

txt1 = tk.Entry(window,width=10)
txt1.grid(column=1,row=0)# asignando posicion a esa txt1

def mifuncion():
    lbl1.configure(text="Hola mundo "+txt1.get())#modificando un atributo del lbl
    print("le has clicado al boton")

btn1 = tk.Button(window,text="Boton",command=mifuncion)#creando un boton
btn1.grid(column=2,row=0)# asignando posicion a esa boton

lbl2 = tk.Label(window,text="Ingrese segundo valor: ")#creando un etiqueta
lbl2.grid(column=0,row=1)# asignando posicion a esa etiqueta

txt2 = tk.Entry(window,width=10)
txt2.grid(column=1,row=1)# asignando posicion a esa txt1
def sumar(a,b):
    return a+b

def mifuncion2():
    a = int(txt1.get())
    b = int(txt2.get())    
    lbl2.configure(text="la suma es: "+str(sumar(a,b)))#modificando un atributo del lbl
    print("Has seleccionado: ",cbo1.get())
    

btn2 = tk.Button(window,text="Sumar",command=mifuncion2)#creando un boton
btn2.grid(column=2,row=1)# asignando posicion a esa boton

cbo1 = ttk.Combobox(window)
cbo1['values']=("sumar","restar","multiplicar","potencia")
cbo1.current(1)
cbo1.grid(column=1,row=2)

window.mainloop()#mostrar el formulario
# tarea seleccionar por combo o por radio button la operacion
# matematica que desea realizar (sumar, restar , multiplicar y potencia)
