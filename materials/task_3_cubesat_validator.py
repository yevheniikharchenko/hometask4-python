"""
Задача 3: Валідатор телеметрії маяка малого супутника (CubeSat).
Вхідний файл: cubesat_frames.txt
Вихідний файл: thermal_warnings.log
"""

valid_frames = 0
corrupt_frames = 0


def process_beacon_line(line, warning_file=None):
    """Обробляє один рядок маяка супутника та оновлює глобальні лічильники."""
    global valid_frames, corrupt_frames
    # TODO:
    # 1. Якщо 'CORRUPT' у рядку -> збільште corrupt_frames та завершіть функцію
    # 2. Розпакуйте числові поля: v_bat, i_solar, *temperatures = ... (конвертуйте у float)
    # 3. Перевірте температури (T > 60.0) циклом for без прапорців:
    #    - при перегріві: запишіть попередження у warning_file, викличте flush() та break
    #    - якщо перегріву не було, переведіть у Кельвіни через map() + lambda, відфільтруйте > 300 K
    #      через filter() + lambda та виведіть результат
    pass


def main():
    # TODO: Відкрийте cubesat_frames.txt та читайте у циклі while з моржевим оператором (:=):
    # while line := f.readline(): ...
    # Пошкоджені рядки пропускайте, а в кінці виведіть статистику.
    pass


if __name__ == '__main__':
    main()
