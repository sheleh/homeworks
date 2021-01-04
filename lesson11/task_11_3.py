
class Product:

    def __init__(self, type_of, name, price):
        self.type = type_of
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.type} / {self.name} / {self.price}'

    def __repr__(self):
        return f'{self.type} / {self.name} / {self.price}'


class ProductStore:

    def __init__(self):
        self.store = []
        self.income = 0

    def add(self, item, amount):
        if isinstance(item, Product):
            self.item = item
            self.amount = amount
            self.item.price *= 0.3
            self.store.append([self.item, self.amount])
        else:
            raise Exception('Wrong Product!!!')

    def set_discount(self, identifier, percent, identifier_type = 'name'):
        self.identifier = identifier
        self.percent = int(percent)
        self. identifier_type = identifier_type
        for item in self.store:
            if self.identifier_type == 'name':
                if self.identifier in item[0].name:
                    item[0].price -= (item[0].price * (self.percent/100))
                    return item[0].price
            elif self.identifier_type == 'type':
                if self.identifier in item[0].type:
                    item[0].price -= (item[0].price * (self.percent/100))
                    return item[0].price
        else:
            raise Exception(f'{self.identifier} not found')

    def sell_product(self, product_name, amount_sell):
        self.product_name = product_name
        self.amount_sell = int(amount_sell)
        for item in self.store:
            if self.product_name in item[0].name:
                item[1] -= self.amount_sell
                self.income += (item[0].price * self.amount_sell)
                return self.income
        else:
            raise Exception(f'{self.product_name} not found')

    def get_income(self):
        return f' Income is = {self.income}'

    def get_all_products(self):
        for item in self.store:
            return item[0].type, item[0].name, item[0].price, item[1]

    def get_product_info(self, product_name):
        self.product_name = product_name
        for item in self.store:
            if item[0].name in self.product_name:
                return f'{item[0].name} = {item[1]} pieces in store'
        else:
            raise Exception(f'{self.product_name} not found')


p = Product('sport', 'Football T-shirt', 100)
p2 = Product("Food", 'Ramen', 5)
p3 = Product('Health', 'BCAA', 30)
p4 = Product('Health', 'Protein', 20)
s = ProductStore()
s.add(p, 1000)
s.add(p2,345)
s.add(p3,100)
s.add(p4,200)

#print(s.store)
s.sell_product('Ramen', 1)
s.sell_product('BCAA', 2)
#print(f'INCOME = {s.income}')
#print(s.store)
s.get_income()
s.get_all_products()
#print(s.get_product_info('Ramen'))
s.set_discount('Health',10,'type')
s.get_all_products()

