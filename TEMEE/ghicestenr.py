from operator import ge
import random

print("Incepe jocul!")
print("Introduceti un numar intre 1 si 99")

n = -1

x = random.randint(1, 100)

while x != n:

    n = input(" ")
    n = int(n)

    if x > n:
        print(" + ")

    else:
        print(" - ")

print("Felicitari!")
print("Ai ghicit numarul" , n)


"""

import random

generated_number = random.randint(1, 100)
print(generated_number)

print("Ghiceste numarul")
print("Alege numarul intre 1 si 99:")

while number != generated_number:
    if number < generated_number:
        print("+")
    elif number > generated_number:
        print("-")
    number = int(input("Numarul este :"))
print("Felicitari ai ghicit numarul:")

"""