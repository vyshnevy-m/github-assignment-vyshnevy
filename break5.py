#print float values#
a = [1.2, 2.5, 3.8, "Hi", 4.6]

for i in a:
    if type(i) == str:
        break
    print(i)