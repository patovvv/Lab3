from Persona import Persona

class Docente(Persona):
    def __init__(self, nombre='', rut='', grado='',inicio='',tipo='',sueldofinal=0):
        super().__init__(nombre,rut)
        self.__grado=grado
        self.__inicio=inicio
        self.__tipo=tipo
        self.__sueldofinal=sueldofinal
    def __str__(self):
        return 'Nombre: {} -  Rut: {}  -  Grado: {}  -  Inicio: {}  -  Tipo: {}  -  Sueldo a pagar: {}'.format(self.GetNombre(),self.GetRut(),self.GetGrado(),self.GetInicio(),self.GetTipo(),self.GetSueldoFinal())

    #Get y Set de grado docente
    def GetGrado(self):
        return self.__grado
    def SetGrado(self,grado):
        self.__grado=grado

    #Get y Set de inicio fecha contrato
    def GetInicio(self):
        return self.__inicio
    def SetInicio(self,inicio):
        self.__inicio=inicio

    #Get y Set de tipo docente
    def GetTipo(self):
        return self.__tipo
    def SetTipo(self,tipo):
        self.__tipo=tipo

    #Get y Set de sueldo final
    def GetSueldoFinal(self):
        return self.__sueldofinal
    def SetSueldoFinal(self,sueldofinal):
        self.__sueldofinal=sueldofinal