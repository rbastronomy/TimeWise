# Agregamos algunas filas de ejemplo
"""data = [["8:00", " ", " ", " ", " ", " ", " "],
        ["9:00", " ", " ", " ", " ", " ", " "],
        ["10:00", " ", " ", " ", " ", " ", " "],
        ["11:00", " ", " ", " ", " ", " ", " "],
        ["12:00", " ", " ", " ", " ", " ", " "],
        ["13:00", " ", " ", " ", " ", " ", " "],
        ["14:00", " ", " ", " ", " ", " ", " "],
        ["15:00", " ", " ", " ", " ", " ", " "],
        ["16:00", " ", " ", " ", " ", " ", " "],
        ["17:00", " ", " ", " ", " ", " ", " "],
        ["18:00", " ", " ", " ", " ", " ", " "],
        ["19:00", " ", " ", " ", " ", " ", " "],
        ["20:00", " ", " ", " ", " ", " ", " "],
        ["21:00", " ", " ", " ", " ", " ", " "],
        ["22:00", " ", " ", " ", " ", " ", " "],
        ["23:00", " ", " ", " ", " ", " ", " "]]
"""
"""data = [["8:00", "a", "", "c", "d", "e", "f"],
        ["9:00", "g", "h", "i", "j", "k", "l"]]
print(len(data[0]))
for i in range(len(data)):
    for j in range(len(data[0])):
        if j != 0:
            if(data[i][j] == ""):
                data[i][j] = "sex"
            print(f"i,j:{i},{j} = {data[i][j]}")
"""
"""import tkinter as tk
from tkinter import ttk

# Creamos la ventana principal
root = tk.Tk()

# Creamos el widget de tabla
table = ttk.Treeview(root)

# Definimos las columnas de la tabla
table['columns'] = ('col1', 'col2', 'col3')

# Añadimos las cabeceras de las columnas
table.heading('col1', text='Columna 1')
table.heading('col2', text='Columna 2')
table.heading('col3', text='Columna 3')

# Permitimos la selección múltiple de celdas
table.tag_configure('sel', background='blue')
table['selectmode'] = 'extended'

# Permitimos la navegación con teclado
table.bind('<Up>', lambda e: table.selection_add(table.focus()))
table.bind('<Down>', lambda e: table.selection_add(table.focus()))
table.bind('<Left>', lambda e: table.selection_add(table.prev(table.focus())))
table.bind('<Right>', lambda e: table.selection_add(table.next(table.focus())))
table.bind('<Shift-Up>', lambda e: table.yview_scroll(-1, 'units'))
table.bind('<Shift-Down>', lambda e: table.yview_scroll(1, 'units'))
table.bind('<Shift-Left>', lambda e: table.xview_scroll(-1, 'units'))
table.bind('<Shift-Right>', lambda e: table.xview_scroll(1, 'units'))

# Permitimos copiar y pegar celdas
def copy():
    # Obtenemos los índices de las columnas
    col_indices = [table['columns'].index(col) for col in table['columns']]
    # Obtenemos las filas seleccionadas
    selected_rows = table.selection()
    # Creamos una lista con los valores de las celdas seleccionadas
    cells = []
    for row_id in selected_rows:
        cells.append([table.item(row_id, 'values')[col] for col in col_indices])
    # Unimos los valores en una sola cadena, separados por tabulaciones
    data = '\n'.join(['\t'.join(row) for row in cells])
    # Copiamos los datos al portapapeles
    root.clipboard_clear()
    root.clipboard_append(data)

def paste():
    clipboard = root.clipboard_get()
    if clipboard:
        rows = clipboard.split('\n')
        for row in rows:
            values = row.split('\t')
            table.insert('', 'end', values=values)

table.bind('<Control-c>', lambda e: copy())
table.bind('<Control-v>', lambda e: paste())

# Permitimos ordenar la tabla por columna
def sort_column(col):
    data = [(table.set(child, col), child) for child in table.get_children('')]
    data.sort()
    for i, item in enumerate(data):
        table.move(item[1], '', i)
    table.heading(col, command=lambda: sort_column(col))

for col in table['columns']:
    table.heading(col, text=col, command=lambda c=col: sort_column(c))

# Añadimos los datos a la tabla
matrix = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

for row in matrix:
    table.insert('', 'end', values=row)
""#"for row in matrix:
    row_id = table.insert('', 'end', values=row)
    for col, val in enumerate(row):
        entry = tk.Entry(table, justify='center', bd=0)
        entry.insert(0, val)
        table.window_create(table.insert(row_id, 'end', values=""), window=entry, padx=5, pady=5)
        entry.bind('<Return>', lambda e: table.focus())
        entry.bind('<FocusOut>', lambda e: table.set(row_id, table['columns'][col], entry.get()))
""#"
def edit_cell(event):
    ""#"Callback para editar una celda al hacer clic en ella."#""
    # Obtener el identificador de la fila y la columna seleccionadas
    row_id, col = table.identify_row(event.y), table.identify_column(event.x)
    # Obtener el valor actual de la celda
    current_value = table.item(row_id)['values'][int(col[1:])-1]
    # Crear una caja de entrada para editar la celda
    entry = tk.Entry(table, width=10)
    entry.insert(0, current_value)
    # Insertar la caja de entrada en la tabla
    table.delete(row_id, col)
    table.insert(row_id, col, widget=entry)

table.bind('<Button-1>', edit_cell)

# Mostramos la tabla en la ventana
table.pack()

# Ejecutamos el loop principal
root.mainloop()

"""

