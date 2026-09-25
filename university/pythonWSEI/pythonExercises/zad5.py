import math

sideA = input('Podaj długość pierwszego boku trójkąta: ')
sideB = input('Podaj długość drugiego boku trójkąta: ')
sideC = input('Podaj długość trzeciego boku trójkąta: ')

def calculate_triangle_area(sideA, sideB, sideC):
    try:
        sideALength = float(sideA)
        sideBLength = float(sideB)
        sideCLength = float(sideC)
        if(sideALength <= 0 or sideBLength <= 0 or sideCLength <= 0):
            return -1
        allSides = [sideALength, sideBLength, sideCLength]
        allSides.sort(reverse=True)
        if(allSides[0] >= allSides[1] + allSides[2]):
            return -1
        p = 0.5 * (sideALength + sideBLength + sideCLength)
        area = math.sqrt(p*((p - sideALength) * (p - sideBLength) * (p - sideCLength)))
        return float(area)
    except Exception as e:
        return -1

triangleArea = calculate_triangle_area(sideA, sideB, sideC)

if(triangleArea > 0):
    print("Pole trójkąta wynosi " + str(triangleArea))
else:
    print("Podane długości boków trójkąta są niepoprawne")