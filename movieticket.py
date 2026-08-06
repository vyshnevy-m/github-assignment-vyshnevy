#movie ticket price calculator#
age = int(input())
weekend = input("Weekend (yes/no): ")

if age < 12:
    price = 100
elif age >= 60:
    price = 120
else:
    price = 200

if weekend == "yes":
    price += 50

print("Ticket Price =", price)