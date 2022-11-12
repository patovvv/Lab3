from io import open
from Adjunto import Adjunto
from Regular import Regular
objt_adjunto=Adjunto()
objt_regular=Regular()
global ladjunto
global lregular
ladjunto=[]
lregular=[]
arch1=open("arch1.txt","a",encoding="utf-8")
#arch1Leer=open("DatosDRegulares.txt","r",encoding="utf-8")

arch2=open("arch2.txt","a",encoding="utf-8")
#arch2Leer=open("DatosDAdjuntos.txt","r",encoding="utf-8")

def IngresoData(a):
    #Funcion modifica atributos en comun de objeto docente y objeto adjunto
    print("")
    a.SetNombre(input("Ingrese su nombre completo: "))
    print("")
    a.SetRut(input("Ingrese su rut: "))
    print("")
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
        EscribirArchivo1(objt_regular)

    if a==objt_adjunto:
        objt_adjunto.ModDatos()
        EscribirArchivo2(objt_adjunto)
        
def EscribirArchivo1(fp):
    ret=arch1.open("arch1.txt",mode="w",encoding="utf-8")
    ret.write(fp)
def EscribirArchivo2(fp):
    ret=arch1.open("arch2.txt",mode="w",encoding="utf-8")
    ret.write(fp)

def LeerArchivo1():
    ret=arch1.open("arch1.txt",mode='r', encoding="utf-8")
    ret.read()
def LeerArchivo2():
    ret=arch2.open("arch2.txt",mode='r', encoding="utf-8")
    ret.read()

    
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
    if op2==3:
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
            LeerArchivo1()
            espacio=input("Volviendo al menu inicial...")

        if d==2:
            LeerArchivo2()        
            espacio=input("Volviendo al menu inicial...")