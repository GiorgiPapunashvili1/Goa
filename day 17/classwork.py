# names = ["gio", "dato", "luka", 1, 4.5]
# print(len[names])
# print(names[2])


# numbers = [10,11,12,13,14,15,16,17,18,19,20]

# numbers[0] = 1
# numbers[2] = 1
# numbers[4] = 1
# numbers[6] = 1
# numbers[8] = 1
# numbers[10] = 1
# print(numbers)

# first_name = input("input your name")
# last_name = input("input your last name")
# personal_info = [first_name, last_name]
# print(personal_info)


# name_and_lastname = input("please eneter your name and lastname: ")
# for i in range(0, len(name_and_lastname)):
#     print(name_and_lastname[i])



# name_and_lastname = input("please eneter your name and lastname: ")
# for i in range(0, len(name_and_lastname), 2):
#     print(name_and_lastname[i])

# numbers = [1,2,3,4,5,6,7,8,9,10]

# if 5 in numbers:
#     print("Yes 5 is in numbers list")
# else:
#     print("No 5 is not in numbers list")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = 0

for num in numbers:
    if num % 2 == 0:
        result = result + num

print(result)
