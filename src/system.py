"""import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
import pandas as pd
import numpy as np
import xlsxwriter
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
"""
"""
# Crear una tabla para mostrar los horarios disponibles
class HorarioTable(ttk.Treeview):
    def __init__(self, parent, columns, *args, **kwargs):
        super().__init__(parent, columns=columns, *args, **kwargs)
        
        # Definir los días de la semana y las horas disponibles
        self.dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        self.horas = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
        
        # Crear las columnas de la tabla
        for col in columns:
            self.heading(col, text=col.title())
        
        # Agregar los días de la semana como filas de la tabla
        for i, dia in enumerate(self.dias_semana):
            self.insert("", "end", text=dia, values=[""]*len(columns), open=True)
            
            # Agregar las horas como subfilas de cada día de la semana
            for hora in self.horas:
                self.insert("", "end", text=hora, values=[""]*len(columns), open=False)
                
        # Establecer el tamaño de las columnas de la tabla
        self.column("#0", width=100)
        for col in columns:
            self.column(col, width=100, anchor="center")
        
        # Permitir que los elementos de la tabla sean arrastrados y soltados
        self.bind('<ButtonPress-1>', self._drag_start)
        self.bind('<B1-Motion>', self._drag_motion)
        
        # Variables para almacenar el elemento arrastrado
        self._drag_data = {"text": "", "item": None}
    
    # Funciones para manejar el arrastre de elementos en la tabla
    def _drag_start(self, event):
        item = self.identify_row(event.y)
        if item:
            self._drag_data["item"] = item
            self._drag_data["text"] = self.item(item, "text")
    
    def _drag_motion(self, event):
        if self._drag_data["item"]:
            item = self.identify_row(event.y)
            if item:
                self.move(self._drag_data["item"], "", self.index(item))
    
    # Función para asignar un curso a un horario específico
    def asignar_curso(self, dia, hora, curso):
        for item in self.get_children(dia):
            if self.item(item, "text") == hora:
                self.set(item, "#1", curso)
                break
                
# Crear una lista de cursos disponibles
cursos_disponibles = ["Programación I", "Programación II", "Bases de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Inglés Técnico", "Matemáticas Avanzadas"]

# Función para cargar los cursos disponibles en un ListBox
def cargar_cursos():
    for curso in cursos_disponibles:
        lista_cursos.insert("end", curso)

# Función para asignar un curso a un horario específico
def asignar_curso():
    # Obtener el curso seleccionado en la lista de cursos
    curso_seleccionado = lista_cursos.get(lista_cursos.curselection())
    
    # Obtener el día y la hora seleccionados en la tabla de horarios
    dia_seleccionado = horario_table.item(horario_table.selection()[0], "text")
    hora_seleccionada = horario_table.item(horario_table.selection()[0], "values")[0]
    
    # Asignar el curso al horario seleccionado
    horario_table.asignar_curso(dia_seleccionado, hora_seleccionada, curso_seleccionado)

# Crear la ventana principal
root = tk.Tk()
root.title("Horarios de la Universidad")

# Crear un ListBox para mostrar los cursos disponibles
lista_cursos = tk.Listbox(root)
lista_cursos.pack(side="left", fill="y")

# Cargar los cursos disponibles en el ListBox
cargar_cursos()

# Crear una tabla para mostrar los horarios disponibles
columns = ["Curso"]
horario_table = HorarioTable(root, columns, show="headings")
horario_table.pack(side="right", fill="both", expand=True)

# Crear un botón para asignar un curso a un horario específico
btn_asignar = tk.Button(root, text="Asignar curso", command=asignar_curso)
btn_asignar.pack()

# Iniciar el loop principal de la ventana
root.mainloop()
"""

