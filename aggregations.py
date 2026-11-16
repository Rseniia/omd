import statistics as stat


def max_value(data, key):
    valid_data = [int(x[key]) for x in data if x.get(key) is not None]
    return max(valid_data) if valid_data else None


def min_value(data, key):
    valid_data = [int(x[key]) for x in data if x.get(key) is not None]
    return min(valid_data) if valid_data else None


def mean_value(data, key):
    values = [x[key] for x in data if x.get(key) is not None]
    return stat.mean(values) if values else None


def median_value(data, key):
    values = [x[key] for x in data if x.get(key) is not None]
    return stat.median(values) if values else None


def top_n(data, key, n):
    collection = []
    dictionary = count(data, key=key)

    sort = sorted(
        dictionary.items(),
        key=lambda x: x[1],
        reverse=True
    )
    if n > len(sort):
        print("ВНИМАНИЕ ВЫВЕДЕТСЯ ТОЛЬКО ТОП", len(sort))
    for x in range(min(n, len(sort))):
        collection.append(sort[x])
    return collection


def count(data, key):
    dictionary = {
        x[key]: sum(item[key] == x[key] for item in data)
        for x in data
    }
    return dictionary


def add_interval(data, key, interval=10):
    for record in data:
        if record[key] is not None:
            record[key + "_interval"] \
                = record[key] // interval * interval

    return data



