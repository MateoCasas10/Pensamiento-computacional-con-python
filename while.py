class inscripcion (): #Clase
    def __init__(self):#constructor
        self.nombre = ''
        self.codigo = ''
        self.inscritos = 0
        self.lista = []
    def estudiantes (self): #Método
        continuar = 's'
        while continuar == 's':
            self.inscritos += 1
            self.nombre = str(input('Ingrese el nombre completo del estudiante: '))
            self.codigo = str(input('Ingrese su código: '))
            self.lista.append((self.inscritos, self.nombre, self.codigo))
            continuar = str(input('¿Dese inscribir a alguien más? (s/n)'))
        print(f'{'N°':<15}{'Nombre':<36}{'Código'}')
        for i in self.lista:
            print(f'{i[0]:<15}{i[1]:<36}{i[2]}')
        print('_'*62)
        print ('La cantidad de inscritos al curso es: ', self.inscritos)
if __name__ == "__main__":
    inscritos = inscripcion ()
    inscritos.estudiantes()