# -*- coding: utf-8 -*-
"""Desafío 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zXpmjmWlPFvF2-okxeTy2nLbeWn6dyzv

### Desafío 1

Vamos a poner en práctica lo que aprendimos sobre Listas y vamos a utilizar algunos métodos:

1. Creá una lista que contenga 3 materias de la escuela
"""

materias_escuela = ["Matemáticas", "Ciencias", "Historia"]

"""2. Eliminá el primer registro de la lista"""

materias_escuela = materias_escuela[1:]

"""3. Agregá una materia más al final"""

materias_escuela = ["Matemáticas", "Ciencias", "Historia"]
materias_escuela.append("Literatura")

"""4. Seleccioná el segundo elemento de la lista"""

materias_escuela = ["Matemáticas", "Ciencias", "Historia"]
print(materias_escuela[1])