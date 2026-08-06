#multiplication using *=#
num = int(input("Enter a number: "))
times = int(input("Enter how many times: "))

result = 1

for i in range(times):
    result *= num

print("Result =", result)