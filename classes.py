from abc import ABC, abstractmethod


class Storage(ABC):
    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @abstractmethod
    def add(self, new_item, item_capacity):
        pass

    @abstractmethod
    def remove(self, item, item_capacity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items: dict = None, capacity: int = 100):
        if items is None:
            items = {}
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def add(self, new_item, item_capacity):
        #  проверка места  на складе
        if self.get_free_space() >= item_capacity:

            if new_item in self.items.keys():
                self.items[new_item] = self.items[new_item] + item_capacity
            else:
                self.items[new_item] = item_capacity

            print(f'На склад успешно помещён товар {new_item} в количестве {item_capacity} позиций.'
                  f' На складе осталось {self.get_free_space()} мест.')
            return [True, new_item, item_capacity]
        else:
            print(f'Склад имеет {self.get_free_space} мест, {new_item} не может быть взят на хранение!')
            return [False, new_item, item_capacity]

    def remove(self, item, item_capacity):
        # Проверка наличия товара и его количества
        if item in self.items.keys():
            if item_capacity < self.items[item]:
                # Отгружаем
                print('Нужное количество есть на складе')
                self.items[item] = self.items[item] - item_capacity
                print(f'Отгрузка товара {item} в количестве {item_capacity} проведена.'
                      f' Остаток на складе {self.items[item]}')
                return [True, item, item_capacity]

            elif item_capacity == self.items[item]:
                #  Отгружаем и закрываем позицию
                print('Нужное количество есть на складе')
                del self.items[item]
                print(f'Отгрузка товара {item} в количестве {item_capacity} проведена. Позиция закрыта')
                return [True, item, item_capacity]
            else:
                # Отгружаем остатки  и закрываем позицию
                print('Нужного количество нет отгрузили остатки')
                print(f'Отгрузка остатков товара {item} в количестве {self.items[item]} проведена. Позиция закрыта')
                temp_capacity = self.items[item]
                del self.items[item]
                return [True, item, temp_capacity]
        else:
            print(f'Товара с наименованием {item} нет на складе')
            return [False, item, 0]

    def get_free_space(self):
        return self._capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)


class Shop(Storage):
    def __init__(self,  items: dict = None, capacity: int = 20, limit: int = 5):
        if items is None:
            items = {}
        self._items = items
        self._capacity = capacity
        self._limit = limit

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        self._limit = limit

    def add(self, new_item, item_capacity):
        # Проверка на лимит в ассортименте
        if self.get_unique_items_count() < self.limit:
            #  проверка места  в магазине
            if self.get_free_space() >= item_capacity:
                if new_item in self.items.keys():
                    self.items[new_item] = self.items[new_item] + item_capacity
                else:
                    self.items[new_item] = item_capacity
                print(f'В магазин успешно помещён товар {new_item} в количестве {item_capacity}'
                      f' позиций. Осталось {self.get_free_space()} мест.')
                return [True, new_item, item_capacity]
            else:
                print(f'Магазин имеет {self.get_free_space()} свободных мест, {new_item} не может быть взят на реализацию!')
                return [False, new_item, item_capacity]
        else:
            print(f'Товар не может быть добавлен так как достигнут предел ограничения в ассортименте -'
                  f'не более ({self.limit} видов товара)')
            return [False, new_item, item_capacity]

    def remove(self, item, item_capacity):
        # Проверка наличия товара и его количества
        if item in self.items.keys():
            if item_capacity < self.items[item]:
                # Отгружаем
                self.items[item] = self.items[item] - item_capacity
                print(f'Товар {item} в количестве {item_capacity} продан.'
                      f' Остаток в магазине {self.items[item]}')
                return [True, item, item_capacity]
            elif item_capacity == self.items[item]:
                #  Продаём и закрываем позицию
                del self.items[item]
                print(f'Товар {item} в количестве {item_capacity} весь продан')
                return [True, item, item_capacity]
            else:
                # Отгружаем остатки  и закрываем позицию
                print(f'Остатки товара {item} в количестве {self.items[item]} проданы.')
                temp_capacity = self.items[item]
                del self.items[item]
                return [True, item, temp_capacity]
        else:
            print(f'Товара с наименованием {item} нет в наличии')
            return [False, item, 0]

    def get_free_space(self):
        return self._capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)


class Request:
    def __init__(self, user_input: str):
        req = user_input.split(' ')
        self.exit_point = req[4]
        self.entry_point = req[6]
        self.amount = int(req[1])
        self.product_name = req[2]

    def __repr__(self):
        return f'Доставить {self.amount} {self.product_name} из {self.exit_point} в {self.entry_point}'
