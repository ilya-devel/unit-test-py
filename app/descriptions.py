"""
Данный модуль содержит дескрипторы для проверки корректности переданных данных
"""

class CheckListNum:
    """
    Данный класс проверяет введённое значение на соответствие требованиям
    """
    def __init__(self, name: str = None):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        lst_num = [float(num) for num in value.split()] \
            if isinstance(value, str) else map(float, value)
        setattr(instance, self.param_name, lst_num)

    def __delete__(self, instance):
        raise AttributeError(f"Свойство {self.param_name} нельзя удалять")

    @staticmethod
    def check_valid_letter(row, valid_letter):
        """
        Проверяет элементы строки на наличие символов отличных от переданного валидного списка
        :param row:
        :param valid_letter:
        :return:
        """
        if isinstance(row, str):
            for letter in row:
                if letter not in valid_letter:
                    raise ValueError("В списке могут быть только целые числа или \
                    числа с плавающей точкой")

    def validate(self, value):
        """
        Проверяет корректность переданных данных
        :param value:
        :return:
        """
        if isinstance(value, (tuple, list)):
            for val in value:
                if isinstance(val, str):
                    self.check_valid_letter(val, '1234567890.')
        else:
            if not isinstance(value, str) or not value:
                raise ValueError(f"Значение {value} может быть пустой строкой")
            for letter in value:
                self.check_valid_letter(letter, '0123456789. ')
