from Docente import Docente

class Regular(Docente):
    def __init__(self, nombre='',rut='',grado='',inicio='',tipo='Regular',jornada='',sueldobase=0,sueldofinal=0):
        super().__init__(nombre,rut,grado,inicio,tipo,sueldofinal)
        self.__jornada=jornada             
        self.__sueldobase=sueldobase

    def __str__(self):
        return 'Nombre: {} -  Rut: {}  -  Grado: {}  -  Inicio: {}  -  Tipo: {}  -  Jornada: {}  -  Sueldo base: {}  -  Sueldo a pagar: {}'.format(self.GetNombre(),self.GetRut(),self.GetGrado(),self.GetInicio(),self.GetTipo(),self.GetJornada(),self.GetSueldoBase(),self.GetSueldoFinal())
         

    #Get y Set de jornada del docente
    def GetJornada(self):
        return self.__jornada
    def SetJornada(self,jornada):
        self.__jornada=jornada

    #Get y Set de sueldo base del docente
    def GetSueldoBase(self):
        return self.__sueldobase
    def SetSueldoBase(self,sueldobase):
        self.__sueldobase=sueldobase

    #Calculo de bono
    def Bono(self):
        global bono
        bono=0
        #Bono para docentes Licenciados
        if self.GetGrado()=='Licenciado' and self.GetJornada()=="Media":
            bono=100000
        if self.GetGrado()=="Licenciado" and self.GetJornada()=="Completa":
            bono=200000

        #Bono para docentes con Magister
        if self.GetGrado()=="Magister" and self.GetJornada()=="Media":
            bono=300000
        if self.GetGrado()=="Magister" and self.GetJornada()=="Completa":
            bono=500000

        #Bono para docentes con Doctorado
        if self.GetGrado()=="Doctorado" and self.GetJornada()=="Media":
            bono=700000
        if self.GetGrado()=="Doctorado" and self.GetJornada()=="Completa":
            bono=800000
            
        self.SetSueldoFinal(bono+self.GetSueldoBase())

    def ModDatos(self):
        j=int(input("Ingrese jornada\n1.Jornada completa\n2.Jornada media\nOpción:"))
        while j>2 or j<1 or j==str:
            j=int(input("Error...\nIngrese opción valida\n1.Jornada completa\n2.Jornada media\nOpción:"))
        if j==1:
            self.SetJornada("Completa")
        if j==2:
            self.SetJornada("Media")
        s=int(input("Ingrese su sueldo sin comas ni puntos: "))
        while s==str or s<0:
            s=int(input("Error... Ingrese su sueldo sin comas ni puntos: "))
        self.SetSueldoBase(s)
        self.Bono()
        print('Docente agregado correctamente, regresando al menu de inicio...')

        