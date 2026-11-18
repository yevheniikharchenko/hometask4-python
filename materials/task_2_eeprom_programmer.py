"""
Задача 2: Програматор EEPROM польотного контролера БПЛА.
Вихідний файл: eeprom_pid.bin (заголовок '<4sHH' = 8 байтів, вісь '<fff' = 12 байтів).
"""
import struct

HEADER_FORMAT = '<4sHH'
AXIS_FORMAT = '<fff'
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)  # 8 байтів
AXIS_SIZE = struct.calcsize(AXIS_FORMAT)      # 12 байтів


def init_eeprom(filepath, axes_gains):
    """Записує заголовок b'FCv2' та початкові коефіцієнти (Kp, Ki, Kd) у режимі запису без буферизації."""
    # TODO: Реалізуйте ініціалізацію EEPROM
    pass


def patch_axis_gains(filepath, axis_index, limiter_callback):
    """У режимі читання та запису переходить на вісь axis_index через seek(), модифікує список коефіцієнтів
    на місці з використанням limiter_callback та перезаписує 12 байтів.
    """
    # TODO: Реалізуйте точковий патчинг коефіцієнтів осі
    pass


def main():
    filepath = 'eeprom_pid.bin'
    initial_gains = [
        (4.2, 0.85, 0.12),   # 0: Roll
        (10.8, 1.40, 0.25),  # 1: Pitch
        (6.5, 0.50, 0.05),   # 2: Yaw
    ]

    # 1. Ініціалізація EEPROM
    init_eeprom(filepath, initial_gains)

    # 2. Оновлення осі Pitch (axis_index=1) через callback-лямбду
    patch_axis_gains(filepath, 1, lambda g: min(round(g * 1.15, 4), 12.0))

    # 3. Зчитування всіх осей у зворотному порядку
    # TODO: Прочитайте заголовок, а потім кожну вісь у зворотному порядку через seek()


if __name__ == '__main__':
    main()
