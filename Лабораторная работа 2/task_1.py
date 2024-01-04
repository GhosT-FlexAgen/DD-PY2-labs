import doctest


class Book:
    def __init__(self, id_: int, name: str, pages: int) -> None:
        """
        Создание объекта "Книга"

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book(1, "Test", 1)  # инициализация экземпляра класса
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name="{self.name}", pages={self.pages})'


class Library:
    def __init__(self, books=None):
        """
        Создание объекта "Библиотека"

        :param books: Список книг (необязательный аргумент). Если пользователь его не передал, то библиотека
                      инициализируется с пустым списком книг.

        :raise ValueError: Если тип параметра books получен некорретный, не list(Books)

        Примеры:
        >>> library_1 = Library()  # инициализация экземпляра класса
        >>> library_2 = Library([Book(1, "Test", 1)])  # инициализация экземпляра класса
        """
        if not books is None and type(books) != list:
            raise ValueError("Библиотека может быть инициалищирована только списком, состоящим из экземпляров класса Book.")
        if not books is None and len(books) == 0:
            raise ValueError("Библиотека может быть инициалищирована только списком, состоящим из экземпляров класса Book.")
        if not books is None and type(books[0]) != Book:
            raise ValueError("Библиотека может быть инициалищирована только списком, состоящим из экземпляров класса Book.")

        self.books = books if not books is None else []

    def get_next_book_id(self) -> int:
        """
        Получение идентификатора для добавления новой книги в библиотеку

        :return: идентификатор новой книги:
                     если книг в библиотеке нет, то вернется 1;
                     если книги есть, то вернется идентификатор последней книги увеличенный на 1.

        Примеры:
        >>> library = Library()  # инициализация экземпляра класса
        >>> library.get_next_book_id()
        1
        >>> library = Library([Book(5, "Test", 1)])  # инициализация экземпляра класса
        >>> library.get_next_book_id()
        6
        """
        return self.books[-1].id + 1 if self.books else 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Получение индекса книги в списке, который хранится в атрибуте экземпляра класса.

        :param book_id: Идентификатор книги

        :return: Если книга существует, то вернется индекс книги из списка.

        :raise ValueError: Если книги нет, то вызываем ошибку.

        Примеры:
        >>> library = Library([Book(100, "T1", 10), Book(91, "T0", 7), Book(101, "T2", 5), Book(64, "T5", 9),])
        >>> library.get_index_by_book_id(101)
        2
        """
        if len(self.books) == 0:
            raise ValueError("Книги с запрашиваемым id не существует")

        for id_, book in enumerate(self.books):
            if book.id == book_id:
                return id_

        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
