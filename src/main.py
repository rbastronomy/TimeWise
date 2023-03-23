"""
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
import flet as ft
from database.operacion import sumar, restar
import pandas as pd
import os
"""
def main(page: ft.Page):

    t = ft.Text(value = "Hola mundo", color = "green")
    page.controls.append(t)
    page.update()

    page.title = "Ejemplo Fleto"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_number = ft.TextField(value="0", text_align= ft.TextAlign.RIGHT, width = 100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click = minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click = plus_click),
            ],
            alignment = ft.MainAxisAlignment.CENTER,
        )
    )
#ft.app(target = main)
ft.app(target = main, view = ft.WEB_BROWSER)
"""

df = pd.read_excel('Libro1.xlsx')

print(df.head())
