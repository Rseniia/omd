#Есть список отзывов на товары.
# На каждой строке — по одному.
# Данные слегка битые, и названия товара записаны в разном регистре.
# `id` при этом один и тот же для одного и того же товара.
# Перед подсчётом приведите названия к одному формату,
# иначе они будут считаться как разные`.

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

#Нужно найти:

#переводим в нижний регистор продукты
for i in reviews:
    i['product'] = i['product'].lower()

# среднюю оценку каждого товара
product_with_stars = []
unique_products = list(set(x['product'] for x in reviews))
for product in unique_products:
    total_stars = sum(1 for x in reviews if x['product'] == product)
    total_sum = sum(x['stars'] for x in reviews
                    if x['product'] == product)
    product_with_stars.append({'product': product,
                          'count': total_stars, 'sum': total_sum,
                          'average': total_sum/total_stars})
print('среднюю оценку каждого товара', {x['product']:
                        x['average'] for x in product_with_stars})
print()

# худший товар по средней оценке среди тех, у кого хотя бы два отзыва
min_average = float('inf')
badly_product = None
for i in product_with_stars:
    if i['count'] >= 2 and i['average'] <= min_average:
        min_average = i['average']
        badly_product = i['product']
print('худший товар по средней оценке', badly_product)
print()

# сколько отзывов на 1 или 2 звезды
count_stars = sum(1 for x in reviews if x['stars'] in [1, 2])
print('отзывов на 1 или 2 звезды составляет', count_stars)
print()

# какую долю всех отзывов они составляют
print('отзывы на 1, 2 звезды составляют '
      'следующую долю от всех отзывов', count_stars/ len(reviews))

