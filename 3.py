#average of numbers#
n = int(input("Enter how many numbers: "))

total = 0

for i in range(n):
    num = int(input("Enter number: "))
    total += num

average = total / n

print("Average =", average)