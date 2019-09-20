import random

n1 = random.randint(1, 30)

p = 0
while p < 5:
    n2 = int(input("Guess my number: "))
    if n1 == n2:
        print("You win!")
        break
    elif n2 > n1:
        print("Your number is bigger than mine")
    else:
        print("Your number is less than mine")
    p += 1

if p == 5:
    print("Your lost! My number was", n1)
