class TradeItem():
    def __init__(self, item_id, item_name, description, price, length, height, depth, weight):
        self.item_id = item_id
        self.item_name = item_name
        self.description = description
        self.price = price
        self.length = length
        self.height = height
        self.depth = depth
        self.weight = weight

    def get_info(self):
        return f'{self.item_name} {self.description} {self.price}'