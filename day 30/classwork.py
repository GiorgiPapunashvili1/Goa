def sum_of_evens(numbers_list):
    sum = 0
    for index in range(len(numbers_list)):
        if index % 2 == 0:
            sum += numbers_list[index]
    return sum

print(sum_of_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def check_int(num):
    if num % 2 == 0:
        return str(num) + " is Even"
    else:
        return str(num) + " is Odd"


print(check_int(6))