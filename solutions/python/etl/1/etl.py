def transform(legacy_data):
    new = {}
    for value in legacy_data:
        for key in legacy_data.get(value):
            lower_key = key.lower()
            new[lower_key] = value
    sorted_dict_by_key = dict(sorted(new.items()))
    return sorted_dict_by_key