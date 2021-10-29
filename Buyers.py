class Buyers():
    def __init__(self, buyer_id, name, surname, phone, delivery_adress):
        self.buyer_id = buyer_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.delivery_adress = delivery_adress

    def get_info(self):
        return f'{self.name} {self.surname} {self.phone} {self.delivery_adress}'
