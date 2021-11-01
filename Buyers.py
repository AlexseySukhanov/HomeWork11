class Buyers:
    def __init__(self, buyer_id, name, surname, phone, delivery_adress):
        if not isinstance(name, str):
            raise TypeError(f'{type(name).__name__} Name is not valid')
        if not isinstance(surname, str):
            raise TypeError(f'{type(surname).__name__} Surname is not valid')

        self.buyer_id = buyer_id
        self.name = name.title()
        self.surname = surname.title()
        self.phone = phone
        self.delivery_adress = delivery_adress

    def get_info(self):
        return f'{self.name} {self.surname} {self.phone} {self.delivery_adress}'
