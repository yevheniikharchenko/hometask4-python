"""
Варіант 2 — Задача 2.4: Планувальник маршруту автономного БПЛА та серіалізація місії.
Вихідні файли: uav_mission.json, uav_mission.pkl
"""
import json
import pickle


def build_waypoint(lat, lon, *active_sensors, **flight_params):
    """Формує маршрутну точку у вигляді вкладеного кортежу ((lat, lon), altitude_m, sensors_tuple)
    та словник розширених параметрів польоту.
    """
    # TODO: Отримайте altitude_m із flight_params (за замовчуванням 1000) та поверніть структуру точки
    pass


def main():
    nav_modes = ('GPS_INS', 'TERRAIN_FOLLOW', 'OPTICAL_FLOW')

    # TODO:
    # 1. Створіть 4 маршрутні точки через build_waypoint(...)
    # 2. Пройдіться по точках циклом із вкладеним розпакуванням: for ((lat, lon), alt, sensors) in waypoints:
    # 3. Вкладеними циклами for згенеруйте комбінації (waypoint_index, nav_mode)
    # 4. Згенеруйте циклічні зсуви старту маршруту через waypoints[i:] + waypoints[:i]
    # 5. Відсортуйте маршрут за висотою через sorted(..., key=lambda wp: wp[1])
    # 6. Збережіть місію в 'uav_mission.json' та 'uav_mission.pkl' (перевірте через pickle.load)
    pass


if __name__ == '__main__':
    main()
