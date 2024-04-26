# #ამოცანა 1
# #  შექმენით პროგრამა, რომელსაც გადასცემთ სიას, სადაც გექნებათ მთელი რიცხვები.
# # თქვენი დავალებაა, რომ ამ სიის ორი მინიმალური რიცხვის ჯამი დააბრუნოთ:
# # ([5, 8, 12, 18, 22]), 13), ([7, 15, 12, 18, 22]), 19), ([25, 42, 12, 18, 22]), 30)

# # list = [ 15, 25, 3, 27, 2]

# # for i in list:
# #     lowest = list[0]
# #     if i < lowest:
# #         lowest = i
# # for j in list:
# #     second_lowest = list[0]
# #     if j < second_lowest and j > lowest:
# #         second_lowest = j 
# #         break


# # print(lowest + second_lowest)  






# #ამოცანა 2
# #  შექმენით პროგრამა რომელსაც გადასცემთ მთელი რიცხვების სიას.
# # შემდეგ უნდა მოახდინოთ გაფილტვრა:
# # ახალ სიაში გადაიტანოთ მარტო ლუწი რიცხვები. ბოლოს კი დააბრუნოთ ახალი სია.
# # test cases: 
# list2 = [1, 2, 3, 4]
# list2Even = []

# for i in list2:
#     if i % 2 == 0:
#         list2Even.append(i)
# print(list2Even)


# #ამოცანა 3
# # შექმენით პროგრამა, სადაც გადმოგეცემათ სიები და თქვენ მოახდენთ ფილტრაციას. 
# # თუ პირველ და მეორე სიაში ერთი და იგივე ინდექსზე მყოფი ელემენტი იგივე იქნება,
# # მთვლელს დაამატეთ 4 ქულა. თუ რომელიმე ელემენტი იქნება "" - ანუ ცარიელი სთრინგი,
# # მთვლელი არ შეცვალოთ. ხოლო თუ გექნებათ განსხვავებული ელემენტები,
# # მთვლელს გამოაკელით ერთი ქულა. იმუშავეთ შემდეგ სიებზე:

# # list1 = ["a", "a", "b", "b"], ["a", "c", "b", "d"]
# # list2 = ["a", "a", "c", "b"], ["a", "a", "b",  ""]
# # list3 = ["a", "a", "b", "c"], ["a", "a", "b", "c"]
# # list4 = ["b", "c", "b", "a"], ["",  "a", "a", "c"]

# # for i in list1:
# #     if i == i




# #ამოცანა 4
# #  შექმენით პროგრამა, სადაც მოახდენთ სიაზე მუშაობას. თქვენ გადმოგეცემათ ერთი სია,
# # დავალება კი შემდეგია: უნდა დაითვალოთ ლუწ ინდექსებზე მყოფი რიცხვების ჯამი,
# # ასევე კენტ ინდექსებზე მყოფი რიცხვების ჯამი.
# # საბოლოოდ ორივე დაამატოთ ახალ სიაში და დააბრუნოთ ეს სია. გამოიყენეთ შემდეგი სიები:

# list1 = [80]
# updated_list1 = []
# even_sum = 0
# odd_sum = 0

# for num in list1:
#     if num % 2 == 0:
#         even_sum = even_sum + num
#         updated_list1.append(num)


# for i in list1:
#     if i % 2 != 0:
#         odd_sum = odd_sum + i
#         updated_list1.append(i)

# print(updated_list1)
        


     






# list2 = [100,50]
# list3 = [50,60,70,80]
# list4 = [13,27,49]
# list5 = [70,58,75,34,91]


#მასწავლებლისგან

number_list = [1, 2, 3, 4]
even_numbers = []

for number in number_list:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


a = ["b", "c", "b", "a"]
b = ["",  "a", "a", "c"]

score = 0

for index in range(len(a)):
    if a[index] == b[index]:
        score = score + 4
    elif a[index] == "" or b[index] == "":
        score = score + 0
    else:
        score = score - 1

print(score)