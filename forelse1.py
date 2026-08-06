#search using for else#
a = [10, 20, 30, 40]
n = int(input())

for i in range(len(a)):
    if a[i] == n:
        print(i)
        break
else:
    print("Item Not Found")