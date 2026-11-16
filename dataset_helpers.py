import aggregations as agg


def filter_data(data, value, condition):
    where_data = []
    for item in data:
        if condition(item[value]):
            where_data.append(item)
    return where_data


def group_data(data, group):
    dict_group = {}
    for item in data:
        group_key = tuple(item[x] for x in group)
        if group_key not in dict_group:
            dict_group[group_key] = []
        dict_group[group_key].append(item)
    return dict_group


def apply_aggregations(data, key, aggregations):

    functions = {
        "mean": agg.mean_value,
        "median": agg.median_value,
        "max": agg.max_value,
        "min": agg.min_value,
        "count": agg.count
    }

    result = {}

    for name in aggregations:
        result[name] = functions[name](data, key)

    return result
