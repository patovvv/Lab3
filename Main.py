import os

from Adjunto import Adjunto
from Regular import Regular

objt_adjunto=Adjunto()
objt_regular=Regular()
global ladjunto
global lregular
ladjunto=[]
lregular=[]


def DatosRegular():
    archivo = open('ListaRegular.txt','a')
    for i in range(len(lregular)):
        var = "Nombre: {}, Rut: {}, Grado: {}, Inicio: {}, Tipo: {}, Jornada: {}, Sueldo base: {}, Sueldo a pagar: {}".format(lregular[i].GetNombre(),lregular[i].GetRut(),lregular[i].GetGrado(),lregular[i].GetInicio(),lregular[i].GetTipo(),lregular[i].GetJornada(),lregular[i].GetSueldoBase(),lregular[i].GetSueldoFinal())
        archivo.write(var+os.linesep)
    archivo.close()

def DatosAdjunto():
    archivo = open('ListaAdjuntos.txt','a')
    for i in range(len(ladjunto)):
        var='Nombre: {}, Rut: {}, Grado: {}, Inicio: {}, Tipo: {}, Horas trabajadas: {}, Sueldo a pagar: {}'.format(ladjunto[i].GetNombre(),ladjunto[i].GetRut(),ladjunto[i].GetGrado(),ladjunto[i].GetInicio(),ladjunto[i].GetTipo(),ladjunto[i].GetHoras(),ladjunto[i].GetSueldoFinal())
        archivo.write(var+os.linesep)
    archivo.close()

def MostrarRegulares():
    with open("ListaRegular.txt") as f:   
        archivo=f.read()
        print(archivo)
        archivo=f.close()

def MostrarAdjuntos():
    with open("ListaAdjuntos.txt") as f:   
        archivo=f.read()
        print(archivo)
        archivo=f.close()
    

def VerificarRut():
    global rut
    while(True):
        try:
            rut=input("Ingrese su rut sin puntos ni digito verificador: ")
            digito=11-sum([int(a)*int(b) for a,b in zip(str(rut).zfill(8),"32765432")])%11
            a={10:"k",11:"0"}
            if digito==10 or digito==11:
                a.get(digito,str(digito))
            print ("Su rut fue ingresado correctamente")
            rut=str(rut)+str(digito)
            break
            
        except:
            print("Error... verifique ingresar su rut sin puntos ni digito verificador")

def IngresoData(a):
    #Funcion modifica atributos en comun de objeto docente y objeto adjunto
    print("")
    a.SetNombre(input("Ingrese su nombre completo: ").capitalize())
    print("")
    VerificarRut()
    a.SetRut(rut)
    print("")
    print(f"Ingrese opcion segun su grado\n1.Licenciado\n2.Magister\n3.Doctorado")
    while (True):
            try:
                pregunt=int(input("Opcion: "))
                while pregunt >3 or pregunt<1:
                    pregunt=int(input("Ingrese solo entre las opciones 1, 2 y 3: "))               
                break           
            except ValueError:
                print("Error...")

    if pregunt==1:
        a.SetGrado("Licenciado")
    if pregunt==2:
        a.SetGrado("Magister")
    if pregunt==3:
        a.SetGrado("Doctorado")
    print("")
    a.SetInicio(input("Ingrese fecha de inicio de contrato de la siguiente manera... Día-Mes-Año\nFecha: "))
    print("")   
    if a==objt_regular:  
        objt_regular.ModDatos()
        
        lregular.append(objt_regular)
        DatosRegular()
        
    if a==objt_adjunto:
        objt_adjunto.ModDatos()
        #
        ladjunto.append(objt_adjunto)
        DatosAdjunto
        
        
menu=0
while menu==0:
    print('_____')
    print('Menu docente')
    print("")   
    print('_____')
    print(f"Ingrese opción mostrada\n1.Docente regular\n2.Docente adjunto\n3.Ver datos")
    while (True):
            try:
                op2=int(input("Opcion: "))
                while op2 >3 or op2<1:
                    op2=int(input("Ingrese solo entre las opciones 1, 2 y 3: "))               
                break           
            except ValueError:
                print("Error...")

    if op2==1:
        IngresoData(objt_regular)
    if op2==2:
        IngresoData(objt_adjunto)
    if op2==3:#REVISAR
        print("")
        print("Informacion docente")
        print("_____")
        print("Seleccione lista de datos")
        print("_____")
        print("1.Lista docentes regulares\n2.Lista docentes adjuntos")
        while (True):
            try:
                d=int(input("Opcion: "))
                while d>2 or d<1:
                    d=int(input("Ingrese solo entre las opciones 1 o 2: "))               
                break           
            except ValueError:
                print("Error...")
        if d==1:
            MostrarRegulares()
            espacio=input("Volviendo al menu inicial...")

        if d==2:
            MostrarAdjuntos()
            espacio=input("Volviendo al menu inicial...")