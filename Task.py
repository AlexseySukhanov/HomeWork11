class trade_item():
    def __init__(self,item_id,item_name,description,price,length,height,depth,weight):
        self.item_id=item_id
        self.item_name=item_name
        self.description=description
        self.price=price
        self.length=length
        self.height=height
        self.depth=depth
        self.weight=weight
    def get_info(self):
        return f'{self.item_name} {self.description} {self.price}'

class buyers():
    def __init__(self,buyer_id,name,surname,phone,delivery_adress):
        self.buyer_id=buyer_id
        self.name=name
        self.surname=surname
        self.phone=phone
        self.delivery_adress=delivery_adress
    def get_info(self):
        return f'{self.name} {self.surname} {self.phone} {self.delivery_adress}'

class orders():
    def __init__(self,order_id,buyer,args):
        self.order_id=order_id
        self.buyer=buyer
        self.order_items=[i for i in args]
    def __str__(self):
        return f'Buyer name: {self.buyer.name} {self.buyer.surname}, delivery adress: {self.buyer.delivery_adress}, total summ: {self.get_sum()}'
    def get_sum(self):
        self.sum=0
        for i in self.order_items:
            self.sum+=i.price
        return self.sum


# добавляем позиции товаров
item=[]
item.append(trade_item(1,"BRAUN Series 5 50-W1500s BLACK",
                 "Электробритва с тремя плавающими лезвиями, которые подстраиваются под контуры вашего лица для гладкого и легкого бритья",
                 2499,25.2,13.7,6.7,0.42))
item.append(trade_item(2,"TEFAL OptiGrill + Initial GC706",
                 "Электрогриль TEFAL КАЖДЫЙ РАЗ ИДЕАЛЬНЫЙ РЕЗУЛЬТАТ ПРОЖАРКИ СТЕЙКА: ОТ RARE ДО WELL-DONE",
                 4699,22.9,39.9,36.9,5.87))
# добавляем покупателя
buyer=[]
buyer.append(buyers(1,"Thomas","Anderson","+380503127023","ave. Bright future 1"))

#добавляем позиции товаров в заказанные позиции
ordered_items=[]
ordered_items.append(item[0])
ordered_items.append(item[1])


#формируем заказ
order=[]
order.append(orders(1,buyer[0],ordered_items))


print(order[0])











