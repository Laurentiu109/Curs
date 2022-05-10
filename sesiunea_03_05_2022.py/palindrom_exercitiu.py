# Scrie un program care citeste de la tastatura u nr natural
# si verifica daca acesta este palindrom. 111 121 292 2992 33533


# Functie care returneaza True daca un nr este palindrom

# Citim de la tastatura un nr

# Apelam functia

def reverse(n):
    rev = 0
    while n != 0:
        c = n % 10 # rest
        n = n // 10 # cat
        rev = rev * 10 + c

    return rev

def palindrom(n):
    if n == reverse(n):
        return True
    else:
        return False

n = input("numar = ")
n = int(n)

if palindrom(n):
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")