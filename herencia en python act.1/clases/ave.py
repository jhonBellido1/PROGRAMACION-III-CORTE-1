from clases.animal import animal
from datetime import date
class ave(animal):
    def __init__(self, nombre, peso, año_nacimiento, propietario):
        super().__init__(nombre, peso)
        self.año_nacimiento=año_nacimiento
        self.propietario=propietario
        
    def calcular_edad(self):
        año_actual = date.today().year
        edad = año_actual - self.año_nacimiento

        if edad >= 5:
            print(f"La ave {self.nombre} es MAYOR DE EDAD.")
        else:
            print(f"La ave {self.nombre} es MENOR DE EDAD.")    