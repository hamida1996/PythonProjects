import random

print("\nThis is a Password Generator Program")
print("====================================\n")

chars = "abcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+?/\\|[{]}<>ABCDEFGHIJKLMNOPQRSTUVWXYZ'\""

amount = int(input("Set the number of passwords: "))
lenght = int(input("Set the lenght of passwords: "))

print("\nHere are your passwords:\n")

for a in range(amount):
    password = ""
    for b in range(lenght):
        password += random.choice(chars)
    print(password)
