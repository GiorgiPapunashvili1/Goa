def manual_replace(collection, old_value, new_value):
    replaced_collection = []
    for item in collection:
        if item == old_value:
            replaced_collection.append(new_value)
        else:
            replaced_collection.append(item)
    return replaced_collection
