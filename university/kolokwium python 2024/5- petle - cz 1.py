for litera in 'napis':
    print(litera)

print("=====")

lista = [1,2,3,4,5]
for element in lista:
    print(element)

print("=====")

lista_z_zerami = [1, 0, 0, 4, 5]
for element in lista_z_zerami:
    if element == 0:
        continue
    print(element)

print("======")

for element in lista_z_zerami:
    if element == 0:
        break
    print(element)

print("======")

for element in lista:
    if element == 0:
        break
    print(element)
else:
    print("wykonano bez przerwania")

print("======")

for element in lista_z_zerami:
    if element == 0:
        break
    print(element)
else:
    print('wykonano bez przerwania')

print("======")

for((a, b), c) in zip([(1, 'a'), (2, 'b'), (3, 'c')], [4,5,6]):
    print(a, b, c)

print("=====")
for(a, c) in zip([(1, 'a'), (2, 'b'), (3, 'c')], [4,5,6]):
    print(a, c)
    # print(a[0], a[1], c)


