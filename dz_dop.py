class Store():
    # Метод ввода названия магазина и адреса
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    # Метод добавления товара
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} был добавлен в {self.name}")

    #
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удалён из {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар {item_name} обновлена в {self.name}")
        else:
            print(f"Товар {item_name} не найден")


store1 = Store("Пятёрочка", "Ленина 40")
store2 = Store("Магнит", "Ленина 45")
store3 = Store("Дикси", "Ленина 80")

store1.add_item("Хлеб", 50)
store1.add_item("Молоко", 90)
store1.add_item("Гречка", 70)

store1.remove_item("Хлеб")

print(f"Цена на Молоко: {(store1.get_price('Молоко'))}")

store1.update_price("Гречка", 80)


