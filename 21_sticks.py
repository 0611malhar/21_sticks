import random
n = 21
while n > 4:
    u = int(input("Enter the number(1-4)"))
    if u in range(1,5):
        n -= u
    else:
        print("invalid input")
    c = random.randint(1,5)
    n -= c


