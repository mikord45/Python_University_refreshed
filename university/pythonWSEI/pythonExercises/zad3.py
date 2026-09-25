from enum import Enum

class Modes(Enum):
    MONTHLY = 'monthly'
    YEARLY = 'yearly'

invalidValueMessage = 'Podano niepoprawną wartość w odpowiedzi na rodzaj dochodu'

try:
    selected_mode = Modes.YEARLY
    mode = input("Czy chcesz podać dochód miesięczny[m] czy roczny[R]: ")
    if (mode == 'm' or mode == 'M'):
        selected_mode = Modes.MONTHLY
    elif (mode != 'r' and mode != 'R' and mode != ''):
        raise Exception(invalidValueMessage)

    income = round(float(input('Podaj swój dochód: ')), 2)
    if(selected_mode == Modes.MONTHLY):
        income *= 12

    tax = 0.0
    if(income <= 120000):
        tax = round(income * 0.12, 2)
    elif(income > 120000):
        tax = round(120000 * 0.12, 2) + round((income - 120000) * 0.32, 2)
    print('Podatek wynosi: ' + str(round(tax, 2)))
except ValueError:
    print('Podane wartości są niepoprawne')
except Exception as e:
    if(str(e) == invalidValueMessage):
        print(e)
    else:
        print('Coś poszło nie tak')