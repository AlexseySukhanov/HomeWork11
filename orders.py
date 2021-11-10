class Orders:
    def __init__(self, order_id, buyer, order_items):
        self.order_id = order_id
        self.buyer = buyer
        self.order_items = order_items

    def __str__(self):
        return f'Buyer name: {self.buyer.name} {self.buyer.surname},\ndelivery adress: {self.buyer.delivery_adress},\n{[i.item_name for i in self.order_items]}\ntotal summ: {self.get_sum()}'

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.order_items):
            self.index += 1
            return self.order_items[self.index-1]
        else:
            raise StopIteration

    def __getitem__(self, item):
        if isinstance(item , slice):
            if item.start < 0 or item.stop > len(self.order_items):
                raise IndexError
            else:
                result = []
                start = 0 if item.start == None else item.start
                stop = len(self.order_items)-1 if item.stop == None else item.stop
                step = 1 if item.step == None else item.step
                for i in range(start, stop ,step):
                    result.append(self.order_items[i])
                return result

    def get_sum(self):
        self.sum = 0
        for i in self.order_items:
            self.sum += i.price
        return self.sum
