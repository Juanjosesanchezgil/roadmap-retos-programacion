from enum import Enum

"""
Ejercicio
"""


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_day(number: int):
    print(Weekday(number).name)


get_day(1)
get_day(3)

"""
Extra
"""

class Pedidos():
    
