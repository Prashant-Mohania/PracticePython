class laptop:
    def __init__(self, brand_name, model, price):
        # instance variable
        self.brand_name = brand_name
        self.model = model
        self.price = price


l1 = laptop('Lenovo', 'ideapad', 47999)
print(l1)
