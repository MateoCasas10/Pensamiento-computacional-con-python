class movimiento:
    def __init__(self):
        self.distancia = 0
    def calculo (self):
        objeto = str (input ('Ingrese el objeto que se mueve: '))
        velocidad = float (input ('Ingrese la velocidad del objeto en m/s: '))
        tiempo = float (input ('Ingrese el tiempo en segundos en el cual quiere saber la distancia recorrida:'))
        self.distancia = velocidad * tiempo
        print(f"La distancia recorrida por {objeto} en {tiempo}s es: {self.distancia:.2f}")
if __name__ == "__main__":
    distancia_recorrida = movimiento ()
    distancia_recorrida.calculo()