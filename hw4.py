#Есть статистика за пять дней работы магазина.
# У каждого дня число заказов, выручка и число возвратов.


days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]


#Нужно найти:

# выручку за всю неделю

sum_revenue =  sum(x['revenue'] for x in days)
print('Выручку за всю неделю',sum_revenue)
print()

# день с самой большой выручкой

#если бы задача была про дни с самой большой выручкой,
# то решалось бы чуть-чуть по другому

max_revenue = days[0]['revenue']
day = days[0]['day']
for i in days:
    if i['revenue'] > max_revenue:
        max_revenue = i['revenue']
        day = i['day']
print('день с самой большой выручкой', day)
print()

# среднюю выручку на один заказ в каждый день

# из предположения, что возвращенные заказы входят в заказы

average_revenue = {x['day']: x['revenue']/x['orders'] for x in days}
print(average_revenue)
print()

# дни, где возвратов больше 20% заказов

days_returned_20 = [x['day'] for x in days if x['returns']/x['orders'] > 0.2]
print(days_returned_20)
