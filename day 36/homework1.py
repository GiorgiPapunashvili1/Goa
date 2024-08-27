def manual_reverse(collection):
    reversed_collection = []
    for i in range(len(collection) - 1, -1, -1):
        reversed_collection.append(collection[i])
    return reversed_collection
