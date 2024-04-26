# #1 დავალება:მომხმარებელს შემოატანინეთ სიტყვა და შეამოწმეთ არის თუ არა ის პალინდრომი.
# #პალინდრომი არის სიტყვა, რომელიც შებრუნებულიც ზუსტად იგივე გამოდის - radar, level, rotor.
# #ამ დავალებისთვის გამოიყენეთ ციკლი და indexing.

# txt = input("input a word: ")
# txt_reversed = txt[::-1]
# if txt == txt_reversed:
#     print("your word is a palindrome")
# else:
#     print("your word is not a palindrome")


# 2. მომხმარებელს შემოატანინეთ ხუთი რიცხვი და შეიტანეთ ისინი სიაში. შემდეგ თქვენ უნდა იმუშაოთ ამ სიაზე:
# თუ რომელიმე ელემენტი სიაში ორჯერ მეორდება, დაამატეთ ის ახალ სიაში. საბოლოოდ გექნებათ ორი ვარიანტი:
# ცარიელი ახალი სია / ახალი სია სადაც იქნება მინიმუმ ერთი ელემენტი. თუ სია ცარიელი იქნება,
# დაბეჭდეთ რომ სია ცარიელია. სხვა შემთხვევაში დაბეჭდეთ ახალი სია.


# original_list = []

# for i in range(5):
#     num = int(input("input a number: "))
#     original_list.append(num)

# new_list = []
# for num in original_list:
#     if original_list.count(num) > 1 and num not in new_list:
#         new_list.append(num)

# if len(new_list) == 0:
#     print("list is empty")
# else:
#     print("new list: ", new_list)


#3.მომხმარებელს შემოატანინეთ ხუთი სიტყვა. თქვენი დავალებაა,
# რომ ააწყოთ ახალი სიტყვა - თითოეულის პირველი ასო დაამატოთ მას. საბოლოოდ კი დაბეჭდოთ ეს სიტყვა.

# word1 = input("input a random word: ")
# word2 = input("input a random word: ")
# word3 = input("input a random word: ")
# word4 = input("input a random word: ")
# word5 = input("input a random word: ")

# list = [word1, word2, word3, word4, word5]

# print(word1[0], word2[0], word3[0], word4[0], word5[0])


#4.პირველ სიაში დაამატეთ 10-იდან 20-ის ჩათვლით არსებული ყველა მთელი რიცხვი.
#მეორე სიაში კი 30-იდან 50-ის ჩათვლით ყველა 5-ის ჯერადი. საბოლოოდ შეაერთეთ ეს ორი სია და დაბეჭდეთ ამ სახით.

# list1 = [10,11,12,13,14,15,16,17,18,19,20]
# list2 = [30,35,40,45,50]

# #სიების შედარება როგორ გავაკეტო არ ვიცი და უბრალოდ დავპრინტავ

# print(list1 + list2)