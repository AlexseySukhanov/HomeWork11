class Orders():
    def __init__(self, order_id, buyer, args):
        self.order_id = order_id
        self.buyer = buyer
        self.order_items = [i for i in args]

    def __str__(self):
        return f'Buyer name: {self.buyer.name} {self.buyer.surname}, delivery adress: {self.buyer.delivery_adress}, total summ: {self.get_sum()}'

    def get_sum(self):
        self.sum = 0
        for i in self.order_items:
            self.sum += i.price
        return self.sum
