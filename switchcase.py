class nota ():#Clase
    def __init__(self): #Constructor
        self.promedio = 0 #Atributos
        self.categoria = ''
    def materia (self): #Método
        codigo = str(input('Ingrese su código estudiantil: '))
        nota1 = float(input('Ingrese la primera nota: '))
        nota2 = float(input('Ingrese la segunda nota: '))
        nota3 = float(input('Ingrese la tercera nota: '))
        nota4 = float(input('Ingrese la cuarta nota: '))
        self.promedio = (nota1+nota2+nota3+nota4)/4
        if self.promedio > 3.4:
            print('Aprobado')
            if self.promedio > 4.5:
                self.categoria = 'Superior'
                print('El estudiante {} se encuentra en la escala de desempeños: {}'.format(codigo,self.categoria))
            else: 
                if self.promedio > 3.9:
                    self.categoria = 'Alto'
                    print('El estudiante {} se encuentra en la escala de desempeños: {}'.format(codigo,self.categoria))
                else:
                    self.categoria ='Básico'
                    print('El estudiante {} se encuentra en la escala de desempeños: {}'.format(codigo,self.categoria))
        else: 
            print('Reprobado')
            if self.promedio> 3.0:
                self.categoria = 'Básico'
                print('El estudiante {} se encuentra en la escala de desempeños: {}'.format(codigo,self.categoria))
            else:
                self.categoria = 'Bajo'
                print('El estudiante {} se encuentra en la escala de desempeños: {}'.format(codigo,self.categoria))

if __name__=="__main__":
    estudiante = nota() #Objeto
    estudiante.materia()