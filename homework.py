from dataclasses import dataclass

@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""

    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65

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

        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        raise NotImplementedError('Метод get_spent_calories нужно переопределить')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        info_message = InfoMessage(type(self).__name__,
                                   self.duration,
                                   self.get_distance(),
                                   self.get_mean_speed(),
                                   self.get_spent_calories())
        return info_message

    def duration_in_minutes(self):
        """Перевод длительность тренировки из часов в минуты."""

        return self.duration * 60


class Running(Training):
    """Тренировка: бег."""

    CF_RUN_1: int = 18
    CF_RUN_2: int = 20

    def get_spent_calories(self) -> float:
        """Подсчет потраченных калорий при тренировке: бег."""

        cal_1 = (self.CF_RUN_1 * self.get_mean_speed() - self.CF_RUN_2)
        calories = (cal_1 * self.weight / self.M_IN_KM
                    * self.duration_in_minutes())
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CF_WALK_1: float = 0.035
    CF_WALK_2: int = 2
    CF_WALK_3: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Подсчет потраченных калорий при тренировке: спортивная ходьба."""

        cal_1 = self.get_mean_speed()**self.CF_WALK_2 // self.height
        cal_2 = cal_1 * self.CF_WALK_3 * self.weight
        cal_3 = self.CF_WALK_1 * self.weight + cal_2
        calories = (cal_3 * self.duration_in_minutes())
        return calories


class Swimming(Training):
    """Тренировка: плавание."""

    CF_SWM_1: float = 1.1
    CF_SWM_2: int = 2
    LEN_STEP: float = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        """Подсчет потраченных калорий при тренировке: плавание."""

        cal_1 = self.get_mean_speed() + self.CF_SWM_1
        calories = cal_1 * self.CF_SWM_2 * self.weight
        return calories

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в басейне"""

        cal_1 = self.length_pool * self.count_pool
        speed = cal_1 / self.M_IN_KM / self.duration
        return speed


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    types_of_training = {'SWM': Swimming,
                         'RUN': Running,
                         'WLK': SportsWalking}

    if workout_type in types_of_training:
        return types_of_training[workout_type](*data)
    else:
        raise ValueError("Передается несоответствующий вид тренировки в read_package")


def main(training: Training) -> None:
    """Главная функция."""

    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
