class cliente (): #Clase
    def __init__(self): #Constructor
        self.nombre ='' # Atributos
        self.boleta = ''
        self.precio = 0
        self.clientes = 0
    def factura (self): #Método
        continuar = 's'
        while continuar == 's':
            self.clientes += 1
            self.nombre = str(input('Ingrese su nombre: '))
            self.precio = int(input('Ingrese el precio de la boleta: '))
            if self.precio == 1000000:
                self.boleta = 'VIP'
            elif self.precio == 500000:
                self.boleta = 'General'
            elif self.precio == 250000:
                self.boleta = 'Lateral'
            else:
                print('Error: el precio no es correcto.')
                break
            print(f'Bienvenid@ {self.nombre}, debe ingresar a la localidad: {self.boleta}\n')
            continuar = str(input('¿Quiere procesar otro cliente? (s/n) '))
        print(f'La cantidad de clientes procesados fueron: {self.clientes}')
if __name__ == "__main__":
    facturacion = cliente()
    facturacion.factura()

            