class Persona():
    def __init__(self,nombre='',rut=''):
        self.__nombre=nombre
        self.__rut=rut

    def __str__(self):
        return 'Nombre: {} -  Rut: {}'.format(self.GetNombre(),self.GetRut())
        
    #Get y Set de nombre del docente
    def GetNombre(self):
        return self.__nombre
    def SetNombre(self,nombre):
        self.__nombre=nombre 
    

    #Get y Set de rut del docente
    def GetRut(self):
        return self.__rut
    def SetRut(self,rut):
        self.__rut=rut
        