"""import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

# Función para cargar datos desde archivos CSV o XLSX
def cargar_datos():
    # Abrir cuadro de diálogo para seleccionar archivo
    archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv"), ("Archivos XLSX", "*.xlsx")])
    if not archivo:
        return
    
    # Cargar datos del archivo seleccionado en un DataFrame de Pandas
    try:
        datos = pd.read_csv(archivo) if archivo.endswith(".csv") else pd.read_excel(archivo)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        return
    
    # Aquí hay código para procesar los datos y asignar los horarios
    messagebox.showinfo("Información", "Datos cargados correctamente")

# Función para asignar horarios sin topes
def asignar_horarios():
    # Aquí hay código para asignar horarios sin topes
    messagebox.showinfo("Información", "Horarios asignados correctamente")

# Función para generar archivos PDF, PNG y/o XLSX de horarios
def generar_archivos():
    # Aquí hay código para generar archivos PDF, PNG y/o XLSX de horarios
    messagebox.showinfo("Información", "Archivos generados correctamente")

# Función para bloquear horarios específicos
def bloquear_horarios():
    # Aquí hay código para bloquear horarios específicos
    messagebox.showinfo("Información", "Horarios bloqueados correctamente")

# Crear ventana principal
root = tk.Tk()
root.title("Asignación de Horarios")

# Crear botones para cada funcionalidad
btn_cargar_datos = tk.Button(root, text="Cargar Datos", command=cargar_datos)
btn_cargar_datos.pack()

btn_asignar_horarios = tk.Button(root, text="Asignar Horarios", command=asignar_horarios)
btn_asignar_horarios.pack()

btn_generar_archivos = tk.Button(root, text="Generar Archivos", command=generar_archivos)
btn_generar_archivos.pack()

btn_bloquear_horarios = tk.Button(root, text="Bloquear Horarios", command=bloquear_horarios)
btn_bloquear_horarios.pack()

# Ejecutar loop de la ventana
root.mainloop()
"""
"""
# Variables globales para los datos y los horarios asignados
datos = None
horarios_asignados = None

# Crear ventana principal
root = tk.Tk()
root.title("Asignación de horarios")

# Función para cargar datos desde archivos CSV o XLSX
def cargar_datos():
    global datos
    # Abrir cuadro de diálogo para seleccionar archivo
    archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv"), ("Archivos XLSX", "*.xlsx")])
    if not archivo:
        return
    
    # Cargar datos del archivo seleccionado en un DataFrame de Pandas
    try:
        datos = pd.read_csv(archivo) if archivo.endswith(".csv") else pd.read_excel(archivo)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        return
    
    # Mostrar mensaje de confirmación
    messagebox.showinfo("Información", "Datos cargados correctamente")

# Función para asignar horarios sin topes
def asignar_horarios():
    # Verificar que se hayan cargado los datos previamente
    if not datos_cargados:
        estado_label.config(text="Estado: Primero debe cargar los datos.")
        return
    
    # Crear una lista de horarios para cada estudiante, profesor y sala
    horarios_estudiantes = [{} for _ in range(num_estudiantes)]
    horarios_profesores = [{} for _ in range(num_profesores)]
    horarios_salas = [{hora: {dia: None for dia in range(dias_semana)} for hora in range(horas_dia)} for _ in range(num_salas)]
    
    # Asignar horarios a cada estudiante
    for i, estudiante in enumerate(estudiantes):
        # Obtener los cursos del estudiante
        cursos_estudiante = cursos_por_estudiante[i]
        
        for curso in cursos_estudiante:
            # Obtener los horarios disponibles para el curso
            horarios_disponibles = horarios_por_curso[curso]
            
            # Buscar un horario disponible que no solape con otros cursos del estudiante
            for horario in horarios_disponibles:
                solapamiento = False
                for horario_asignado in horarios_estudiantes[i].values():
                    if solapan(horario, horario_asignado):
                        solapamiento = True
                        break
                
                if not solapamiento:
                    horarios_estudiantes[i][curso] = horario
                    break
    
    # Asignar horarios a cada profesor
    for i, profesor in enumerate(profesores):
        # Obtener los cursos del profesor
        cursos_profesor = cursos_por_profesor[i]
        
        for curso in cursos_profesor:
            # Obtener los horarios disponibles para el curso
            horarios_disponibles = horarios_por_curso[curso]
            
            # Buscar un horario disponible que no solape con otros cursos del profesor
            for horario in horarios_disponibles:
                solapamiento = False
                for horario_asignado in horarios_profesores[i].values():
                    if solapan(horario, horario_asignado):
                        solapamiento = True
                        break
                
                if not solapamiento:
                    horarios_profesores[i][curso] = horario
                    break

    
    # Asignar horarios a salas
    for sala in salas:
        for hora in range(horas_dia):
            for dia in range(dias_semana):
                if sala_disponible(sala, hora, dia):
                    for curso in cursos:
                        if curso in cursos_sala[sala] and curso_disponible(curso, hora, dia):
                            horarios_salas[sala][hora][dia] = curso
                            break
                    else:
                        continue
                    break
    
    # Actualizar los datos de los estudiantes, profesores y salas con sus respectivos horarios
    for i, estudiante in enumerate(estudiantes):
        estudiante["horario"] = horarios_estudiantes[i]
        
    for i, profesor in enumerate(profesores):
        profesor["horario"] = horarios_profesores[i]
        
    for i, sala in enumerate(salas):
        sala["horario"] = horarios_salas[i]
        
    # Mostrar mensaje de éxito
    estado_label.config(text="Estado: Horarios asignados correctamente")

    # Generar archivos de horarios
    generar_archivos(estudiantes, profesores, salas, bloques, horarios)

    # Mostrar mensaje de éxito en la generación de archivos
    estado_label.config(text="Estado: Archivos generados correctamente")

    # Mostrar mensaje final
    estado_label.config(text="Estado: Proceso de asignación de horarios completado")



# Función para generar archivos de horarios en formatos PDF, PNG y XLSX
def generar_archivos(estudiantes, profesores, salas, bloques, horarios):
    # Generar archivos de horarios en formato PDF
    for estudiante in estudiantes:
        nombre_archivo = f"horario_{estudiante}.pdf"
        html = generar_html(estudiante, profesores, salas, bloques, horarios)
        pdfkit.from_string(html, nombre_archivo)

    # Generar archivos de horarios en formato PNG
    for profesor in profesores:
        nombre_archivo = f"horario_{profesor}.png"
        html = generar_html(profesor, estudiantes, salas, bloques, horarios)
        pdfkit.from_string(html, nombre_archivo, {'format': 'png'})

    # Generar archivo de horarios en formato XLSX
    horarios_dict = {}
    for estudiante in estudiantes:
        horarios_dict[estudiante] = generar_horario_dict(estudiante, profesores, salas, bloques, horarios)
    df = pd.DataFrame(horarios_dict)
    df.to_excel("horarios.xlsx", index=False)

def generar_html(nombre, opciones1, opciones2, opciones3, horarios):
    html = "<html><head><style>table, th, td {border: 1px solid black;}</style></head><body>"
    html += f"<h2>Horario de {nombre}</h2>"
    html += "<table><tr><th>Hora/Día</th>"
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        html += f"<th>{dia}</th>"
    html += "</tr>"
    for hora in range(8, 20):
        html += f"<tr><td>{hora}:00 - {hora + 1}:00</td>"
        for dia in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
            html += "<td>"
            if nombre in horarios[dia][hora]:
                clase = horarios[dia][hora][nombre]
                html += f"{clase.materia}<br>{clase.sala}<br>{clase.profesor}"
            html += "</td>"
        html += "</tr>"
    html += "</table></body></html>"
    return html

def generar_horario_dict(nombre, opciones1, opciones2, opciones3, horarios):
    horario = {}
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        horario[dia] = []
        for hora in range(8, 20):
            if nombre in horarios[dia.lower()][hora]:
                clase = horarios[dia.lower()][hora][nombre]
                horario[dia].append(f"{clase.materia}\n{clase.sala}\n{clase.profesor}")
            else:
                horario[dia].append("")
    return horario


# Función para bloquear horarios específicos para profesores
def bloquear_horarios():
    # Verificar que se hayan asignado los horarios
    if not horarios_asignados:
        messagebox.showwarning("Advertencia", "Primero debe asignar los horarios")
        return
    
    # Aquí hay código para bloquear horarios específicos para profesores
    # Se puede utilizar el DataFrame de Pandas con los horarios asignados para identificar los horarios que se deben bloquear
    
    # Mostrar mensaje de confirmación
    messagebox.showinfo("Información", "Horarios bloqueados correctamente")

# Crear botones y etiquetas en la ventana principal
cargar_datos_button = tk.Button(root, text="Cargar datos",command=cargar_datos)
cargar_datos_button.pack(padx=10, pady=5)

asignar_horarios_button = tk.Button(root, text="Asignar horarios", command=asignar_horarios)
asignar_horarios_button.pack(padx=10, pady=5)

generar_archivos_button = tk.Button(root, text="Generar archivos de horarios", command=generar_archivos)
generar_archivos_button.pack(padx=10, pady=5)

bloquear_horarios_button = tk.Button(root, text="Bloquear horarios para profesores", command=bloquear_horarios)
bloquear_horarios_button.pack(padx=10, pady=5)

estado_label = tk.Label(root, text="Estado: Esperando acción...")
estado_label.pack(padx=10, pady=5)


cargar_datos_button.pack(padx=10, pady=10)

asignar_horarios_button = tk.Button(root, text="Asignar horarios", command=asignar_horarios)
asignar_horarios_button.pack(padx=10, pady=10)

generar_archivos_button = tk.Button(root, text="Generar archivos", command=generar_archivos)
generar_archivos_button.pack(padx=10, pady=10)

bloquear_horarios_button = tk.Button(root, text="Bloquear horarios", command=bloquear_horarios)
bloquear_horarios_button.pack(padx=10, pady=10)

datos_label = tk.Label(root, text="Datos cargados: No")
datos_label.pack(padx=10, pady=10)

horarios_label = tk.Label(root, text="Horarios asignados: No")
horarios_label.pack(padx=10, pady=10)

#def actualizar_etiquetas():
 #   global datos, horarios_asignados
  #  datos_label.config(text=f"Datos cargados: {'Sí' if datos is not None else 'No'}")
   # horarios_label.config(text=f"Horarios asignados: {'Sí' if horarios_asignados is not None else 'No'}")
    #root.after(100, actualizar_etiquetas)
    
#actualizar_etiquetas()
root.mainloop()"""

