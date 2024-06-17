def numbers(start, end):
    for i in range(start, end):
        print(i)


numbers(1,3)
numbers(2, 5)


def calculate_sum(start, end):
    result = 0
    for i in range(start, end):
        result = result + i
    print(result)


calculate_sum(2,5)


def calculate_arithmetic(start, end):
    numbers = []

    for i in range(start, end):
        numbers.append(i)
    
    result = sum(numbers) / len(numbers)

    print(result)

calculate_arithmetic(5, 11)



def print_char(name, index):
    print(name[index])

print_char("Luka", 3)