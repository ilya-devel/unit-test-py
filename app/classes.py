"""
Данный модуль содержит классы данного приложения
"""
from app.descriptions import CheckListNum


class NumLists:
    """
    Класс для работы с числовыми списками
    """
    lst_num = CheckListNum()

    def __init__(self, row):
        self.lst_num = row

    def get_avg(self):
        """
        Возвращает среднее значение
        :return:
        """
        return sum(self.lst_num) / len(self.lst_num)

    def __str__(self):
        return str(self.lst_num)

    def __repr__(self):
        return f"NumLists(\"{' '.join([str(num) for num in self.lst_num])}\")"

    def check_avg(self, other):
        """
        Сравнивает среднее значение текущего объекта класса с другим и возвращает результат
        :param other:
        :return:
        """
        if not isinstance(other, NumLists):
            raise TypeError("Объект для сравнения не является классом NumLists")

        if self.get_avg() < other.get_avg():
            return "Второй список имеет большее среднее значение"
        elif self.get_avg() > other.get_avg():
            return "Первый список имеет большее среднее значение"
        else:
            return "Средние значения равны"
