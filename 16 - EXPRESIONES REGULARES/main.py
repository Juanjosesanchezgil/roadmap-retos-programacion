import re


def find_numbers(text: str) -> list:
    return re.findall(r"[0-9]+", text)


print(find_numbers("El 13 tengo que ir a comprar 4 aviones y 3 barcos"))
