#armstrong#
n = int(input())
o = n
s = 0

while n > 0:
    d = n % 10
    s += d ** 3
    n //= 10

if o == s:
    print("Armstrong")
else:
    print("Not Armstrong")