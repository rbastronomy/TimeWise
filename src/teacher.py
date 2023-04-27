"""
class teacher():
    def __init__(self) -> None:
        pass"""
"""import tkinter as tk

class Block:
    def __init__(self, master, text):
        self.master = master
        self.text = text
        self.label = tk.Label(master, text=text, width=10, height=3, bg='white', relief=tk.RAISED)
        self.label.pack()

        # Agregar la funcionalidad de arrastrar y soltar
        self.label.bind('<ButtonPress-1>', self.on_button_press)
        self.label.bind('<B1-Motion>', self.on_button_motion)
        self.label.bind('<ButtonRelease-1>', self.on_button_release)

        self._x = 0
        self._y = 0

    def on_button_press(self, event):
        self._x = event.x
        self._y = event.y

    def on_button_motion(self, event):
        # Calcular la distancia de movimiento
        dx = event.x - self._x
        dy = event.y - self._y

        # Mover la etiqueta
        self.label.place(x=self.label.winfo_x() + dx, y=self.label.winfo_y() + dy)

        # Actualizar las coordenadas iniciales para el próximo movimiento
        self._x = event.x
        self._y = event.y

    def on_button_release(self, event):
        # Ajustar la etiqueta a la columna y fila más cercanas
        col = (self.label.winfo_x() + event.x) // 100
        row = (self.label.winfo_y() + event.y) // 100
        self.label.place(x=col * 100, y=row * 100)

# Crear la ventana principal
root = tk.Tk()
root.title('Matriz de Horarios')
root.geometry("800x600")

# Crear la matriz vacía
matrix = [[None for _ in range(5)] for _ in range(5)]

# Crear bloques en la matriz
for i in range(5):
    for j in range(5):
        block = Block(root, f'Block {i+1}-{j+1}')
        block.label.place(x=j * 100, y=i * 100)
        matrix[i][j] = block

# Iniciar el bucle de eventos de la ventana
root.mainloop()
"""
"""import tkinter as tk

class Block:
    def __init__(self, master, text):
        self.master = master
        self.text = text
        self.label = tk.Label(master, text=text, width=10, height=3, bg='white', relief=tk.RAISED)
        self.label.pack()

        # Agregar la funcionalidad de arrastrar y soltar
        self.label.bind('<ButtonPress-1>', self.on_button_press)
        self.label.bind('<B1-Motion>', self.on_button_motion)
        self.label.bind('<ButtonRelease-1>', self.on_button_release)

        # Crear el menú contextual
        self.menu = tk.Menu(self.master, tearoff=0)
        self.menu.add_command(label='Agregar bloque', command=self.add_block)
        self.menu.add_command(label='Eliminar bloque', command=self.remove_block)

        # Agregar la funcionalidad del menú contextual
        self.label.bind('<Button-3>', self.show_menu)

        self._x = 0
        self._y = 0

    def on_button_press(self, event):
        self._x = event.x
        self._y = event.y

    def on_button_motion(self, event):
        # Calcular la distancia de movimiento
        dx = event.x - self._x
        dy = event.y - self._y

        # Mover la etiqueta
        self.label.place(x=self.label.winfo_x() + dx, y=self.label.winfo_y() + dy)

        # Actualizar las coordenadas iniciales para el próximo movimiento
        self._x = event.x
        self._y = event.y

    def on_button_release(self, event):
        # Ajustar la etiqueta a la columna y fila más cercanas
        col = (self.label.winfo_x() + event.x) // 100
        row = (self.label.winfo_y() + event.y) // 100
        self.label.place(x=col * 100, y=row * 100)

    def show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

    def add_block(self):
        # Crear un nuevo bloque y agregarlo a la matriz
        new_block = Block(self.master, f'Block {len(matrix)+1}-{len(matrix[0])+1}')
        new_block.label.place(x=len(matrix[0]) * 100, y=len(matrix) * 100)
        matrix.append([new_block])

    def remove_block(self):
        # Eliminar el bloque actual de la matriz y destruir su etiqueta
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == self:
                    matrix[i][j].label.destroy()
                    matrix[i][j] = None
                    return

# Crear la ventana principal
root = tk.Tk()
root.title('Matriz de Horarios')

# Crear la matriz vacía
matrix = [[None for _ in range(5)] for _ in range(5)]

# Crear bloques en la matriz
for i in range(5):
    for j in range(5):
        block = Block(root, f'Block {i+1}-{j+1}')
        block.label.place(x=j * 100, y=i * 100)
        matrix[i][j] = block

# Iniciar el bucle de eventos
"""
"""
import tkinter as tk
from tkinter import messagebox

class Block:
    def __init__(self, master, text):
        self.master = master
        self.text = text
        self.label = tk.Label(master, text=text, width=10, height=3, bg='white', relief=tk.RAISED)
        self.label.pack()

        # Agregar la funcionalidad de arrastrar y soltar
        self.label.bind('<ButtonPress-1>', self.on_button_press)
        self.label.bind('<B1-Motion>', self.on_button_motion)
        self.label.bind('<ButtonRelease-1>', self.on_button_release)

        self._x = 0
        self._y = 0

    def on_button_press(self, event):
        self._x = event.x
        self._y = event.y

    def on_button_motion(self, event):
        # Calcular la distancia de movimiento
        dx = event.x - self._x
        dy = event.y - self._y

        # Mover la etiqueta
        self.label.place(x=self.label.winfo_x() + dx, y=self.label.winfo_y() + dy)

        # Actualizar las coordenadas iniciales para el próximo movimiento
        self._x = event.x
        self._y = event.y

    def on_button_release(self, event):
        # Ajustar la etiqueta a la columna y fila más cercanas
        col = (self.label.winfo_x() + event.x) // 100
        row = (self.label.winfo_y() + event.y) // 100
        self.label.place(x=col * 100, y=row * 100)

def show_context_menu(event):
    global matrix
    col = event.x // 100
    row = event.y // 100
    if row >= len(matrix) or col >= len(matrix[0]):
        return
    block = matrix[row][col]
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Agregar Bloque", command=lambda: add_block(row, col))
    if block is not None:
        menu.add_command(label="Eliminar Bloque", command=lambda: delete_block(row, col))
    menu.post(event.x_root, event.y_root)

def add_block(row, col):
    global matrix
    if matrix[row][col] is None:
        block = Block(root, f'Block {row+1}-{col+1}')
        block.label.place(x=col * 100, y=row * 100)
        matrix[row][col] = block

def delete_block(row, col):
    global matrix
    if matrix[row][col] is not None:
        block = matrix[row][col]
        block.label.destroy()
        matrix[row][col] = None


# Crear la ventana principal
root = tk.Tk()
root.title('Matriz de Horarios')

# Crear la matriz vacía con 7 filas y 6 columnas
matrix = [[None for _ in range(6)] for _ in range(7)]


# Crear bloques en la matriz
for i in range(5):
    for j in range(5):
        block = Block(root, f'Block {i+1}-{j+1}')
        block.label.place(x=j * 100, y=(i+1) * 100)
        matrix[i][j] = block

# Agregar el menú contextual
root.bind('<Button-3>', show_context_menu)

# Iniciar el bucle de eventos de la ventana
root.mainloop()
"""

class Teacher():
    def __init__(self, name, rut, birthdate, email):
        self.__Name = name
        self.__Rut = rut
        self.__BirthDate = birthdate
        self.__Email = email

    def GetName(self):
        return self.__Name
    def GetRut(self):
        return self.__Rut
    def GetBirthDate(self):
        return self.__BirthDate
    def GetEmail(self):
        return self.__Email
    



