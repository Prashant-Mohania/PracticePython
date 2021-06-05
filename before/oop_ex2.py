class laptop:
    def __init__(self, brand_name, model, price):
        # instance variable
        self.brand_name = brand_name
        self.model = model
        self.price = price

    def discount(self, percentage_off):
        return self.price - self.price * (percentage_off/100)


l1 = laptop('Lenovo', 'ideapad', 100000)
print(l1.discount(10))
