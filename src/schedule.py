import tkinter as tk
from tkinter import ttk
from subjects import Subject
class Schedule():
    def __init__(self):
        self.__Header = ["Hora", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
        self.Dataset = [["8:00", "", "", "", "", "", ""],
                            ["9:00", "", "", "", "", "", ""],
                            ["10:00", "", "", "", "", "", ""],
                            ["11:00", "", "", "", "", "", ""],
                            ["12:00", "", "", "", "", "", ""],
                            ["13:00", "", "", "", "", "", ""],
                            ["14:00", "", "", "", "", "", ""],
                            ["15:00", "", "", "", "", "", ""],
                            ["16:00", "", "", "", "", "", ""],
                            ["17:00", "", "", "", "", "", ""],
                            ["18:00", "", "", "", "", "", ""],
                            ["19:00", "", "", "", "", "", ""],
                            ["20:00", "", "", "", "", "", ""],
                            ["21:00", "", "", "", "", "", ""],
                            ["22:00", "", "", "", "", "", ""],
                            ["23:00", "", "", "", "", "", ""]]
    def GetHeader(self):
        return self.__Header
    def CalculateAccurateSubjectSchedule(self,sub:Subject):
        print("and then we done it")
        maxhours = sub.GetLectureHours()
        filledhours = 0
        for i in range(len(self.Dataset)):
            for j in range(len(self.Dataset[1])):
                if(j != 0):
                    if(self.Dataset[i][j].find("") and filledhours <= maxhours):
                        self.Dataset[i][j] = f"{sub.GetId()}\n{sub.GetName()}\nSala: {sub.GetClassroom()}"
                        filledhours += 1 



        



"""import tkinter as tk
from tkinter import ttk

# Crear la ventana de tkinter
root = tk.Tk()
root.title("Matriz")

# Crear una tabla con tres columnas
table = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings")

# Definir el encabezado de cada columna
table.heading("col1", text="Columna 1")
table.heading("col2", text="Columna 2")
table.heading("col3", text="Columna 3")

# Agregar datos a la tabla
table.insert("", "end", values=("1", "2", "3"))
table.insert("", "end", values=("4", "5", "6"))
table.insert("", "end", values=("7", "8", "9"))

# Ajustar el tamaño de cada columna
table.column("col1", width=100, anchor="center")
table.column("col2", width=100, anchor="center")
table.column("col3", width=100, anchor="center")

# Mostrar la tabla en la ventana
table.pack()

# Ejecutar la ventana de tkinter
root.mainloop()"""


"""import tkinter as tk
from tkinter import ttk

# Creamos la ventana principal
root = tk.Tk()
root.title("Tabla de datos")

# Creamos el encabezado de la tabla
header = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
table = ttk.Treeview(root, columns=header, show="headings")
for col in header:
    table.heading(col, text=col.title())
table.pack()

# Agregamos algunas filas de ejemplo
#data = [["Juan", "Perez", "30"],
 #       ["Ana", "Garcia", "25"],
  #      ["Pedro", "Lopez", "40"]]
data = [["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"],
        ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"],
        ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]]
for row in data:
    table.insert("", "end", values=row)

# Mostramos la ventana principal
root.mainloop()"""

# Creamos la ventana principal
root = tk.Tk()
root.title("Tabla de datos")

# Creamos el encabezado de la tabla
#header = ["Hora", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
sch = Schedule()
table = ttk.Treeview(root, columns=sch.GetHeader(), show="headings")
for col in sch.GetHeader():
    table.heading(col, text=col.title())
table.pack()

# Agregamos algunas filas de ejemplo
data = [["8:00", "", "", "", "", "", ""],
        ["9:00", "", "", "", "", "", ""],
        ["10:00", "", "", "", "", "", ""],
        ["11:00", "", "", "", "", "", ""],
        ["12:00", "", "", "", "", "", ""],
        ["13:00", "", "", "", "", "", ""],
        ["14:00", "", "", "", "", "", ""],
        ["15:00", "", "", "", "", "", ""],
        ["16:00", "", "", "", "", "", ""],
        ["17:00", "", "", "", "", "", ""],
        ["18:00", "", "", "", "", "", ""],
        ["19:00", "", "", "", "", "", ""],
        ["20:00", "", "", "", "", "", ""],
        ["21:00", "", "", "", "", "", ""],
        ["22:00", "", "", "", "", "", ""],
        ["23:00", "", "", "", "", "", ""]]
for row in data:
    table.insert("", "end", values=row)

# Mostramos la ventana principal
root.mainloop()

