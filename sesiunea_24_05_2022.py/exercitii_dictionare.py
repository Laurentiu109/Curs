words = ['Python', 'is', 'an' 'easy', 'to', 'learn', 'powerful', 'programming', 'language']

d1 = {}

def histrogram():
    for i in words:
        if i not in d1:
            d1[i]= words.count(i)

for k, v in d1.items():
    print(k, "." * 5, v)

histrogram()


# Python.....12
# is.....18
# .....