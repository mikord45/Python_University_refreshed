import time

name = input("Podaj imie: ")
age = input("Podaj wiek: ")

try:
    age = int(age)
    print('Cześć ' + name + "!")
    name_as_list = list(name)
    print('Twoje imię ma ' + str(len(name_as_list)) + " liter i zaczyna się od " + str(name_as_list[0]))
    age_in_one_year = age + 1
    current_time = time.gmtime()
    current_year = current_time.tm_year
    year_of_birth = current_year - age
    print('Teraz masz ' + str(age) + ' lat(a), a za rok będzie to ' + str(age_in_one_year) + '. Rok urodzenia to ' + str(year_of_birth))
except ValueError:
    print('Podany wiek nie jest liczbą')
except Exception as e:
    print('Coś poszło nie tak')