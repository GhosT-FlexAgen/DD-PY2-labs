import doctest


class Car:
    def __init__(self, color: str, acceleration: float, mileage: float) -> None:
        """
        Создание объекта "Машина"

        :param color: Цвет автомобиля
        :param acceleration: Максимальный разгон, км/ч
        :param mileage: Пробег, км

        :raise ValueError: Если ускорение автомобиля или его пробег отрицательные, то вызываем ошибку

        Примеры:
        >>> car = Car("red", 198.6, 12923)  # инициализация экземпляра класса
        """
        if acceleration < 0:
            raise ValueError("Ускорение автомобиля не может быть меньше 0.0 км/ч")

        if mileage < 0:
            raise ValueError("Пробег автомобиля не может быть меньше 0.0 км")

        self.color = color
        self.acceleration = acceleration
        self.mileage = mileage

    def mileage_check(self, pick_mileage) -> bool:
        """
        Проверка пробега автомобиля с критическим значением

        :param pick_mileage: Критическое значение пробега, км
        :return: Если текущий пробег больше критического - True, иначе - False

        Примеры:
        >>> car = Car("red", 198.6, 12923)
        >>> car.mileage_check(150000)
        """
        ...

    def get_path_to_top_speed(self) -> float:
        """
        Расчёт пути автомобиля до достижения максимальной скорости по его ускорению

        :return: Путь автомобиля, км

        Примеры:
        >>> car = Car("red", 198.6, 12923)
        >>> car.get_path_to_top_speed()
        """
        ...

    def get_time_to_top_speed(self) -> float:
        """
        Расчёт времени, которое понадобится автомобилю для достижения максимальной скорости по его ускорению

        :return: Время разгона до максимальной скорости в секундах

        Примеры:
        >>> car = Car("red", 198.6, 12923)
        >>> car.get_time_to_top_speed()
        """
        ...


class Flower:
    def __init__(self, petal_color: str, is_perennial: bool) -> None:
        """
        Создание объекта "Цветочек"

        :param petal_color: Цвет лепестков цветочка
        :param is_perennial: Цветок многолетний или нет

        Примеры:
        >>> violet = Flower("purple-blue", True)  # инициализация экземпляра класса
        """
        self.petal_color = petal_color
        self.is_perennial = is_perennial

    def get_contrasting_colours(self) -> list[str]:
        """
        Получение списка цветов контрасных цвету цветка с помощью круга Иттена.

        :return: Список цветов, контрасных цвету цветочка

        Примеры:
        >>> violet = Flower("purple-blue", True)
        >>> violet.get_contrasting_colours()
        """
        ...

    def growth(self) -> None:
        """
        Рост цветочка в течении года с изменением цвета лепестков (их яркости и насыщенности).

        :return: Если цветок многолетний, то после роста его экземпляр остаётся и возвращается в начальное состояние,
                 иначе экземляр класса становится None.

        Примеры:
        >>> violet = Flower("purple-blue", True)
        >>> violet.growth()
        """
        ...


class Bee:
    def __init__(self, age: float, color: str, is_honeybee: bool) -> None:
        """
        Создание объекта "Пчёлка"

        :param age: Возраст пчелы, лет
        :param color: Окрас пчелы
        :param is_honeybee: Медоносная пчела или нет

        :raise ValueError: Если возраст пчелы отрицательный, то вызываем ошибку

        Примеры:
        >>> bee = Bee(2.5, "yellow-brown", True)  # инициализация экземпляра класса
        """
        if age < 0:
            raise ValueError("Возраст пчелы не может быть отрицательным значением")

        self.age = age
        self.color = color
        self.is_honeybee = is_honeybee

    def get_acceptable_colours(self) -> list[str]:
        """
        Получения списка цветов, наиболее привлекательных для пчелы, исходя из её окраса и возраста.

        :return: Список цветов, наиболее привлекательных для пчелы.

        Примеры:
        >>> bee = Bee(2.5, "yellow-brown", True)
        >>> bee.get_honey_quality()
        """
        ...

    def get_honey_quality(self) -> float:
        """
        Расчёт качества мёда исходя из возраста медоносной пчелы.

        :return: Если пчела не медоносная - None, иначе качество мёда от 0.0 до 100 %.

        Примеры:
        >>> bee = Bee(2.5, "yellow-brown", True)
        >>> bee.get_honey_quality()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
