def manual_count(collection, value_to_count):
    count = 0
    for item in collection:
        if item == value_to_count:
            count += 1
    return count
