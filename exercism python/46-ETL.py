def transform(legacy_data):
    result = {}
    for map in legacy_data:
        for letter in legacy_data[map]:
            low_letter = letter.lower()
            result[low_letter] = map
    return result