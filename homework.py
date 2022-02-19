class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight


    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        
        distance_km = self.action * LEN_STEP / M_IN_KM 
        return distance_km
        

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    workout_type_list = {'SWM' : Swimming,
                     'RUN' : Running,
                     'WLK' : SportsWalking}

    class_obj = workout_type_list[workout_type]

    if workout_type == 'SWM':
        return class_obj(workout_type, data[0], data[1], data[2], data[3], data[4])
    elif workout_type == 'RUN':
        return class_obj(workout_type, data[0], data[1], data[2])
    elif workout_type == 'WLK':
        return class_obj(workout_type, data[0], data[1], data[2], data[3])


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

