class examen:
    def __init__(self): #Constructor
        self.admitido = '' #Atributo
    def evaluar (self): #Método
        nota1 = float(input('Ingrese la nota del primer examen: '))
        nota2 = float(input('Ingrese la nota del segundo examen: '))
        if nota1 >= 80 and nota2 >= 80:
            self.admitido = 'Felicitaciones ha sido admitido'
        else:
            self.admitido = 'Lastimosamente no ha sido admitido'
        print(self.admitido)
        
if __name__ == "__main__":
    respuesta = examen () #Objeto
    respuesta.evaluar()