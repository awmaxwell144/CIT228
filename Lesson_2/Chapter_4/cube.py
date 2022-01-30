cubes = []
for n in range(1,11):
    cubes.append(n**3)
for c in cubes:
    print(c)

cubes = [n**3 for n in range(1,11)]
for c in cubes:
    print(c)