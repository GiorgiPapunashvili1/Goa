def manual_index(numbers_list,search_value):
    for i in range(len(numbers_list)):
        if numbers_list[i] == search_value:
            return i
        if search_value not in numbers_list:
            return -1
print(manual_index([1,2,3,3,4,5], 6))
