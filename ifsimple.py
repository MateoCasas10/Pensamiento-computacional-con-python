class empleado:
    def __init__(self):
        self.sueldo = 0
    def incentivo (self):
        trabajador = str (input('Ingrese el nombre del empleado: '))
        horas = int(input('Ingrese las horas trabajadas: '))
        sueldobase = float(input('Ingrese el sueldo base del empleado: '))
        if horas > 40:
            self.sueldo = sueldobase + (sueldobase * 0.05)
            print('El empleado {} tiene el incentivo, por lo tanto su suelo es: {}'.format(trabajador,self.sueldo))

if __name__ == "__main__":
    sueldo_incentivo = empleado ()
    sueldo_incentivo.incentivo()