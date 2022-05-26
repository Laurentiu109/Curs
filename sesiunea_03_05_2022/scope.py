def reverse(n):
    rev = 0
    while n != 0:
        c = n % 10 # rest
        n = n // 10 # cat
        rev = rev * 10 + c

    return rev