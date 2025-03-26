count = 0

def my_custome_decorator(function):
    def wrapper(*args, **kwargs):
        global count = count + 1
        print(count)
        return function(*args, **kwargs)

    return wrapper


@my_custome_decorator
def suma(a, b):
    return (a + b)


print(suma(2, 2))
print(suma(2, 2))
print(suma(2, 2))
print(suma(2, 2))
