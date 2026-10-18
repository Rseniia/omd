#Есть список заказов:
# `status` -  статус заказа
#`delivered` доставлен покупателю
#`returned` возврат
#`amount` — сумма заказа.

orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

#Нужно найти:

# на какую сумму оформили возвраты
sum_returned =  sum(x['amount'] for x in orders if x['status'] == 'returned')
print('Оформили возвраты на сумму', sum_returned)
print()

# кто хотя бы раз вернул заказ
returned_name = set()
for i in orders:
    if i['status'] == 'returned':
        returned_name.add(i['buyer'])
print(returned_name)
print()

# сколько заказов доставлено покупателю
delivered_buyer = [x['buyer'] for x in orders if  x['status'] == 'delivered']
dict_delivered_buyer = {x:delivered_buyer.count(x) for x in delivered_buyer}
print(dict_delivered_buyer)
print()

# средний чек доставленных заказов

sum_delivered =  sum(x['amount'] for x in orders if x['status'] == 'delivered')
count_delivered =  len([x['status'] for x in orders if x['status'] == 'delivered'])
print('средний чек',round(sum_delivered/count_delivered, 2))