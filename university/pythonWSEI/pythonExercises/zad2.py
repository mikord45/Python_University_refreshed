
age = input("Podaj wiek: ")
money = input("Podaj ilość pieniędzy w portfelu: ")

try:
    age = int(age)
    money = float(money)
    if(age >= 18 and money >= 20):
        toPrint = 'Jesteś pełnoletni i masz wystarczającą ilość pieniędzy'
    elif(age < 18 and money >= 20):
        missingAge = 18 - age
        toPrint = 'Nie jesteś pełnoletni, brakuje Ci ' + str(missingAge) + ' lat'
    elif(age >= 18 and money < 20):
        missingMoney = float(20) - money
        missingMoney = round(missingMoney, 2)
        toPrint = 'Nie masz wystarczającej ilości pieniędzy, brakuje Ci ' + str(missingMoney) + ' zł'
    else:
        missingAge = 18 - age
        missingMoney = float(20) - money
        missingMoney = round(missingMoney, 2)
        toPrint = 'Nie jesteś pełnoletni, brakuje Ci ' + str(missingAge) + ' lat oraz nie masz wystarczającej ilości pieniędzy, brakuje Ci ' + str(missingMoney) + ' zł'

    print(toPrint)
except ValueError:
    print('Podany wiek lub/oraz ilość pieniędzy są niepoprawne')
except Exception as e:
    print('Coś poszło nie tak')