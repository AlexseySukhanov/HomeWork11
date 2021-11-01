class TradeItem:
    def __init__(self, item_id, item_name, description, price, length, height, depth, weight):
        if not isinstance(price, (int,float)):
            raise TypeError(f'{type(price).__name__} priсe is not valid')
        if price <= 0:
            raise ValueError("Price can't be less or equal to zero")

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