import tkinter as tk
from tkinter import filedialog, messagebox
#import pdfkit
import pandas as pd
from openpyxl import load_workbook
from datetime import datetime, timedelta
from teacher import Teacher as tch
from studient import Studient as std
from classroom import Classroom as csr

# Función para cargar datos desde archivos CSV o XLSX
def CargarDatos():
    global datos
    # Abrir cuadro de diálogo para seleccionar archivo
    archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv"), ("Archivos XLSX", "*.xlsx")])
    if not archivo:
        return
    
    # Cargar datos del archivo seleccionado en un DataFrame de Pandas
    try:
        datos = pd.read_csv(archivo) if archivo.endswith(".csv") else pd.read_excel(archivo)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        return
    
    # Mostrar mensaje de confirmación
    #messagebox.showinfo("Información", "Datos cargados correctamente")

CargarDatos()
#print(datos)
#def cargar_profesor():
#    if
#cargar_profesor()
#profe = []
#profe.append(tch("A", "123456-7", "12-10-1999", "holam@unap.cl"))
#print(profe[0].GetRut())
def CargarProfesor():
    arr = []
    #print(datos.columns.tolist())
    try:
        for index, fila in datos.iterrows():
            arr.append(tch(fila['Profesor'], fila['RUT'], fila['Fecha de nacimiento'], fila['Email']))
            print(f"Teacher {index}: {arr[index].GetName()}, {arr[index].GetRut()}, {arr[index].GetBirthDate()}, {arr[index].GetEmail()}")
        return arr
    except Exception as e:
        print("ARCHIVO CSV O XLSX NO CORRESPONDE PARA ESTA CLASE!")
        #messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        #return

