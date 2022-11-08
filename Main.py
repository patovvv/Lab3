from io import open
from Adjunto import Adjunto
from Regular import Regular
objt_adjunto=Adjunto()
objt_regular=Regular()
global ladjunto
global lregular
ladjunto=[]
lregular=[]
archtxt1Agregar=open("DatosDRegulares.txt","r+",encoding="utf-8")
archtxt1Leer=open("DatosDRegulares.txt","r+",encoding="utf-8")

archtxt2Agregar=open("DatosDAdjuntos.txt","r+",encoding="utf-8")
archtxt2Leer=open("DatosDAdjuntos.txt","r+",encoding="utf-8")

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

    if a==objt_adjunto:       
        objt_adjunto.ModDatos()

    
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
        archtxt1Agregar.write(str(IngresoData(objt_regular)))   

    if op2==2:       
        archtxt2Agregar.write(str(IngresoData(objt_adjunto)))

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
            #for lista in lregular:
            #print(lregular)
            #lista1=archtxt1Leer.read()
            print(archtxt1Leer.read())
            espacio=input("Volviendo al menu inicial...")
        if d==2:
            #for lista in ladjunto:
            #print(ladjunto)
            print(archtxt2Leer.read())
            
            espacio=input("Volviendo al menu inicial...")


#probando subir archivo