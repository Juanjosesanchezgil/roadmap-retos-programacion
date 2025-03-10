import os

"""
Ejercicio
"""

file_name = "mouredev.txt"

with open(file_name, "w") as file:
    file.write("Brais Moure\n")
    file.write("36\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"""
Extra
"""

file_name = "gestion.txt"


def ventas():
    while True:
        action = input("Introduce una opcion: ")

        if action == "exit":
            os.remove(file_name)
            break

        if action == "add":
            articulos = input("articulos")
            add(articulos)


def add(articulos):
    with open(file_name, "w") as file:
        file.write(articulos)


ventas()
