#fare tax for distance#
km = int(input("Distance: "))

if km <= 5:
    fare = 100
elif km <= 15:
    fare = 100 + (km - 5) * 15
else:
    fare = 100 + 10 * 15 + (km - 15) * 12

print("Fare =", fare)