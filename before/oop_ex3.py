class laptop:
    count_instance = 0

    def __init__(self, brand_name, model, price):
        # instance variable
        laptop.count_instance += 1
        self.brand_name = brand_name
        self.model = model
        self.price = price

    def discount(self, percentage_off):
        return self.price - self.price * (percentage_off/100)

    def full_name(self):
        return f"{self.brand_name} {self.model}"


class desktop(laptop):
    def __init__(self, brand_name, model, price, graphic_card):
        # inheritance

        # 1 method
        super().__init__(brand_name, model, price)

        # 2 method
        # laptop.__init__(self, brand_name, model, price)
        self.graphic_card = graphic_card


l1 = laptop('Lenovo', 'ideapad', 100000)
d1 = desktop('Apple', 'Mac', 130000, 'Radeon')
print(l1.full_name())
print(d1.full_name())
