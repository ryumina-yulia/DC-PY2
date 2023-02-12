import doctest

class EquipmentForRhythmicGymnastic:
    """
        Создание и подготовка к работе базового класса "Инвентарь для художественной гимнастики"
    :param brand: производитель
    :param model: вид
    :param weight: вес
    """
    def __init__(self, brand: str, model: str, weight: int):
        self.brand = brand
        self.model = model
        self.weight = weight

    def __str__(self) -> str:
        return f"Производитель {self.brand}. Вид {self.model}. Вес {self.weight}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}"

    def weight_suitable(self, weight: int):
        """
        Функция, которая проверяет, что вес предмета для художественной гимнастики типа int
        :param weight: Вес
        :raise ValueError: Если вес указан тип не int, то вызываем ошибку
        Примеры:
        >>> subject = EquipmentForRhythmicGymnastic("Pastorelli","обруч", 250)
        >>> subject.weight_suitable(250)
        """
        if not isinstance(weight, int):
            raise TypeError("Вес предмета должен быть типа int")

    def weight_total(self, weight: int):
        """
        Функция weight_total проверяет, не превышает ли вес предмета 500 гр
        :param weight: Вес
        :raise ValueError: Если вес больше допустимого, то вызываем ошибку ValueError
        """
        if self.weight >= 500:
            raise ValueError("Вес предмета не может быть более 500 граммов")

class Ball(EquipmentForRhythmicGymnastic):
    """
    Создание дочернего класса "Мяч".
    :param brand: производитель
    :param model: вид
    :param weight: вес
    :param diameter_of_ball: диаметр мяча
     """
    def __init__(self, brand: str, model: str, weight: int, diameter_of_ball: int):
        """
        Расширяем конструктор базового класса, так как у мяча есть дополнительный атрибут - диаметр (diameter_of_ball).
        """
        super().__init__(brand, model, weight)
        self.diameter_of_ball = diameter_of_ball

    def __str__(self)->str:
        """
        Перегружаем  str, так как у мяча есть дополнительный атрибут - диаметр, и это надо отобразить в str
        """
        return f"Производитель {self.brand}. Вид {self.model}. Вес {self.weight}. Диаметр мяча {self.diameter_of_ball}"

    def __repr__(self) -> str:
        """
        Перегружаем  repr так как у мяча есть дополнительный атрибут - диаметр, и это надо отобразить в repr
        """
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}, diameter_of_ball={self.diameter_of_ball}"

    def weight_total(self, weight: int):
        """
        Перегружаем функцию weight_total, так как у мяча вес не может быть больше 350 гр
        """
        if self.weight >= 350:
            raise ValueError ("Вес мяча не может быть более 350 граммов")

    @property
    def diameter_of_ball(self):
        """Возвращает диаметр мяча"""
        return self._diameter_of_ball

    @diameter_of_ball.setter
    def diameter_of_ball (self, new_diameter_of_ball: int) -> None:
        """Устанавливает диаметр мяча."""
        if not isinstance(new_diameter_of_ball, int):
            raise TypeError ("Диаметр мяча должен быть типа int")
        if not new_diameter_of_ball >= 1:
            raise ValueError ("Диаметр мяча должен быть положительным числом")
        self._diameter_of_ball = new_diameter_of_ball


class Clubs(EquipmentForRhythmicGymnastic):
    """
    Дочерний класс "Булавы"
    :param brand: производитель
    :param model: вид
    :param weight: вес
    :param lenght: длина булав
    """

    def __init__(self, brand: str, model: str, weight: int, length_of_clubs: int):
        """Расширяем  конструктор базового класса, так как у булав есть дополнительный атрибут - длина (lenght_of_clubs)
        """
        super().__init__(brand, model, weight)
        self.length_of_clubs = length_of_clubs

    def __str__(self)->str:
        """
        Перегружаем  str, так как у булав есть дополнительный атрибут lenght_of_clubs, и его надо прописать в str
        """
        return f"Производитель {self.brand}. Вид {self.model}. Вес {self.weight}. Длина булав {self.length_of_clubs}"

    def __repr__(self) -> str:
        """
        Перегружаем  repr, так как у булав есть дополнительный атрибут lenght_of_clubs, и его надо прописать в repr
        """
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}, length_of_clubs={self.length_of_clubs}"

    def weight_total(self, weight: int):
        """
        Перегружаем  weight_total так как вес булавы не должен быть более 150 гр.
        """
        if self.weight >= 150:
            raise ValueError("Вес одной булавы не может быть более 150 граммов")


if __name__ == "__main__":
    doctest.testmod()
