import math

a = input('Podaj wartość współczynnika "a" równiania kwadratowego: ')
b = input('Podaj wartość współczynnika "b" równiania kwadratowego: ')
c = input('Podaj wartość współczynnika "c" równiania kwadratowego: ')

def calculate_roots_of_the_quadratic_equation(a, b, c):
    try:
        a_value = float(a)
        b_value = float(b)
        c_value = float(c)
        if(a_value == 0):
            return
        discriminant = b_value * b_value - (4 * a_value * c_value)
        if(discriminant < 0):
            return []
        if(discriminant == 0):
            double_root = (-1 * b_value) / (2*a_value)
            return [double_root, double_root]

        square_root_of_discriminant = math.sqrt(discriminant)
        first_root = ((-1 * b_value) - square_root_of_discriminant) / (2*a_value)
        second_root = ((-1 * b_value) + square_root_of_discriminant) / (2*a_value)
        return [first_root, second_root]

    except Exception as e:
        return

roots = calculate_roots_of_the_quadratic_equation(a, b, c)

if(roots == None):
    print("Podane wartości współczynników równania kwadratowego są niepoprawne")
elif(len(roots) == 0):
    print("To równianie kwadratowe nie posiada pierwiastków")
elif(roots[0] == roots[1]):
    print("To równianie kwadratowe posiada jeden podwójny pierwiastek: " + str(roots[0]))
else:
    print("To równanie kwadratowe posiada dwa pierwiastki: " + str(roots[0]) + " oraz " + str(roots[1]))