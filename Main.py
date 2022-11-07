from Adjunto import Adjunto
from Regular import Regular
objt_adjunto=Adjunto()
objt_regular=Regular()
global ladjunto
global lregular
ladjunto=[]
lregular=[]


def IngresoData(a):
    #Funcion modifica atributos en comun de objeto docente y objeto adjunto
    print("")
    a.SetNombre(input("Ingrese su nombre completo: "))
    print("")
    a.SetRut(input("Ingrese su rut: "))
    print("")
    print("")
    print(f"Ingrese opcion segun su grado\n1.Licenciado\n2.Magister\n3.Doctorado")
    pregunt=int(input("Opción a elegir: "))
    while pregunt>3 or pregunt<1 or pregunt==str:
        print("")
        print(f"Error...\nIngrese opcion valida...\n1.Licenciado\n2.Magister\n3.Doctorado")
        pregunt=int(input("Opción: "))
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
        #Funcion modifica atributos especificos de objeto regular
        objt_regular.ModDatos()
    if a==objt_adjunto:
        #Funcion modifica atributos especificos de objeto adjunto
        objt_adjunto.ModDatos()

    
menu=0
while menu==0:
    print('_____')
    print('Menu docente')
    print("")   
    #print(f"Ingrese opción que desea realizar\n1.Ingresar docente\n2.Ver datos")
    print('_____')

    op2 = int(input(f"Ingrese tipo docente\n1.Docente regular\n2.Docente adjunto\n3.Ver datos\nOpcion: "))
    while op2 < 1 or op2 > 3 or op2==str:
        op2 = input("Error... Ingrese tipo docente\n1.Docente regular\n2.Docente adjunto\nOpcion: ")
        print('')

    if op2==1:
        #b=1       
        lregular.append(IngresoData(objt_regular))

    if op2==2:
        #b=2
        ladjunto.append(IngresoData(objt_adjunto))

    if op2==3:
        print("")
        print("Informacion docente")
        print('')
        print("Seleccione que tipo de datos desea ver")
        d=int(input("1.Datos docentes regulares\n2.Datos docentes adjuntos\nOpcion: "))
        while d<1 or d>2 or d==str:
            print("Error... Seleccione opcion valida:")
            d=int(input("1.Docentes regulares\n2.Docentes adjuntos\nOpcion: "))
            print('')
        if d==1:
            for lista in lregular:
                print(lista)
                
        if d==2:
            for lista in ladjunto:
                print(lista)