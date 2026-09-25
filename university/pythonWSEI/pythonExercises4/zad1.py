class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Elektryczny(Samochod):
    def __init__(self, zasieg_na_ladowaniu, ** args):
        super(Elektryczny, self).__init__(**args)
        self.zasieg_na_ladowaniu = zasieg_na_ladowaniu

class Sportowy(Samochod):
    def __init__(self, maksymalna_predkosc, **args ):
        super(Sportowy, self).__init__(**args)
        self.maksymalna_predkosc = maksymalna_predkosc

class ElektrycznySportowy(Elektryczny, Sportowy):
    def __init__(self, marka, model, zasieg_na_ladowaniu, maksymalna_predkosc):
        super(ElektrycznySportowy, self).__init__(marka=marka, model=model, zasieg_na_ladowaniu=zasieg_na_ladowaniu, maksymalna_predkosc=maksymalna_predkosc)

elektryczny_sportowy = ElektrycznySportowy("Tesla", "Model S", 500, 250)
print(f"Marka: {elektryczny_sportowy.marka}")
print(f"Model: {elektryczny_sportowy.model}")
print(f"Zasięg na jednym ładowaniu: {elektryczny_sportowy.zasieg_na_ladowaniu} km")
print(f"Maksymalna prędkość: {elektryczny_sportowy.maksymalna_predkosc} km/h")

