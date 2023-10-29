"""
Модуль тестирования функций управления
"""
from click.testing import CliRunner
from app.control import check_avg


def test_check_avg_with_args():
    """
    Проверяет корректность запуска приложения с аргументами
    :return:
    """
    result = CliRunner().invoke(check_avg, ["-a", "2 2 2", "-b", "1 2 3"])
    assert result.exit_code == 0
    assert result.output == "Средние значения равны\n"


def test_check_avg_without_args():
    """
        Проверяет корректность запуска приложения без аргументов
        :return:
        """
    result = CliRunner().invoke(check_avg, [])
    assert result.exit_code == 0
    assert result.output == "Для справки запустите с ключом --help\n"
