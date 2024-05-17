#დავალება 1
# word = "VaNo MoTiashvili"
# reversed_word = word[::-1]
# reversed_uppercase = reversed_word.upper()
# print(reversed_uppercase)

#დავალება 2
# def categorize_strings(strings):
#     odd = []
#     even = []
#     for string in strings:
#         if len(string) % 2 == 0:
#             even.append(string.upper())
#         else:
#             odd.append(string.upper())
#     return f'odds: {odd}  evens:  {even}]' 

# print(categorize_strings(["vano" , "davit" , "zuka" , "yiyliyo"]))  
     
#დავალება 3
# def odd_and_even_strings(strings):
#     result = []
#     for string in strings:
#         if len(string) % 2 == 0:
#             result.append(string.upper())
#         else:
#             result.append(string.capitaliz())
#     return f'result: {result}]' 

# print(odd_and_even_strings(["goa_best" , "vano" , "nesvi" , "tskhVarAdzE"]))

#დავალება 4
# def transform_case(input_list):
#     transformed_list = []
#     for item in input_list:
#         if item.isupper():
#             transformed_list.append(item.lower())
#         else:
#             transformed_list.append(item.upper())
#     return transformed_list

# result = transform_case(["vano", "DAVIT", "LUKA", "nika"])
# print(f'result: {result}')

#დავალება 5
# def process_string(string, to_find):
#     amount = string.find(to_find)
#     if amount % 2 == 0:
#         res = string.upper()
#     elif amount % 2 != 0:
#         res = string.capitalize()
#     return res        

# print(process_string("vano motishvili", "m"))