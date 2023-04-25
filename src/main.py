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
"""
import tkinter as tk
from tkinter import ttk
"""
# Pack a big frame so, it behaves like the window background
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

# Set the initial theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")
"""
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Proyecto TimeWise")
        self.geometry("800x600")

        self.tk.call("source", "../azure.tcl")
        self.tk.call("set_theme", "light")

        # Crear botones
        btn_opcion1 = ttk.Button(self, text="Opción 1", command=self.opcion1)
        btn_opcion2 = ttk.Button(self, text="Opción 2", command=self.opcion2)
        btn_exit = ttk.Button(self, text="Salida", command=self.Salida)
        theme_button = ttk.Button(self, text="Cambiar tema", command=self.change_theme)
        
        # Ubicar botones
        btn_opcion1.pack(pady=10)
        btn_opcion2.pack(pady=10)
        btn_exit.pack(pady=10)
        theme_button.pack(side="left", anchor="sw", padx=20, pady=20)

        self.geometry_pos = self.geometry()
        
    def opcion1(self):
        self.ocultar()
        Opcion1(self, self.geometry_pos)
        
    def opcion2(self):
        self.ocultar()
        Opcion2(self, self.geometry_pos)

    def Salida(self):
        exit()
        
    def ocultar(self):
        self.geometry_pos = self.geometry()
        self.withdraw()
    def change_theme(self):
        # NOTE: The theme's real name is azure-<mode>
        if self.tk.call("ttk::style", "theme", "use") == "azure-dark":
            # Set light theme
            self.tk.call("set_theme", "light")
        else:
            # Set dark theme
            self.tk.call("set_theme", "dark")


class Opcion1(tk.Toplevel):
    def __init__(self, parent, geometry_pos):
        super().__init__(parent)
        
        self.title("Opción 1")
        # Crear botones
        btn_regresar = ttk.Button(self, text="Regresar", command=self.regresar)
        
        # Ubicar botones
        btn_regresar.pack(pady=10)
        
        # Crear imagen y texto
        self.imagen = tk.PhotoImage(file='src\sampletext.png')
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
        self.imagen = tk.PhotoImage(file="src\sampletext.png")
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

"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Proyecto TimeWise")
root.geometry("800x600")

# Pack a big frame so, it behaves like the window background
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

# Set the initial theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

# Create and pack the buttons
#button1 = ttk.Button(big_frame, text="Nuevo horario")
#button1.pack(side="left", padx=20, pady=20)

#button2 = ttk.Button(big_frame, text="Importar Excel")
#button2.pack(side="left", padx=20, pady=20)

#button3 = ttk.Button(big_frame, text="Exportar horario")
#button3.pack(side="left", padx=20, pady=20)

#button4 = ttk.Button(big_frame, text="Salir",command=exit)
#button4.pack(side="left", padx=20, pady=20)
# Obtener el ancho y la altura de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular el ancho del recuadro verde como el 70% del ancho total de la pantalla
color_box_width = int(screen_width * 0.7)

# Crear el frame principal
frame = tk.Frame(root, bd=1, relief="solid")
frame.pack(side="top", fill="both", expand=True)

# Crear la lista de opciones en la izquierda
options_list = tk.Listbox(frame, bd=0)
options_list.pack(side="left", fill="both", expand=True)

# Agregar algunos elementos a la lista de opciones
for item in ["Opción 1", "Opción 2", "Opción 3"]:
    options_list.insert("end", item)

# Crear el recuadro de color verde en la derecha
color_box = tk.Canvas(frame, bg="green", width=color_box_width, height=screen_height)
color_box.pack(side="right", fill="both", expand=True)

theme_button = ttk.Button(big_frame, text="Cambiar tema", command=change_theme)
theme_button.pack(side="left", anchor="sw", padx=20, pady=20)

root.mainloop()"""