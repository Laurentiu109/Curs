# inmultirea numerelor

def produs(a, b):
    res = 0
    for i in range(b):
        res = res + a
    return res


print(produs(3, 4))

x_result = produs(30, 23)

print(x_result + 2)