def CargarEstudiante():
    arr = []
    #print(datos.columns.tolist())
    try:
        for index, fila in datos.iterrows():
            arr.append(std(fila['Alumno'], fila['RUT'], fila['Fecha de nacimiento'], fila['Email'], fila['Carrera'], fila['Semestre']))
            print(f"Studient {index}: {arr[index].GetName()}, {arr[index].GetRut()}, {arr[index].GetBirthDate()}, {arr[index].GetEmail()}, {arr[index].GetCareer()}, {arr[index].GetSemester()}")
        return arr
    except Exception as e:
        #print("ARCHIVO CSV O XLSX NO CORRESPONDE PARA ESTA CLASE!")
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        return

def CargarSalas():
    arr = []
    #print(datos.columns.tolist())
    
    try:
        for index, fila in datos.iterrows():
            arr.append(csr(fila['Codigo sala'], fila['Capacidad']))
            print(f"Classroom {index}: {arr[index].GetCode()}, {arr[index].GetCapacity()}")
        return arr
    except Exception as e:
        #print("ARCHIVO CSV O XLSX NO CORRESPONDE PARA ESTA CLASE!")
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        return

def CargarMaterias():
    arr = []
    #print(datos.columns.tolist())    
    try:
        for index, fila in datos.iterrows():
            arr.append(csr(fila['Codigo sala'], fila['Capacidad']))
            print(f"Classroom {index}: {arr[index].GetCode()}, {arr[index].GetCapacity()}")
        return arr
    except Exception as e:
        #print("ARCHIVO CSV O XLSX NO CORRESPONDE PARA ESTA CLASE!")
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        return

        
arr2 = CargarSalas()
#arr2 = CargarProfesor()
#print(arr2[0].GetName())
#print(arr2[1].GetName())