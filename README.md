# qa_python
### test_init_genres
Проверяет корректность инициализации экземпляра класса по жанрам в методе *__init__*
### test_add_new_book_add_two_books
Проверяет, что добавилось именно две книги. Метод *add_new_book*
### test_add_new_book_not_added
Проверяет что книги без названия или с очень длинным названием не добавляются. Метод *add_new_book*
### test_add_new_book_already_added_not_added
Проверяет, что ранее добавленная книга не добавляется повторно. Метод *add_new_book*
### test_set_book_genre_new_book_genre_set
Проверяет возможность добавления жанра к книге. Метод *set_book_genre*
### test_set_book_genre_new_book_unknown_genre_not_set
Проверяет что жанр не из списка не добавляется. Метод *set_book_genre*
### test_set_book_genre_change_genre_changed
Проверяет возможность смены жанра у книги. Метод *set_book_genre*
### test_get_book_genre_no_book
Проверяет запрос жанра у недобавленной книги. Метод *get_book_genre*
### test_get_books_with_specific_genre
Проверяет что В список попали только книги с указанным жанром. Метод *get_books_with_specific_genre*
### test_get_books_genre
Проверяет работу метода *test_get_books_genre*
### test_get_books_for_children_no_restricted
Проверяет что в список детских книг не попали книги с жанрами ограниченными по возрасту. Метод *get_books_for_children*
### test_add_book_in_favorites_book_from_list
Проверяет возможность добавить известную книгу в избранное *add_book_in_favorites*
### test_add_book_in_favorites_book_not_from_list
Проверяет возможность добавить книгу не из списка. *add_book_in_favorites*
### test_delete_book_from_favorites_book_from_list
Проверяет удаление из избранного ранее добавленной книги. Метод *add_book_in_favorites*

Метод *get_list_of_favorites_books* проверяется в тестах *test_delete_book_from_favorites_book_from_list* *test_add_book_in_favorites_book_not_from_list*, *test_add_book_in_favorites_book_from_list*