class planta:
    def __init__(self):
        self.plantas = 0
    def crecimiento (self):
        inicio = int (input ('Ingrese la cantidad actual de plantas: '))
        tasa  = float (input ('Ingrese la tasa actual de crecimiento (por ejemplo, 0.20 para 20%): '))
        dias = int (input ('Ingrese los días que quiere predecir la cantidad de plantas: '))
        self.plantas = inicio * ( 1 + tasa )** dias
        print(f"La cantidad de plantas después de {dias} días es: {self.plantas:.2f}")
if __name__ == "__main__":
    total_plantas = planta ()
    total_plantas.crecimiento()