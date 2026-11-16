import dataset_helpers
import aggregations as agg


def unpack_prizes(data):
    prizes_data = []

    for laureate in data:
        for prize in laureate["prizes_relevant"]:
            new_record = laureate.copy()
            new_record.update(prize)
            del new_record["prizes_relevant"]
            prizes_data.append(new_record)

    return prizes_data


def get_multiple_laureates(data):
    groups = dataset_helpers.group_data(data, ["id"])
    result = []

    for laureate_id, records in groups.items():
        if len(records) > 1:
            prizes = sorted(records, key=lambda x: x["award_year"])
            categories = agg.count(prizes, "category_en")

            result.append({
                "id": laureate_id[0],
                "name": prizes[0]["name"],
                "type_": prizes[0]["type_"],
                "prizes_count": len(prizes),
                "prizes": prizes,
                "same_category": len(categories) == 1,
                "years_between":
                    prizes[1]["award_year"] - prizes[0]["award_year"]
            })

    return result



