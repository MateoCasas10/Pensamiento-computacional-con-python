import math #Libreria
class calculo_angulos(): #Clase
    def __init__(self): #Constructor
        self.seno = 0#Atributos
        self.coseno = 0
        self.tangente = 0
    def angulo (self):#Método
        cantidad = int(input('Ingrese la cantidad de ángulos a calcular: '))
        resultados = []
        for i in range(cantidad):
            angulo = float(input('Ingrese el ángulo en grados: '))
            x = math.radians(angulo)
            self.seno = math.sin(x)
            self.coseno = math.cos(x)
            self.tangente = math.tan(x)
            resultados.append([angulo, self.seno, self.coseno, self.tangente])
        print(f'{'Ángulo(°)':<12}{'Seno':<12}{'Coseno':<12}{'Tangente':<12}')
        print('_'*44)
        for fila in resultados:
            print(f'{fila[0]:<12.4f}{fila[1]:<12.4f}{fila[2]:<12.4f}{fila[3]:<12.4f}')
if __name__ == "__main__":
    calculo = calculo_angulos ()
    calculo.angulo()