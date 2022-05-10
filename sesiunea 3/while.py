"""
while conditie:
    cod - instructiuni
    cod - instructiuni
    cod - instructiuni
"""

# executam de 3 x print

"""
n = 0


while n < 3:
    print("Hello!")
    n = n + 1

    # 1. n = 0
    # 2. n = 1
    # 3. n = 2
    # 4. n = 3 - nu se mai executa

"""


n = input("introduceti numar = ")
n = int(n)

k = 1
k = int(k)

while  k <= n:
    print("*" * k, "+" * (n - k), sep='')
    k = k + 1


# 1. n = 3; k = 1
# 2. n = 3; k = 2
# 3. n = 3; k = 3
# 4. n = 3; k = 4 - nu se mai executa