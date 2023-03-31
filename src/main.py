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
"""
import tkinter as tk
from tkinter import ttk

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplicación")
        self.geometry("800x600")
        
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure('.', background='#f0f0f0')

        """
        #estilo.configure("TButton", background="red")
        #estilo.configure("Estilo.TButton", foreground="white", background="blue", font=("Helvetica", 12))
        """

        # Crear botones
        btn_opcion1 = ttk.Button(self, text="Opción 1", command=self.opcion1)
        btn_opcion2 = ttk.Button(self, text="Opción 2", command=self.opcion2)
        btn_exit = ttk.Button(self, text="Salida", command=self.Salida)
        
        # Ubicar botones
        btn_opcion1.pack(pady=10)
        btn_opcion2.pack(pady=10)
        btn_exit.pack(pady=10)

        self.geometry_pos = self.geometry()
        
    def opcion1(self):
        self.ocultar()
        Opcion1(self, self.geometry_pos)
        
    def opcion2(self):
        self.ocultar()
        Opcion1(self, self.geometry_pos)

    def Salida(self):
        exit()
        
    def ocultar(self):
        self.geometry_pos = self.geometry()
        self.withdraw()

class Opcion1(tk.Toplevel):
    def __init__(self, parent, geometry_pos):
        super().__init__(parent)
        
        self.title("Opción 1")
        # Crear botones
        btn_regresar = ttk.Button(self, text="Regresar", command=self.regresar)
        
        # Ubicar botones
        btn_regresar.pack(pady=10)
        
        # Crear imagen y texto
        self.imagen = tk.PhotoImage(file='sampletext.png')
        lbl_imagen = tk.Label(self, image=self.imagen)
        lbl_imagen.pack(pady=10)
        lbl_texto = tk.Label(self, text="Texto de la opción 1")
        lbl_texto.pack(pady=10)
        
        #configurar la geometria de la ventana con la posicion recibida
        self.geometry(geometry_pos)

    def regresar(self):
        # Actualizar posición de la ventana principal con la posición actual de la ventana secundaria
        self.master.geometry_pos = self.geometry()
        self.master.geometry(self.master.geometry_pos)
        self.destroy()
        self.master.deiconify()

class Opcion2(tk.Toplevel):
    def __init__(self, parent, geometry_pos):
        super().__init__(parent)
        
        self.title("Opción 2")
        # Crear botones
        btn_regresar = ttk.Button(self, text="Regresar", command=self.regresar)
        
        # Ubicar botones
        btn_regresar.pack(pady=10)
        
        # Crear imagen y texto
        self.imagen = tk.PhotoImage(file="sampletext.png")
        lbl_imagen = tk.Label(self, image=self.imagen)
        lbl_imagen.pack(pady=10)
        lbl_texto = tk.Label(self, text="Texto de la opción 2")
        lbl_texto.pack(pady=10)

        #configurar la geometria de la ventana con la posicion recibida
        self.geometry(geometry_pos)
        
    def regresar(self):
        # Actualizar posición de la ventana principal con la posición actual de la ventana secundaria
        self.master.geometry_pos = self.geometry()
        self.master.geometry(self.master.geometry_pos)
        self.destroy()
        self.master.deiconify()
        
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
