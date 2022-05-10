a = input("a= ")
b = input ("b= ")

a = int(a)
b = int(b)

if a > b:
    print("a mai mare decat b")
    if b < a - b:
        print("b este mai mic decat jumatate lui a")

elif a == b:
    print("a si b sunt egale")
else:
    print("b mai mare decat a")

    print("DONE")