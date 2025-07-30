class Calculadora:
    def __init__(self):
        self.resultado = 0

    def suma(self):
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        self.resultado = num1 + num2
        print('El resultado de la suma es:', self.resultado)

    def resta(self):
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        self.resultado = num1 - num2
        print('El resultado de la resta es:', self.resultado)

    def multiplicacion(self):
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        self.resultado = num1 * num2
        print('El resultado de la multiplicación es:', self.resultado)

    def division(self):
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        if num2 == 0:
            print('Error, no se puede dividir por cero')
        else:
            self.resultado = num1 / num2
            print('El resultado de la división es:', self.resultado)

    def menu(self):
        while True:
            print("""
                        ------- Bienvenido al menú de la calculadora -------
                        Seleccione la opción que desea ejecutar:
                        1. Suma
                        2. Resta
                        3. Multiplicación
                        4. División
                        5. Salir """)
            opcion = input("Ingrese una opción (1-5): ")

            if opcion == '1':
                self.suma()
            elif opcion == '2':
                self.resta()
            elif opcion == '3':
                self.multiplicacion()
            elif opcion == '4':
                self.division()
            elif opcion == '5':
                print("Gracias por usar la calculadora.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calc = Calculadora()
    calc.menu()
