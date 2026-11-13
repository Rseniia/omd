from json_dict_processing import create_processor
from prizes_configs import prize_processor


def process_year(year_string):

    if year_string is None:
        return None

    return int(year_string[:4])


CONFIG_PERSON = {
    "id": ["id"],
    "name": ["knownName", "en"],
    "gender": ["gender"],
    "birth_year": (["birth", "date"], process_year),
    "country_birth": ["birth", "place", "country", "en"],
    "country_now": ["birth", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor())
}


CONFIG_ORG = {
    "id": ["id"],
    "name": ["orgName", "en"],
    "founded_year": (["founded", "date"], process_year),
    "country_founded": ["founded", "place", "country", "en"],
    "country_now": ["founded", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor())
}


def person_processor():
    return create_processor(CONFIG_PERSON)


def org_processor():
    return create_processor(CONFIG_ORG)

"""
def main():
    pass


if __name__ == "__main__":
    main()
"""




