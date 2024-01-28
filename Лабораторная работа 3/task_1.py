import doctest


class Book:
    def __init__(self,  name: str, author: str) -> None:
        """
        Базовый класс "Книга"

        :param name: Название книги
        :param author: Автор книги

        Примеры:
        >>> book = Book("Медный всадник. Петербургская повесть.", "А. С. Пушкин")
        >>> print(book)
        Книга Медный всадник. Петербургская повесть.. Автор А. С. Пушкин
        >>> book.__repr__()
        "Book(name='Медный всадник. Петербургская повесть.', author='А. С. Пушкин')"
        >>> book.name = "Вечера на хуторе близ Диканьки"
        Атрибуты name и author изменяться не могут.
        >>> book.author = "Н. В. Гоголь"
        Атрибуты name и author изменяться не могут.
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        print("Атрибуты name и author изменяться не могут.")

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        print("Атрибуты name и author изменяться не могут.")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        Дочерний класс "Бумажная книга"

        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = PaperBook("Медный всадник. Петербургская повесть", "А. С. Пушкин", 120)
        >>> print(book)
        Книга Медный всадник. Петербургская повесть. Автор А. С. Пушкин
        >>> book.__repr__()
        "PaperBook(name='Медный всадник. Петербургская повесть', author='А. С. Пушкин', pages=120)"
        >>> book.name = "Вечера на хуторе близ Диканьки"
        Атрибуты name и author изменяться не могут.
        >>> book.author = "Н. В. Гоголь"
        Атрибуты name и author изменяться не могут.
        >>> book.pages = 122
        """
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if isinstance(new_pages, int) and 0 < new_pages:
            self._pages = new_pages
        else:
            raise ValueError("Ошибка при изменении количества страниц. Проверьте, чтобы кол-во страниц было int и больше нуля.")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Дочерний класс "Аудио книга"

        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность книги (в минутах)

        Примеры:
        >>> book = AudioBook("Медный всадник. Петербургская повесть", "А. С. Пушкин", 123.72)
        >>> print(book)
        Книга Медный всадник. Петербургская повесть. Автор А. С. Пушкин
        >>> book.__repr__()
        "AudioBook(name='Медный всадник. Петербургская повесть', author='А. С. Пушкин', duration=123.72)"
        >>> book.name = "Вечера на хуторе близ Диканьки"
        Атрибуты name и author изменяться не могут.
        >>> book.author = "Н. В. Гоголь"
        Атрибуты name и author изменяться не могут.
        >>> book.duration = 120.7
        """
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if isinstance(new_duration, float) and 0.0 < new_duration:
            self._duration = new_duration
        else:
            raise ValueError("Ошибка при изменении количества страниц. Проверьте, чтобы кол-во страниц было int и было больше 0.0 минут.")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
