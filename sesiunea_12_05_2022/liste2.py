# magic_numbers = [2.3, 4.5, 46.6, 29.29, 0.22, 23.3]
#              #    0    1    2      3      4     5

# for index in range(0, len(magic_numbers), 2):
#     print(index, magic_numbers[index])


magic_numbers = [2.3, 4.5, 46.6, 29.29, 0.22, 23.3]
             #    0    1    2      3      4     5

for index in range(len(magic_numbers) -1, -1, -1):
    print(magic_numbers[index])
