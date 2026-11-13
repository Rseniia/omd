
import json


def read_json_file(json_file):

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

        return data


def extract_nested_value(obj, keys):

    for key in keys:
        if not isinstance(obj, dict) or obj.get(key) is None:
            return None
        obj = obj.get(key)

    return obj


def process_dictionary_with_config(dictionary, config):
    new_dict = {k: None for k in config}
    for key in new_dict.keys():
        if isinstance(config[key], tuple):
            path, func = config[key]
            value = extract_nested_value(dictionary, path)
            new_dict[key] = func(value)
        else:
            new_dict[key] = extract_nested_value(dictionary, config[key])

    return new_dict


def process_list_of_dicts_with_config(list_of_dicts, config):
    new_list_of_dicts = []

    for i in list_of_dicts:
        new_list_of_dicts.append(process_dictionary_with_config(i, config))

    return new_list_of_dicts


def create_processor(config, list_processor=False):

    def processor(obj):
        if list_processor:
            return process_list_of_dicts_with_config(obj, config)
        else:
            return process_dictionary_with_config(obj, config)

    return processor



"""
def main():

    pass
if __name__ == "__main__":
    main()
"""

