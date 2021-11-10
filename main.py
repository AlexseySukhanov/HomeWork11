from tradeitem import TradeItem
from buyers import Buyers
from orders import Orders

item = []
item.append(TradeItem(1, "BRAUN Series 5 50-W1500s BLACK",
                      "Электробритва с тремя плавающими лезвиями, которые подстраиваются под контуры вашего лица для гладкого и легкого бритья",
                      2499, 25.2, 13.7, 6.7, 0.42))
item.append(TradeItem(2, "TEFAL OptiGrill + Initial GC706",
                      "Электрогриль TEFAL КАЖДЫЙ РАЗ ИДЕАЛЬНЫЙ РЕЗУЛЬТАТ ПРОЖАРКИ СТЕЙКА: ОТ RARE ДО WELL-DONE",
                      4699, 22.9, 39.9, 36.9, 5.87))

# добавляем покупателя
buyer = []
buyer.append(Buyers(1, "thomas", "anderson", "+380503127023", "ave. Bright future 1"))

# добавляем позиции товаров в заказанные позиции
ordered_items = []
ordered_items.append(item[0])
ordered_items.append(item[1])

# формируем заказ

order = Orders(1, buyer[0], ordered_items)

print(order)

for i in order:
    print(i)


