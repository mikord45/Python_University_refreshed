def user(imie, nazwisko):
    return imie+' '+nazwisko

print(user('Mikolaj', 'Stryczek'))

def wypisz(a):
    for x in a:
        print(x)

wypisz('abcde')
print("======")
wypisz([1,2,3,4,5,6,7,8,9,10])