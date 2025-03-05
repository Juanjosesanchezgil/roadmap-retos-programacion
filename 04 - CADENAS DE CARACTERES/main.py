"""
Operaciones
"""

s1 = "Hola"
s2 = "Python"

# Concatenacion
print(s1 + " " + s2)

# Repeticion
print(s1 * 3)

# Indexacion
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s1))

# Slicing (porcion)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda


def analiza(palabra1: str, palabra2: str):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if palabra1 == palindromo(palabra2):
        return ("Es un palindromo")
    

def palindromo(palabra):
    palabra_convertida = palabra[::-1]
    return palabra_convertida


print(analiza("arroz", "zorrA"))
