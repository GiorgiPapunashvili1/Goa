# name = "giorgi"
# print(name[0:3])

# list = [1,2,3,4,5,6]
# print(list[4:6])

numbers = []

start = 5
end = -1
step = -1

while start > end:
    numbers.append(start)
    start = start + step

print(numbers)



list = [1,2,3,4,5,6,7]
reversed_list = []

for num in list(len(list), -1, -1):
    reversed_list.append(i)