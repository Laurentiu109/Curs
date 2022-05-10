# 2. Scrie un program care citeste de la tastatura un numar 
# natural, reprezentand raza unui cerc, si afiseaza perimetrul
# cercului insotit de mesajul "Perimetru cercului = <valoare>".
# Daca numarul citit este mai mare decat 100 se va calcula si aria
# cercului. Aceasta se va afisa insotita de mesajul "Aria cercului = <valoare>".

"""

from cmath import pi


raza = input("raza cercului =")
raza = int(raza)


perimetru = 2 * 3.14 * raza

aria = 3.14 * (raza ** 2)

if raza > 0 and raza <= 100 :
    print("Perimetru cercului = " , perimetru)

else:
    print("Aria cercului este = " , aria)

"""

# 4. Scrie un program care citeste de la tastatura doua numere,
# si calculeaza a / b daca a > b sau b / a daca a <= b. Afiseaza 
# rezultatul.


""""

a = input("dati a = ")
a = float(a)

b = input("dati b = ")
b = float(b)

c = a / b
c = float(c)

d = b / a
d = float(d)

if a > b :
    print("Impartirea lui a la b = " , float(c))
elif b >= a :
    print("Impartirea lui b la a = " , float(d))
else:
    print("asta e")


"""

# 3. Scrie un program care citeste de la tastatura doua numere, a si b.
# Daca a > b sa se diferenta suma lor.
# Daca a == b sa se afiseze a la puterea b
# Altfel sa se afiseze suma lor.



a = input("dati a = ")
a = int(a)

b = input("dati b = ")
b = int(b)

c = a - b
c = int(c)

d = a ** b
d = int(d)

e = a + b
e = int(e)

if a > b :
    print("diferenta lor = " , int(c))
elif a == b :
    print("b la puterea a = " , int(d))
else:
    print("suma lor este = " , int(e))