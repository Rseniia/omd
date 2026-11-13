from laureates_configs import org_processor, person_processor
from json_dict_processing import read_json_file


def get_laureate_data(laureate):

    if "knownName" in laureate:
        processor = person_processor()
        result = processor(laureate)
        result["type_"] = "person"

    elif "orgName" in laureate:
        processor = org_processor()
        result = processor(laureate)
        result["type_"] = "org"

    return result


def main():

    laureates = read_json_file("laureates.json")
    laureates_data = []

    for laureate in laureates['laureates']:
        laureates_data.append(get_laureate_data(laureate))


if __name__ == "__main__":
    main()