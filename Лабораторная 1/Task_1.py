import doctest


class Box:
    def __init__(self, available_capacity: (int, float), occupied_volume: (int, float)):
        """
        Создание и подготовка к работе объекта "Коробка"
        :param available_capacity: Вмещаемая нагрузка (кг)/вмещаемость
        :param occupied_volume: Занимаемая нагрузка (кг)
        Примеры:
        >>> box = Box(15, 0)
        """
        if not isinstance(available_capacity, (int, float)):
            raise TypeError("Вмещаемость коробки должна быть типа int или float")
        if available_capacity <= 0:
            raise ValueError("Вмещаемость коробки должна быть положительным числом или 0")
        self.available_capacity = available_capacity

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Кол-во занимаемой нагрузки должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Кол-во занимаемой нагрузки не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_box(self) -> bool:
        """
        Функция которая проверяет является ли коробка пустой
        :return: Является ли коробка пустой
        Примеры:
        >>> box = Box(15, 0)
        >>> box.is_empty_box()
        """
        ...

    def add_things_in_box(self, thing: int) -> None:
        """
        Добавление вещей в коробку.
        :param thing: Кол-во добавляемых вещей в коробку
        :raise ValueError: Если количество добавляемых вещей превышает свободное место в коробке, то вызываем ошибку
        Примеры:
        >>> box = Box (15, 0)
        >>> box.add_things_in_box(10)
        """
        ...

class Backpack:
    def __int__(self, wrap_status: bool, backpack_capacity: (int, float)):
        """
        Создание и подготовка к работе объекта "Рюкзак"
        :param wrap_status: открыт или закрыт рюкзак
        :param backpack_capacity: вместимость рюкзака(в литрах)
        примеры:
        >>> backpack = Backpack(0, 15)
        """

        if not isinstance(backpack_capacity, (int, float)):
            raise TypeError("Вместимость рюкзака должна быть типа int или float")
        if not backpack_capacity > 0:
            raise ValueError("Вместимость рюкзака должна быть положительным числом")
        self.backpack_capacity = backpack_capacity
        if (wrap_status != 0) and (wrap_status != 1):
            raise ValueError("Рюкзак должен быть закрыт(0) или открыт(1)")
        self.wrap_status = wrap_status

    def close_backpack(self) -> bool:
        """
        Если рюкзак был открыт, тогда функция закрывает его
        Если рюкзак был закрыт, тогда получаем сообщение "Рюкзак закрыт"
        :raise ValueError: возвращает ошибку, если рюкзак изначально был закрыт
        Пример:
        >>> backpack = Backpack(0,13)
        >>> backpack.close_backpack()
        """
        ...

    def open_backpack(self) -> bool:
        """
        Если рюкзак был закрыт, тогда функция открывает его
        Если рюкзак был открыт, тогда получаем сообщение "Рюкзак открыт"
        :raise ValueError: возвращает ошибку, если рюкзак изначально был открыт
        Примеры:
        >>> backpack = Backpack(0, 15)
        >>> backpack.open_backpack()
        """
        ...

    def add_things(self, things: (int, float)) -> None:
        """
        Функция добавляет вещи в рюкзак, совокупный объем которых не больше вместимости рюкзака
        :param things: объем вещей
        :raise ValueError: вернет ошибку, если попытаться переполнить рюкзак
        :return: вернёт число занятого объема
        Примеры:
        >>> backpack = Backpack(1,15)
        >>> backpack.add_things(5)
        """

class House:
    def __int__(self, owner_name: str, height: int):
        """
        Создание и подготовка к работе объекта "Дом"
        :param owner_name: Имя владельца
        :param height: Высота здания в метрах
        """

        if not isinstance(owner_name, str):
            raise TypeError("Имя должно быть типа str")
        self.owner_name = owner_name

        if not isinstance(height, int):
            raise TypeError("Высота толжна быть типа int")
        if height < 0:
            raise ValueError("Высота не может быть отрицательным числом")
        self.height = height

    def elevator_availability(self) -> bool:
        """
        Проверка на наличие в доме лифта
        :return: есть ли в доме лифт
        """
        ...

    def house_age(self, age: [int, float]):
        """
        Выяснение, сколько дому лет.
        :param age: Возраст дома
        :raise TypeError: Если введен неверный тип данных, возвращается ошибка
        :raise ValueError: Если возраст отрицательный, возвращается ошибка
        :return: Возраст дома
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()
        pass
