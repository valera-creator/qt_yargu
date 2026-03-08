class Product:
    def __init__(self, name, cnt, weight):
        self.__name = None
        self.__cnt = None
        self.__weight = None

        self.set_name(name)
        self.set_cnt(cnt)
        self.set_weight(weight)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            raise ValueError("название продукта не может быть пустым")
        else:
            self.__name = name

    def get_cnt(self):
        return self.__cnt

    def set_cnt(self, cnt):
        if cnt < 0:
            raise ValueError("количество продукта не может быть отрицательным числом")
        else:
            self.__cnt = cnt

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        if weight < 0:
            raise ValueError("единицы массы продукта не могут быть отрицательным числом")
        else:
            self.__weight = weight
