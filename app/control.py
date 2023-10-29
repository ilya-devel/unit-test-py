"""
Модуль содержит функции управления приложением
"""

import click

from app.classes import NumLists


@click.command()
@click.option('-a', default='', help="Укажите первый список чисел через пробел")
@click.option('-b', default='', help="Укажите второй список чисел через пробел")
def check_avg(a, b):
    """
    Данная программа сравнивает среднее значение двух списков чисел и возвращает результат

    """
    if a.strip() == '' or b.strip() == '':
        print("Для справки запустите с ключом --help")
    lst_a = NumLists(a)
    lst_b = NumLists(b)
    print(lst_a.check_avg(lst_b))
