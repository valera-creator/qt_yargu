class Book:
    def __init__(self, name, author, cnt_pages, link):
        self.name = name
        self.author = author
        self.cnt_pages = cnt_pages
        self.link = link

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Имя книги не может не существовать")
        else:
            self._name = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not author:
            raise ValueError("Автора книги не может не существовать")
        else:
            self._author = author

    @property
    def cnt_pages(self):
        return self._cnt_pages

    @cnt_pages.setter
    def cnt_pages(self, pages):
        try:
            pages = int(pages)
        except ValueError:
            raise ValueError("Значение должно быть числом")
        if pages < 0:
            raise ValueError("Значение не может быть отрицательным")
        if pages == 0:
            raise ValueError("Книга не может содержать 0 страниц")
        self._cnt_pages = pages

    def get_info(self):
        return (f'Название: "{self.name}",\nАвтор: {self.author},\nКоличество страниц: {self.cnt_pages},\n'
                f'Ссылка на обложку: {self.link}')
