def square(x: int) -> int:
    return x * x


def apply_to_each(func, iter):
    return [func(x) for x in iter]


numeros = [1, 2, 3, 4, 5]
print(apply_to_each(square, numeros))


students = [
    {"name": "Juan", "birthdate": "23-05-1984", "grades": [5, 7, 8, 9, 10]},
    {"name": "Jose", "birthdate": "23-07-2000", "grades": [4, 7, 6, 9, 3]},
    {"name": "Paco", "birthdate": "23-05-1999", "grades": [5, 7, 6, 7, 2]}
]


def average(grades):
    return (sum(grades) / len(grades))


print(
    list(map(lambda student: {
        "name": student["name"],
        "average": average(student["grades"])}, students)
    )
)
