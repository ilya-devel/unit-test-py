"""
Модуль проверки функциональности класса
"""

import pytest

from app.classes import NumLists


class TestNumLists:
    """
    Тестирование класса NumLists
    """
    def test_num_lists_true(self):
        """
        Проверяем корректность создания объекта класса при передаче верных аргументов
        :return:
        """
        num_lst = NumLists('1 2 3 4.5')
        assert repr(num_lst) == 'NumLists(\"1.0 2.0 3.0 4.5\")'
        num_lst = NumLists([1, 2, 3])
        assert repr(num_lst) == 'NumLists(\"1.0 2.0 3.0\")'

    def test_num_lists_error(self):
        """
        Проверяем корректность вывода ошибок при создании объекта класса, \
        когда переданы не верные аргументы
        :return:
        """
        with pytest.raises(ValueError):
            NumLists('1 s 4')
        with pytest.raises(TypeError):
            NumLists()
        with pytest.raises(ValueError):
            NumLists('')
        with pytest.raises(ValueError):
            NumLists('1,1 5,0 4')
        with pytest.raises(ValueError):
            NumLists(['1,1', '5', '0.4'])

    def test_get_avg(self):
        """
        Проверям корректность вывода среднего значения
        :return:
        """
        assert NumLists('1 2 3').get_avg() == 2
        assert NumLists('1 2 3').get_avg() != 3

    def test_check_avg_two_num_lists_equal(self):
        """
        Проверяем вывод, если среднее значения первого и второго списка равны
        :return:
        """
        result = NumLists('1 2 3').check_avg(NumLists('2 2 2'))
        assert result == "Средние значения равны"

    def test_check_avg_two_num_lists_less(self):
        """
        Проверяем вывод, если среднее значение первого списка меньше
        :return:
        """
        result = NumLists('1 2 1').check_avg(NumLists('2 2 2'))
        assert result == "Второй список имеет большее среднее значение"

    def test_check_avg_two_num_lists_larger(self):
        """
        Проверяем вывод, если среднее значение первого списка больше
        :return:
        """
        result = NumLists('4 2 3').check_avg(NumLists('2 2 2'))
        assert result == "Первый список имеет большее среднее значение"

    def test_check_avg_without_second_list(self):
        """
        Проверяем, что функция выдаёт ошибку, если вторым элементом\
         не был передан объект класса
        :return:
        """
        with pytest.raises(TypeError):
            NumLists('4 2 3').check_avg("NumLists('2 2 2')")

    def test_get_string(self):
        """
        Проверяем результат вывода объекта класса как строкового элемента
        :return:
        """
        assert str(NumLists("1 2 3")) == '[1.0, 2.0, 3.0]'

    def test_del_arg_in_num_lists(self):
        """
        Проверяем, что объекту класса запрещено удалять аргументы класса
        :return:
        """
        num_lst = NumLists("1 2 3")
        with pytest.raises(AttributeError):
            delattr(num_lst, "lst_num")
