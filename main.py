from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items):
        self._items = items
        self.capacity = 1000

    def add(self, name, quantity):
        self._items[name] += int(quantity)

    def remove(self, name, quantity):
        self._items[name] -= int(quantity)

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        unique_items = {}
        for k, v in self._items.items():
            if k in unique_items:
                unique_items[k] += v
            else:
                unique_items.update(k, v)
        return unique_items


class Store(Storage):
    def __init__(self, items):
        super().__init__(items)
        self._items = items
        self.capacity = 100


class Shop(Storage):
    def __init__(self, items):
        super().__init__(items)
        self._items = items
        self.capacity = 20


class Request:
    def __init__(self, request_str):
        self.request_str = request_str

    def request_obj(self):
        data = self.request_str.split()
        return [data[2], data[1], data[4], data[6]]


def main(data):
    if data[2] == "склад" and data[3] == "магазин":
        for k, v in store.get_items().items():
            if k == data[0] and v >= int(data[1]):

                print("Нужное количество есть")
            elif k == data[0] and v < int(data[1]):
                return (f"На {data[2]} нет столько")
        if int(data[1]) <= int(shop.get_free_space()):
            shop.add(data[0], data[1])
            store.remove(data[0], data[1])
            print(f"Курьер забрал {data[1]} {data[0]} из {data[2]}")
            print(f"Курьер везет {data[1]} {data[0]} в {data[3]}")
            print(f"Курьер доставил {data[1]} {data[0]} в {data[3]}")
        else:
            print(f"В {data[3]} недостаточно места")
    else:
        print(f"Не определо место")


if __name__ == '__main__':
    request_str = str(input())
    request = Request(request_str)
    store_now = {"печеньки": 10, "собачки": 10, "коробки": 10}
    store = Store(store_now)
    shop = Shop(items={"печеньки": 2, "собачки": 2})
    movement = request.request_obj()
    main(movement)
    print(f"\nВ {movement[2]} хранится \n {store.get_items()}")
    print(f"\nВ {movement[3]} хранится \n {shop.get_items()}")
