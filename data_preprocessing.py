def find_none(data):
    for laureate in data:
        for value in laureate.values():
            if value is None:
                return True
    return False


def count_all(data) -> dict[str, int]:
    dict_all = {}
    for laureate in data:
        for key, value in laureate.items():
            dict_all[key] = dict_all.get(key, 0) + 1
    return dict_all


def count_none(data) -> dict[str, int]:
    dict_none = {}
    for laureate in data:
        for key, value in laureate.items():
            dict_none[key] = (dict_none.get(key, 0) + (value is None))
    return dict_none


def proportion_none(dict_none, dict_all) -> dict[str, int]:
    proportion = {}
    for key, value in dict_all.items():
        proportion[key] = round(dict_none[key] / dict_all[key], 3)
    return proportion


def max_value(data, value, linked_value):
    maximum = max(data, key=lambda x: int(x[value]))

    result = {
        value: maximum[value]
    }

    if linked_value in maximum:
        result[linked_value] = maximum[linked_value]
    else:
        result[linked_value] = [
            prize.get(linked_value)
            for prize in maximum["prizes_relevant"]
        ]

    return result


def min_value(data, value, linked_value):
    minimum = min(data, key=lambda x: int(x[value]))

    result = {
        value: minimum[value]
    }

    if linked_value in minimum:
        result[linked_value] = minimum[linked_value]
    else:
        result[linked_value] = [
            prize.get(linked_value)
            for prize in minimum["prizes_relevant"]
        ]

    return result


def repeat_id(data):
    list_of_value = [int(laureate["id"]) for laureate in data]
    has_repeat = len(list_of_value) != len(set(list_of_value))
    return has_repeat


def difference_couple_id(data):
    list_of_id = [int(laureate["id"]) for laureate in data]
    sorted_list_of_id = sorted(list_of_id)
    id_gaps = []

    for i in range(len(sorted_list_of_id) - 1):
        if sorted_list_of_id[i + 1] - sorted_list_of_id[i] > 1:
            id_gaps.append((sorted_list_of_id[i], sorted_list_of_id[i + 1]))

    return id_gaps
