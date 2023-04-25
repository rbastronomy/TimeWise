"""
class teacher():
    def __init__(self) -> None:
        pass"""
"""import tkinter as tk
from tkinter import ttk

# Definir la clase de la aplicación
class HorarioUniversidadApp:
    def __init__(self):
        # Crear la ventana principal
        self.window = tk.Tk()
        self.window.title("Horario de Universidad")

        # Crear los widgets de la interfaz de usuario
        self.label_materia = ttk.Label(self.window, text="Materia:")
        self.label_materia.grid(column=0, row=0, padx=10, pady=10)
        self.entry_materia = ttk.Entry(self.window)
        self.entry_materia.grid(column=1, row=0, padx=10, pady=10)

        self.label_profesor = ttk.Label(self.window, text="Profesor:")
        self.label_profesor.grid(column=0, row=1, padx=10, pady=10)
        self.entry_profesor = ttk.Entry(self.window)
        self.entry_profesor.grid(column=1, row=1, padx=10, pady=10)

        self.label_horario = ttk.Label(self.window, text="Horario:")
        self.label_horario.grid(column=0, row=2, padx=10, pady=10)
        self.entry_horario = ttk.Entry(self.window)
        self.entry_horario.grid(column=1, row=2, padx=10, pady=10)

        self.button_agregar = ttk.Button(self.window, text="Agregar", command=self.agregar_materia)
        self.button_agregar.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.text_resultado = tk.Text(self.window, height=10, width=40)
        self.text_resultado.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        # Iniciar el bucle de eventos
        self.window.mainloop()

    def agregar_materia(self):
        materia = self.entry_materia.get()
        profesor = self.entry_profesor.get()
        horario = self.entry_horario.get()

        # Validar que se hayan ingresado todos los datos
        if materia == "" or profesor == "" or horario == "":
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, "Por favor, complete todos los campos.")
        else:
            # Agregar la materia al horario
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, f"Materia: {materia}\nProfesor: {profesor}\nHorario: {horario}\n\nMateria agregada al horario.")

# Crear una instancia de la aplicación
app = HorarioUniversidadApp()
"""
"""import tkinter as tk
from tkinter import ttk

# Definir la clase de la aplicación
class HorarioUniversidadApp:
    def __init__(self):
        # Crear la ventana principal
        self.window = tk.Tk()
        self.window.title("Horario de Universidad")

        # Crear los widgets de la interfaz de usuario
        self.label_materia = ttk.Label(self.window, text="Materia:")
        self.label_materia.grid(column=0, row=0, padx=10, pady=10)
        self.entry_materia = ttk.Entry(self.window)
        self.entry_materia.grid(column=1, row=0, padx=10, pady=10)

        self.label_profesor = ttk.Label(self.window, text="Profesor:")
        self.label_profesor.grid(column=0, row=1, padx=10, pady=10)
        self.entry_profesor = ttk.Entry(self.window)
        self.entry_profesor.grid(column=1, row=1, padx=10, pady=10)

        self.label_horario = ttk.Label(self.window, text="Horario:")
        self.label_horario.grid(column=0, row=2, padx=10, pady=10)
        self.entry_horario = ttk.Entry(self.window)
        self.entry_horario.grid(column=1, row=2, padx=10, pady=10)

        self.button_agregar = ttk.Button(self.window, text="Agregar", command=self.agregar_materia)
        self.button_agregar.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.text_resultado = tk.Text(self.window, height=10, width=40)
        self.text_resultado.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        self.button_eliminar = ttk.Button(self.window, text="Eliminar", command=self.eliminar_materia)
        self.button_eliminar.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

        # Crear la lista de materias
        self.materias = []

        # Iniciar el bucle de eventos
        self.window.mainloop()

    def agregar_materia(self):
        materia = self.entry_materia.get()
        profesor = self.entry_profesor.get()
        horario = self.entry_horario.get()

        # Validar que se hayan ingresado todos los datos
        if materia == "" or profesor == "" or horario == "":
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, "Por favor, complete todos los campos.")
        else:
            # Agregar la materia a la lista
            self.materias.append({
                "materia": materia,
                "profesor": profesor,
                "horario": horario
            })

            # Mostrar la lista de materias en el cuadro de texto
            self.mostrar_materias()

    def eliminar_materia(self):
        # Obtener el índice de la materia seleccionada
        seleccion = self.text_resultado.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.materias[indice]

            # Mostrar la lista de materias actualizada en el cuadro de texto
            self.mostrar_materias()

    def mostrar_materias(self):
        # Limpiar el cuadro de texto
        self.text_resultado.delete(1.0, tk.END)

        # Mostrar la lista de materias en el cuadro de texto
        for i, materia in enumerate(self.materias):
            self.text_resultado.insert(tk.END, f"{i+1}. {materia['materia']} ({materia['profesor']}) - {materia['horario']}\n")

# Iniciar la aplicación
app = HorarioUniversidadApp()"""
"""import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.cells = []
        for row in range(5):
            row_cells = []
            for column in range(5):
                cell = tk.Label(self, text=f"({row}, {column})", width=10, height=5, relief="solid")
                cell.grid(row=row, column=column)
                cell.bind("<Button-1>", lambda event, row=row, column=column: self.start_drag(event, row, column))
                cell.bind("<B1-Motion>", self.on_drag)
                cell.bind("<ButtonRelease-1>", self.end_drag)
                row_cells.append(cell)
            self.cells.append(row_cells)

        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.grid(row=6, column=2)

    def start_drag(self, event, row, column):
        self.dragging_cell = self.cells[row][column]
        self.dragging_cell_x = event.x
        self.dragging_cell_y = event.y

    def on_drag(self, event):
        x, y = event.x_root, event.y_root
        self.dragging_cell.place(x=x-self.dragging_cell_x, y=y-self.dragging_cell_y)

    def end_drag(self, event):
        row = self.grid_info()['row']
        column = self.grid_info()['column']
        self.cells[row][column] = self.dragging_cell
        self.dragging_cell.grid(row=row, column=column)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
"""
"""import tkinter as tk

class HorarioUniversidad:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [['' for _ in range(columnas)] for _ in range(filas)]

class HorarioUniversidadGUI:
    def __init__(self, filas, columnas):
        self.root = tk.Tk()
        self.horario_universidad = HorarioUniversidad(filas, columnas)
        self.crear_interfaz()

    def crear_interfaz(self):
        self.root.title('Horario Universidad')

        # Crear una matriz de etiquetas para mostrar el horario
        self.etiquetas = []
        for i in range(self.horario_universidad.filas):
            fila_etiquetas = []
            for j in range(self.horario_universidad.columnas):
                etiqueta = tk.Label(self.root, text='', width=15, height=2, relief=tk.RAISED)
                etiqueta.grid(row=i, column=j, padx=5, pady=5)
                etiqueta.bind('<Button-1>', self.iniciar_arrastre)
                etiqueta.bind('<B1-Motion>', self.arrastre)
                etiqueta.bind('<ButtonRelease-1>', self.finalizar_arrastre)
                fila_etiquetas.append(etiqueta)
            self.etiquetas.append(fila_etiquetas)

    def iniciar_arrastre(self, event):
        # Obtener la etiqueta en la que se hizo clic para iniciar el arrastre
        self.etiqueta_seleccionada = event.widget
        self.origen = (self.etiqueta_seleccionada.grid_info()['row'],
                       self.etiqueta_seleccionada.grid_info()['column'])

    def arrastre(self, event):
        # Actualizar la posición de la etiqueta mientras se arrastra
        self.etiqueta_seleccionada.place(x=event.x, y=event.y)

    def finalizar_arrastre(self, event):
        # Obtener la etiqueta de destino y actualizar la matriz de horarios
        destino = (event.widget.grid_info()['row'], event.widget.grid_info()['column'])
        self.horario_universidad.matriz[destino[0]][destino[1]] = self.horario_universidad.matriz[self.origen[0]][self.origen[1]]
        self.horario_universidad.matriz[self.origen[0]][self.origen[1]] = ''
        self.etiqueta_seleccionada.grid(row=destino[0], column=destino[1])
        self.etiqueta_seleccionada = None

    def iniciar(self):
        self.root.mainloop()

# Crear una instancia de la interfaz de usuario con una matriz de 3x3
horario_gui = HorarioUniversidadGUI(3, 3)
horario_gui.iniciar()
"""
"""import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.cells = []
        for row in range(5):
            row_cells = []
            for col in range(5):
                cell = tk.Canvas(master, width=50, height=50, bg="white", highlightthickness=1,
                                 highlightbackground="black")
                cell.grid(row=row, column=col)
                cell.bind("<Button-1>", self.start_drag)
                cell.bind("<B1-Motion>", self.drag)
                cell.bind("<ButtonRelease-1>", self.end_drag)
                row_cells.append(cell)
            self.cells.append(row_cells)
        self.dragging_cell = None

    def start_drag(self, event):
        self.dragging_cell = event.widget

    def drag(self, event):
        if self.dragging_cell:
            self.master.lift(self.dragging_cell)
            self.dragging_cell.place(x=event.x_root, y=event.y_root)

    def end_drag(self, event):
        if self.dragging_cell:
            col, row = self.get_cell_at(event.x_root, event.y_root)
            self.cells[row][col], self.cells[self.dragging_cell.row][self.dragging_cell.col] = \
                self.cells[self.dragging_cell.row][self.dragging_cell.col], self.cells[row][col]
            self.cells[row][col].grid(row=row, column=col)
            self.dragging_cell = None

    def get_cell_at(self, x, y):
        for row_cells in self.cells:
            for cell in row_cells:
                x1, y1, x2, y2 = cell.bbox("all")
                if x1 <= x <= x2 and y1 <= y <= y2:
                    return cell.row, cell.col

root = tk.Tk()
app = App(root)
root.mainloop()"""
import tkinter as tk

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
