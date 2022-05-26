# scrieti un script care citeste de la tst 3 nr (a, b si c) si afiseaza toti multipli comuni intr-un interval.
# primul nr (a) reprezinta limita superioara a intervalului in care se opereaza, limita inferioara este 1
# celelalte 2 (b, c) sunt numerele pentru care se vor cauta multipli comuni

# extra: sa se verifice daca b si c sunt mai mari decat 1 si mai mici decat lim. sup. (a)
# daca nu sunt in intervalul respectiv sa se afiseze eroare

a = input("numar a = ")
a = int(a)

b = input("numar b = ")
b = int(b)

c = input("numar c = ")
c = int(c)

multipli_b = list (range(1*b, a+1, b))
multipli_c = list (range(1*c, a+1, c))

set1 = set(multipli_b)
set2 = set(multipli_c)

intersec = set1.intersection (set2)
for i in intersec:
    print(i)
