# scrie un program care citeste de la tastatura un nr natural  "n"
# si afiseaa n! (factorial)


n = int(input("n = "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial + 1
print("Numarul factorial al", "n este:" , factorial)
