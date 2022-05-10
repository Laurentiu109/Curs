"""

Intr-o cutie se afla 300 de bile, numerotate cu numere incepand de la unu din trei in trei.
Toate bilele carora le corespund numere pare sunt verzi. 
Sa se afle cate bile verzi sunt.

"""
"""
Modalitate 1



even_count = 0
for i in range(1, 900, 3):
    if i % 2 == 0:
        print(i, end = ' ')
        even_count = even_count + 1
print (" === Total Bile verzi === ", even_count)


"""


i = 0
nr_pe_bile = 1
bile_verzi = 0

while i <= 300 :
    if nr_pe_bile % 2 == 0 :
        bile_verzi += 1
    i += 1
    nr_pe_bile += 3 
print ("Bile verzi= ",bile_verzi)