names = ["gurami", "giorgi", "luka", "davit"]
index = int(input("please input an index: "))

for i in range(len(names)):
    length = len(names)
    if i == index:
        print(names[i])