"""import tkinter as tk

# Crear una matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Crear una ventana de Tkinter
ventana = tk.Tk()

# Crear una tabla de cuadrícula
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        # Crear una celda de la tabla
        celda = tk.Entry(ventana, width=5)
        celda.grid(row=i, column=j)
        celda.insert(0, matriz[i][j])

# Mostrar la ventana de Tkinter
ventana.mainloop()
"""
"""import tkinter as tk

class Table:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns

        # Crear una matriz vacía de Entry widgets
        self.widgets = []
        for i in range(rows):
            row = []
            for j in range(columns):
                cell = tk.Entry(root, width=10)
                cell.grid(row=i, column=j)
                row.append(cell)
            self.widgets.append(row)

    # Método para obtener los datos de la tabla como una lista de listas
    def get_data(self):
        data = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self.widgets[i][j].get())
            data.append(row)
        return data

# Crear la ventana principal
root = tk.Tk()

# Crear la tabla
table = Table(root, 5, 5)

# Crear un botón que imprime los datos de la tabla
button = tk.Button(root, text="Imprimir datos", command=lambda: print(table.get_data()))
button.grid(row=6, column=0)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
"""
import tkinter as tk

class Table:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns

        # Crear una matriz vacía de Entry widgets
        self.widgets = []
        for i in range(rows):
            row = []
            for j in range(columns):
                cell = tk.Entry(root, width=15, font=('Arial', 14), bg='white', relief=tk.RIDGE, borderwidth=1)
                cell.grid(row=i+1, column=j, padx=3, pady=3)
                row.append(cell)
            self.widgets.append(row)

        # Agregar etiquetas de columna
        for j in range(columns):
            label = tk.Label(root, text=f"Column {j+1}", font=('Arial', 14), bg='white', padx=5, pady=5)
            label.grid(row=0, column=j)

    # Método para obtener los datos de la tabla como una lista de listas
    def get_data(self):
        data = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self.widgets[i][j].get())
            data.append(row)
        return data

# Crear la ventana principal
root = tk.Tk()

# Personalizar el estilo de la ventana
root.geometry('700x500')
root.title("Tabla de ejemplo")
root.configure(bg='white')

# Crear la tabla
table = Table(root, 10, 10)

# Obtener la posición de la última fila de la tabla
last_row = table.rows

# Crear un botón que imprime los datos de la tabla
button = tk.Button(root, text="Imprimir datos", font=('Arial', 14), bg='lightblue', command=lambda: print(table.get_data()))

# Agregar el botón justo debajo de la última fila de la tabla
button.grid(row=last_row+1, column=0, sticky=tk.EW, pady=50)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
