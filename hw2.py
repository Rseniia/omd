#Дана история поисковых запросов:
# каждая строка — один введённый запрос.
# Повтор в списке значит, что этот запрос ввели ещё раз.

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

#Нужно найти:

#сколько всего поисковых запросов в ленте

print(len(queries))
print()

#сколько раз ввели каждый запрос

uniq = list(set(queries)) # содержит только уникальные запросы
for i in range(len(uniq)):
    print('запрос', uniq[i], 'ввели', queries.count(uniq[i]))
print()
#другой метод через словарь

dict_queries = {x: queries.count(x) for x in queries}
print(dict_queries)
print()

#какой запрос вводили чаще всего

print(max(dict_queries, key=dict_queries.get))
print()

#другой метод через for

m = max(dict_queries.values())
for i in range(len(uniq)):
    if dict_queries[uniq[i]] == m: #dict_queries[uniq[i]] возвращает значение словаря по ключу
        print(uniq[i])
        m_key = uniq[i]
print()
#какую долю всех поисков он занимает

print(m_key, 'занимает cледующую долю', round(m/sum(dict_queries.values())*100,2), '%') #можно делить на len(queries)
print()

#какие запросы встретились один раз

for i in range(len(uniq)):
    if dict_queries[uniq[i]] == 1: #dict_queries[uniq[i]] возвращает значение словаря по ключу
        print(uniq[i])