""" orientado a objetos
print("Hola Mundo")

class Animal:
    def __init__(self, especie, peso):
        self.especie = especie
        self.peso = peso

    def Sonido(self):
        print("A")
class Gato(Animal):
    def __init__(self, especie, peso):
        super().__init__(especie, peso)
    def Sonido(self):
        print("Meow")


Animalia = Animal("Gato", 4) 
Animalia.Sonido()
Gatito = Gato("Gato", 4)
Gatito.Sonido()
"""
from database.operacion import sumar, restar #ejemplo de importar funciones de otro archivo
import pandas as pd #para el excel
import tkinter as tk #para la interfaz grafica
import os #para acceder y manipular archivos

### Leer excel
df = pd.read_excel('Libro1.xlsx')

print(df.head())
###


# Funciones que se llaman al seleccionar cada opción
def opcion1():
    print("Seleccionaste la opción 1")

def salida():
    exit()
# Creación de la ventana y los elementos
ventana = tk.Tk()

menu = tk.Menu(ventana)

etiqueta = tk.Label(ventana, text="Selecciona una opción:")
etiqueta.pack()

opcion_menu1 = tk.Menu(menu, tearoff=0)
opcion_menu1.add_command(label="Opcion 1", command=opcion1)

menu.add_cascade(label="Menu", menu=opcion_menu1)

ventana.config(menu=menu)
#boton1 = tk.Button(ventana, text="Opción 1", command=opcion1)
#boton1.pack()

boton4 = tk.Button(ventana, text="Salir", command=salida)
boton4.pack()

ventana.mainloop()
