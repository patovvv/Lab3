from Docente import Docente



class Adjunto(Docente):
    def __init__(self,nombre='',rut='',grado='',inicio='',tipo='Adjunto',horast=0,sueldofinal=0):
        super().__init__(nombre,rut,grado,inicio,tipo,sueldofinal)       
        self.__horast=horast 

    def __str__(self):
        return 'Nombre: {} -  Rut: {}  -  Grado: {}  -  Inicio: {}  -  Tipo: {}  -  Horas trabajadas: {}  -  Sueldo a pagar: {}'.format(self.GetNombre(),self.GetRut(),self.GetGrado(),self.GetInicio(),self.GetTipo(),self.GetHoras(),self.GetSueldoFinal())
        
    #Get y Set de horas trabajadas por docente
    def GetHoras(self):
        return self.__horast
    def SetHoras(self,horast):
        self.__horast=horast


    def Sueldo(self):       
        valorhora=0
        if self.GetGrado()=="Licenciado":
            valorhora=16000
        if self.GetGrado()=="Magister":
            valorhora=19000
        if self.GetGrado()=="Doctorado":
            valorhora=25000
        self.SetSueldoFinal(self.GetHoras()*valorhora)

    
    def ModDatos(self):
        global menu
        print("Ingrese cantidad de horas trabajadas en el mes")
        while (True):
            try:
                h=int(input("Horas: "))
                while h<0:
                    h=int(input("La cantidad de horas debe ser mayor a cero: "))               
                break           
            except ValueError:
                print("Error...")
        self.SetHoras(h)
        self.Sueldo() 
        print("")
        espacio=input('Docente agregado correctamente, regresando al menu de inicio...')
        
        
        menu=0
   