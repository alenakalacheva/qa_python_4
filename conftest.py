import pytest
from main import BooksCollector


@pytest.fixture(scope="function")
def collector():
    return BooksCollector()


@pytest.fixture(scope="function")
def add_book_with_genre(collector):
    book_name = 'Гордость и предубеждение и зомби'
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, 'Ужасы')
    return collector

@pytest.fixture(scope="function")
def add_all_genres(collector):
    books = ['Кроты. Хомяки', 'Гордость и зомби', 'Кто украл запятые', 'Веселые утки', 'Смешной и еще смешнее']
    for book in books:
        collector.add_new_book(book)
        collector.set_book_genre(book, collector.genre[books.index(book)])
    return collector
