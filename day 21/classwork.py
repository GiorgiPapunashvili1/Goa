word = "luka"

for i in range(len(word), -1, -1 -1):
    print(i)




words_list = []

for i in range(5):
    word = input("Please enter word: ")
    words_list.append(word)

result = ""

for word in words_list:
    result += word[0]

print(result)





word = "ana"
reversed_word = ""

for index in range(len(word) - 1, -1, -1):
    reversed_word = reversed_word + word[index]

if word == reversed_word:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")

    