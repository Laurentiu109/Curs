# 4. Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
# un singur agument reprezentand muchia cubului in metri.

def cube_volume(edge):

# 1 m3 = 1000 litri

    return edge ** 3 * 1000

def convert_to_m3(liters):

    return liters / 1000

edge = int(input("muchia:"))

print("Volumul cubului:" , convert_to_m3(cube_volume(18)), "m3")
