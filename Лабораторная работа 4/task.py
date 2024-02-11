import doctest
import math
from typing import List


# Заглушка класса "Противник"
class Enemy:
    ...


class Character:
    def __init__(self,  name: str, characteristic: List[int],
                 cost: int = 0, level: int = 0) -> None:
        """
        Базовый класс "Персонаж"

        :param name: Название персонажа (ник)
        :param characteristic: Характеристики персонажа [Vigor, Mind, Endurance, Strength, Dexterity, Intelligence, Faith, Arcane]
        :param cost: Количество золотых монет у персонажа
        :param level: Уровень персонажа (по-умолчанию 0)

        Примеры:
        >>> hero = Character("Obi-Wan", [1, 99, 1, 1, 1, 99, 0, 0], level=100)
        >>> hero.name = "Obibi-Wana"
        Имя персонажа изменять нельзя.
        >>> hero.cost = 1
        >>> hero.level = 101
        Недостаточно монет для повышения уровня.
        >>> print(hero.get_cost_of_upgrading())
        55066164
        >>> hero.cost = 55066164
        >>> hero.level = 101
        >>> print(hero)
        Персонаж 'Obi-Wan'. Уровень: 101. Характеристики: [1, 99, 1, 1, 1, 99, 0, 0]. Монет: 0.
        >>> hero.__repr__()
        "Character(name='Obi-Wan', characteristic=[1, 99, 1, 1, 1, 99, 0, 0], cost=0, level=101"
        """
        # имя - protected, так как его по правилам игры менять нельзя
        self._name = name
        # level - protected, так как при его измененений подразумевается определённый алгоритм (см. в setter).
        # Например, уровень нельзя уменьшить, и для повышения нужно определённое число cost и т.д.
        self._level = level
        self.cost = cost
        self.characteristic = characteristic

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        print("Имя персонажа изменять нельзя.")

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, new_level) -> None:
        """
        Повышение уровня персонажа за счёт списания соответсвующего кол-ва монет

        :return: True, если повышение выполнено успешно.
                 False - если по какой-то причине не удалось (недостаточно монет, или ручная отмена).
        """
        target_cost = self.get_cost_of_upgrading()
        if target_cost > self.cost:
            print("Недостаточно монет для повышения уровня.")
            return
        self.cost -= target_cost
        self._level += 1
        self.select_characteristic()

    def __str__(self):
        return f"Персонаж {self.name!r}. Уровень: {self.level}. Характеристики: {self.characteristic}. Монет: {self.cost}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, characteristic={self.characteristic!r}, cost={self.cost!r}, level={self.level!r}"

    def get_cost_of_upgrading(self):
        # Получение стоимости повышения уровня
        return int((self._level + 150) * 10 * math.exp(self.level // 10 + self.level % 10))

    def view_characteristic(self):
        # Отображение текущих характеристик персонажа пользователю
        ...

    def select_characteristic(self):
        # Выбор характеристики для повышения с отображением сопуствующей информации пользователю
        ...

    def attach_enemy(self, enemies: List[Enemy]):
        # Нанесение урона противникам исходя из характеристик персонажа
        ...


class Warrior(Character):
    def __init__(self, name: str, characteristic: List[int], type_attack: str,
                 cost: int = 0, level: int = 0, ) -> None:
        """
        Дочерний класс "Воин"

        :param name: Название персонажа (ник)
        :param characteristic: Характеристики персонажа [Vigor, Mind, Endurance, Strength, Dexterity, Intelligence, Faith, Arcane]
        :param type_attack: Тип атаки: тяжёлая, средняя или лёгкая. Влияет на урон от атаки и её скорость. Выбирается при создании.
        :param cost: Количество золотых монет у персонажа
        :param level: Уровень персонажа (по-умолчанию 0)

        Примеры:
        >>> hero = Warrior("Obi-Wan", [1, 99, 1, 1, 1, 99, 0, 0], "heavy", level=100)
        >>> hero.name = "Obibi-Wana"
        Имя персонажа изменять нельзя.
        >>> hero.cost = 1
        >>> hero.level = 101
        Недостаточно монет для повышения уровня.
        >>> print(hero.get_cost_of_upgrading())
        55066164
        >>> hero.cost = 55066164
        >>> hero.level = 101
        >>> print(hero)
        Персонаж 'Obi-Wan'. Уровень: 101. Характеристики: [1, 99, 1, 1, 1, 99, 0, 0]. Монет: 0.
        >>> hero.__repr__()
        "Warrior(name='Obi-Wan', characteristic=[1, 99, 1, 1, 1, 99, 0, 0], type_attack='heavy', cost=0, level=101"
        """
        super().__init__(name, characteristic, cost, level)
        # type_attack - protected, так как его по правилам игры менять нельзя
        self._type_attack = type_attack

    @property
    def type_attack(self) -> str:
        return self._type_attack

    @type_attack.setter
    def type_attack(self, new_type: int) -> None:
        print("Тип атаки изменить нельзя")

    # Методы: get_cost_of_upgrading - получение стоимости повышения уровня,
    #         view_characteristic - просмотр текущих характеристик,
    #         select_characteristic - выбор характеристики для улучшения после повышения уровня
    # унаследованы от базового класса, так как они едины для всех классов.

    # Метод attach_enemy перегружен, так как у класса "Воин" урон, наносимый противникам, зависит не только от
    # характеритик персонажа, но и от типа атаки (тяжёлая, средняя или лёгкая).
    def attach_enemy(self, enemies: List[Enemy]):
        # Нанесение урона противникам исходя из характеристик персонажа и типа атаки.
        ...

    # Метод __repr__ перегружен, так как консруктор класса Warrior расширен типом атаки по сравнению с базовым классом.
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, characteristic={self.characteristic!r}, type_attack={self.type_attack!r}, cost={self.cost!r}, level={self.level!r}"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
