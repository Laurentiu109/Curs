"""

Scrieti un program care afiseaza toate literele (capitale) ale alfabetului englez,
pe aceias linie despartite prin spatiu.
A se vedea tabelul ASCII. chr(65) -> A

"""

for i in range(65, 91):
    chr(i)
    print(chr(i), end = " ")