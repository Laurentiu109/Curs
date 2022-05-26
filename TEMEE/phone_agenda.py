print (" " * 15, "AGENDA TELEFON")

def display_menu():

    print("1. Adauga numarul de telefon in agenda telefonului")
    print("2. Cauta numarul de telefon din agenda telefonului")
    print("3. Sterge numarul de telefon din agenda telefonului")
    
    return int(input("Selectati optiunea: "))

d1 = {}

while True:
    n = display_menu()
    if n==1:
        name=input("Introduceti numele:")
        numar=input("introduceti numarul de telefon:")
        varsta=int(input("Intorduceti varsta:"))
        d1[name]=[numar, varsta]
    elif n==2:
        name1=input("Introduceti numele pe care vrei sa il cauti in agenda telefonului: ")
        if name1 in d1.keys():
             print("Numarul de telefon" , name1 , "este", d1[name1][0])
        else:
            print("Numarul nu exista in agenda telefonului!")
    elif n==3:
        name1=input("Introduceti numele contactului pe care vrei sa il stergi din agenda: ")
        if name1 in d1.keys():
            del d1[name1]
            print("Numarul a fost sters!")
        else:
            print("Numarul nu exista in agenda telefonului!")
        
    elif n==0:
        break