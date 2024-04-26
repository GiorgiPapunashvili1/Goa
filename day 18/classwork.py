names = ["Nika", "Luka", "Gabrieli", "Dato", "Mate"]

for i in names:
    print(i)


numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        print(number)



numbers = [1,2,3,4,5,6,7,8,9,10]

sum = 0
multiple = 1

for num in numbers:
    sum = sum + num
    multiple = multiple * num

print(numbers,"sum of these numbers is",sum)
print(numbers, "multiple of these numbers is", multiple)





numbers = [1,2,3,4,5,6,7,8,9,10]

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num
        print(num)

print(even_sum)


numbers = [1,2,3,4,5,6,7,8,9,10]

odd_sum = 0
odd_multiple = 1

for num in numbers:
    if num % 2 != 0:
        odd_sum = odd_sum + num
        odd_multiple = odd_multiple * num

print("Odd numbers sum", odd_sum)
print("Odd numbers multiple", odd_multiple)


name = "Luka"

for char in name:
    print(char) 


    name = "Giorgi"
even_indexes_string = ''
        #  0 1 2 3 4 5
for i in range(0, len(name)):
    if i % 2 == 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)