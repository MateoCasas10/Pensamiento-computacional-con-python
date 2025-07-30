class nota:
    def __init__ (self):
        self.promedio = 0
        self.suma_notas = 0
    def notas (self):
        cantidad = int(input('Ingrese la cantidad de notas para calcular el promedio: '))
        for i in range (cantidad):
            nota = float (input('Ingrese la nota: '))
            self.suma_notas += nota
            self.promedio = self.suma_notas / cantidad
        print('El promedio de las notas ingresadas es:', self.promedio)
if __name__ == "__main__":
    promedio_notas = nota ()
    promedio_notas.notas()