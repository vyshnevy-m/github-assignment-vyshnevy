#sum of numbers until the sum is greater than 100#
s = 0

while True:
    s += int(input())

    if s > 100:
        break

print(s)