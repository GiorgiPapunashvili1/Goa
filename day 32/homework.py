def manual_index(numbers_list, search_value):
    # გადის სიას და აბრუნებს ინდექსს თუ პოულობს საძიებელი მნიშვნელობას
    for index, value in enumerate(numbers_list):
        if value == search_value:
            return index
    # თუ მნიშვნელობა არ მოიძებნა, აბრუნებს -1
    return -1

# მაგალითი გამოყენების:
numbers = [10, 20, 30, 40, 50]
value_to_find = 30
index = manual_index(numbers, value_to_find)
print(f"Index of {value_to_find} is: {index}")


def manual_max(numbers_list):
    # თუ სია ცარიელია, აბრუნებს None
    if not numbers_list:
        return None
    
    # ითვალისწინებს პირველი ელემენტი როგორც მაქსიმუმი
    max_value = numbers_list[0]
    
    # გადის ყველა ელემენტს და პოულობს მაქსიმუმს
    for number in numbers_list[1:]:
        if number > max_value:
            max_value = number
    
    return max_value

def manual_min(numbers_list):
    # თუ სია ცარიელია, აბრუნებს None
    if not numbers_list:
        return None
    
    # ითვალისწინებს პირველი ელემენტი როგორც მინიმუმი
    min_value = numbers_list[0]
    
    # გადის ყველა ელემენტს და პოულობს მინიმუმს
    for number in numbers_list[1:]:
        if number < min_value:
            min_value = number
    
    return min_value

# მაგალითი გამოყენების:
numbers = [10, 20, 30, 40, 50]
max_value = manual_max(numbers)
min_value = manual_min(numbers)
print(f"Maximum value is: {max_value}")
print(f"Minimum value is: {min_value}")
#ამაზე მოკლედ ვერ დავწერე


def manual_pop(numbers_list, index):
    # თუ ინდექსი არ არის სწორ დიაპაზონში, აბრუნებს ორიგინალ სიას
    if index < 0 or index >= len(numbers_list):
        return numbers_list
    
    # ქმნის ახალ სიას, რომელიც შეიცავს ყველა ელემენტს გარდა წასაშლელისა
    new_list = []
    for i in range(len(numbers_list)):
        if i != index:
            new_list.append(numbers_list[i])
    
    return new_list

# მაგალითი გამოყენების:
numbers = [10, 20, 30, 40, 50]
index_to_remove = 2
new_numbers = manual_pop(numbers, index_to_remove)
print(f"New list after removing index {index_to_remove}: {new_numbers}")
