"""import random
import pandas as pd


profesores = []
materias = []

# Generar 10 profesores
for i in range(1, 11):
    profesor = {
        'Nombre': f'Profesor {i}',
        'Apellido': f'Apellido {i}',
        'Rut': f'Rut {i}',
        'Materias': [],
        'Fecha de nacimiento': f'Fecha {i}',
        'Direccion': f'Direccion {i}',
        'Correo': f'Correo {i}'
    }
    profesores.append(profesor)

# Generar 20 materias
materias = []
materias_codigo = ['MAT101', 'FIS201', 'QUI301', 'BIO401', 'ING501']
materias_nombre = ['Matemáticas', 'Física', 'Química', 'Biología', 'Inglés']
paralelos = ['A', 'B', 'C']

for i in range(1, 21):
    materia = {
        'Nombre': materias_nombre[random.randint(0, 4)],
        'Codigo de materia': materias_codigo[random.randint(0, 4)],
        'Paralelo': paralelos[random.randint(0, 2)],
        'Sala': None,
        'Creditos academicos': random.randint(1, 5),
        'Horas de catedra': 0,
        'Tipo de modalidad': '',
        'Cupo total de la materia': random.randint(10, 30)
    }
    materias.append(materia)

# Asignar materias a los profesores
for profesor in profesores:
    num_materias = random.randint(3, 6)
    materias_asignadas = random.sample(materias, num_materias)
    for materia in materias_asignadas:
        paralelo = paralelos[random.randint(0, 2)]
        materia_nueva = materia.copy()
        materia_nueva['Paralelo'] = paralelo
        profesor['Materias'].append(materia_nueva)

# Imprimir los datos generados
print("Profesores:")
print(profesores)
print("\nMaterias:")
print(materias)

# Crear un dataframe con los datos
df_profesores = pd.DataFrame(profesores)
df_materias = pd.DataFrame(materias)

# Crear un writer para exportar a Excel
with pd.ExcelWriter('datos_generados.xlsx') as writer:
    # Escribir el dataframe de profesores en una hoja llamada "Profesores"
    df_profesores.to_excel(writer, sheet_name='Profesores', index=False)

    # Escribir el dataframe de materias en una hoja llamada "Materias"
    df_materias.to_excel(writer, sheet_name='Materias', index=False)

    # Escribir cada conjunto de materias asignadas a cada profesor en una hoja individual
    for i, profesor in enumerate(profesores):
        df_materias_asignadas = pd.DataFrame(profesor['Materias'])
        df_materias_asignadas.to_excel(writer, sheet_name=f'Profesor {i+1}', index=False)
"""
"""
import pandas as pd
import random

profesores = []
materias = []

# Generar 10 profesores
for i in range(1, 11):
    profesor = {
        'Nombre': f'Profesor {i}',
        'Apellido': f'Apellido {i}',
        'Rut': f'Rut {i}',
        'Materias': [],
        'Fecha de nacimiento': f'Fecha {i}',
        'Direccion': f'Direccion {i}',
        'Correo': f'Correo {i}'
    }
    profesores.append(profesor)

# Generar 20 materias
materias = []
materias_codigo = ['MAT101', 'FIS201', 'QUI301', 'BIO401', 'ING501']
materias_nombre = ['Matemáticas', 'Física', 'Química', 'Biología', 'Inglés']
paralelos = ['A', 'B', 'C']
salas = ['A1','A2','A3','A4','A5','A6','A7', None]

for i in range(1, 21):
    materia = {
        'Nombre': materias_nombre[random.randint(0, 4)],
        'Codigo de materia': materias_codigo[random.randint(0, 4)],
        'Paralelo': paralelos[random.randint(0, 2)],
        'Sala': salas[random.randint(0, 7)],
        'Creditos academicos': random.randint(1, 5),
        'Horas de catedra': 0,
        'Tipo de modalidad': '',
        'Cupo total de la materia': random.randint(10, 30)
    }
    materias.append(materia)

# Asignar materias a los profesores
for profesor in profesores:
    num_materias = random.randint(3, 6)
    materias_asignadas = random.sample(materias, num_materias)
    for materia in materias_asignadas:
        paralelo = paralelos[random.randint(0, 2)]
        materia_nueva = materia.copy()
        materia_nueva['Paralelo'] = paralelo
        profesor['Materias'].append(materia_nueva)

# Convertir los datos en dataframes de Pandas
df_profesores = pd.DataFrame(profesores)
df_materias = pd.DataFrame(materias)

# Exportar los dataframes a archivos Excel
df_profesores.to_excel('profesores.xlsx', index=False)
df_materias.to_excel('materias.xlsx', index=False)

print("Archivos Excel generados exitosamente.")

# Crear un DataFrame para los profesores
profesores_df = pd.DataFrame(profesores)

# Expandir las materias para cada profesor en filas
profesores_materias_df = profesores_df.explode('Materias')

# Crear un DataFrame para las materias
materias_df = pd.DataFrame(materias)

# Exportar los DataFrames a un archivo CSV
profesores_materias_df.to_csv('profesores_materias.csv', index=False)
materias_df.to_csv('materias.csv', index=False)
"""
import csv
profesores = {
    'Juan Pérez': {
        'rut': '12345678-9',
        'nacimiento': '15/06/1975',
        'materias': [
            {
                'nombre': 'Introducción a la Programación',
                'codigo': 'PROG101',
                'paralelo': 'A',
                'sala': 101,
                'creditos': 5,
                'horas_catedra': 3,
                'modalidad': 'presencial',
                'cupo': 30
            },
            {
                'nombre': 'Programación Avanzada',
                'codigo': 'PROG201',
                'paralelo': 'B',
                'sala': 201,
                'creditos': 6,
                'horas_catedra': 4,
                'modalidad': 'mixto',
                'cupo': 25
            },
            {
                'nombre': 'Bases de Datos',
                'codigo': 'BBDD101',
                'paralelo': 'A',
                'sala': 202,
                'creditos': 4,
                'horas_catedra': 2,
                'modalidad': 'online',
                'cupo': 40
            }
        ]
    },
    'Ana Fernández': {
        'rut': '98765432-1',
        'nacimiento': '10/02/1980',
        'materias': [
            {
                'nombre': 'Redes de Computadores',
                'codigo': 'RC101',
                'paralelo': 'A',
                'sala': 102,
                'creditos': 5,
                'horas_catedra': 3,
                'modalidad': 'presencial',
                'cupo': 30
            },
            {
                'nombre': 'Programación Orientada a Objetos',
                'codigo': 'POO201',
                'paralelo': 'A',
                'sala': 201,
                'creditos': 6,
                'horas_catedra': 4,
                'modalidad': 'presencial',
                'cupo': 25
            },
            {
                'nombre': 'Sistemas Operativos',
                'codigo': 'SO101',
                'paralelo': 'B',
                'sala': 202,
                'creditos': 4,
                'horas_catedra': 2,
                'modalidad': 'online',
                'cupo': 40
            }
        ]
    }
}

with open('profesores.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir los encabezados de las columnas
    writer.writerow(['Profesor', 'RUT', 'Fecha de nacimiento', 'Materia', 'Código', 'Paralelo', 'Sala', 'Créditos', 'Horas cátedra', 'Modalidad', 'Cupo'])
    
    # Iterar sobre los profesores y sus materias
    for profesor, datos in profesores.items():
        for materia in datos['materias']:
            
            # Escribir los datos de cada materia
            writer.writerow([profesor, datos['rut'], datos['nacimiento'], materia['nombre'], materia['codigo'], materia['paralelo'], materia['sala'], materia['creditos'], materia['horas_catedra'], materia['modalidad'], materia['cupo']])