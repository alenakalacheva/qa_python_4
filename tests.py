import pytest


class TestBooksCollector:

    def test_init_genres(self, collector):

        # проверяем корректность инициализации экземпляра класса по жанрам

        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', ['', 'Гордость и предубеждение и зомби зомби!!!'])
    def test_add_new_book_not_added(self, book_name, collector):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_already_added_not_added(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_new_book_genre_set(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        assert collector.get_book_genre(book_name) == 'Ужасы'

    def test_set_book_genre_new_book_unknown_genre_not_set(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужас')
        assert collector.get_book_genre(book_name) == ''

    def test_set_book_genre_change_genre_changed(self, collector, add_book_with_genre):
        book_name = list(collector.get_books_genre())[0]
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'

    def test_get_book_genre_no_book(self, collector):
        assert collector.get_book_genre('Кроты, хомяки') is None

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Хома')
        collector.set_book_genre('Хома', 'Ужасы')
        collector.add_new_book('Хома 2')
        collector.set_book_genre('Хома 2', 'Ужасы')
        collector.set_book_genre('Крот', 'Комедии')
        books_with_genre = collector.get_books_with_specific_genre('Ужасы')
        assert ('Хома' and 'Хома 2' in books_with_genre) and 'Крот' not in books_with_genre

    def test_get_books_genre(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        assert collector.get_books_genre() == {book_name: 'Ужасы'}

    def test_get_books_for_children_no_restricted(self, collector, add_all_genres):
        allowed_books = collector.get_books_for_children()
        for book in allowed_books:
            assert collector.get_book_genre(book) not in collector.genre_age_rating

    def test_add_book_in_favorites_book_from_list(self, collector, add_book_with_genre):
        collector.add_book_in_favorites(list(collector.get_books_genre())[0])
        assert collector.get_list_of_favorites_books() == [list(collector.get_books_genre())[0]]

    def test_add_book_in_favorites_book_not_from_list(self, collector, add_book_with_genre):
        collector.add_book_in_favorites('Pride')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_from_list(self,collector, add_book_with_genre):
        collector.delete_book_from_favorites(list(collector.get_books_genre())[0])
        assert collector.get_list_of_favorites_books() == []
