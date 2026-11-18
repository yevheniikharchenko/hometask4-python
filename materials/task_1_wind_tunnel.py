"""
Задача 1: Потоковий аналіз продувки профілю крила в аеродинамічній трубі.
Вхідний файл: wind_tunnel.csv
Вихідний файл: polar_reduced.csv
"""
import csv


def calc_normal_force_coeff(p_upper, p_lower, /, q_dyn, *, calibration_factor=1.0):
    """Обчислює коефіцієнт нормальної сили Cn.
    p_upper та p_lower — суто позиційні (/), calibration_factor — суто іменований (*).
    """
    # TODO: Поверніть ((p_lower - p_upper) / q_dyn) * calibration_factor
    pass


def stream_tunnel_data(csv_path):
    """Генератор, який відкриває CSV через with та повертає кортеж конвертованих чисел через yield."""
    # TODO: Зчитайте csv_path через csv.reader, пропустіть заголовок і поверніть
    # (int(sample_id), float(aoa), float(p_upper), float(p_lower), float(q_dyn))
    yield from ()


def main():
    angles = []
    cn_values = []

    # TODO:
    # 1. Пройдіться по stream_tunnel_data('wind_tunnel.csv') через for + enumerate()
    #    із розпакуванням кортежу в заголовку циклу
    # 2. Побудуйте словник polar_curve
    # 3. Запишіть кожен третій замір  у 'polar_reduced.csv'
    pass


if __name__ == '__main__':
    main()
