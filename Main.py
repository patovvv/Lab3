from Adjunto import Adjunto
from Regular import Regular

regular=Regular()
adjunto=Adjunto()

def Regulares(a):
    print("")
    a.SetNombre(input("Ingrese su nombre completo: "))

    print("")
    a.SetRut(input("Ingrese su rut: "))

    print("")
    print(f"Ingrese opcion segun su grado\n1.Licenciado\n2.Magister\n3.Doctorado")
    pregunt=int(input("Opción a elegir: "))
    if pregunt==1:
        a.SetGrado("Licenciado")
    if pregunt==2:
        a.SetGrado("Magister")
    if pregunt==3:
        a.SetGrado("Doctorado")

    print("Ingrese su fecha de inicio de su contrato de la siguiente manera: Día-Mes-A;o")
    a.SetInicio(input("Fecha de inicio: "))
    print("")

    a.SetSueldoBase(int(input("Ingrese su sueldo base sin signos: ")))
    print("")

    pregunta=int(input(f"Ingrese opcion segun tipo de jornada:\n1.Jornada Media\n2.Jornada Completa\nOpción: "))
    if pregunta==1:
        a.SetJornada("Media")
    if pregunta==2:
        a.SetJornada("Completa")
    a.Bono()
    print("")
    print(a)
    print("__________")
    
def Adjuntos(a):
    print("")
    a.SetNombre(input("Ingrese su nombre completo: "))

    print("")
    a.SetRut(input("Ingrese su rut: "))

    print("")
    print(f"Ingrese opcion segun su grado\n1.Licenciado\n2.Magister\n3.Doctorado")
    pregunt=int(input("Opción a elegir: "))
    if pregunt==1:
        a.SetGrado("Licenciado")
    if pregunt==2:
        a.SetGrado("Magister")
    if pregunt==3:
        a.SetGrado("Doctorado")

    print("")
    print("Ingrese su fecha de inicio de su contrato de la siguiente manera: Día-Mes-A;o")
    a.SetInicio(input("Fecha de inicio: "))

    print("")
    a.SetHoras(int(input("Ingrese cantidad de horas trabajadas: ")))
    a.Sueldo() 
    print("")
    print(a)
    print("__________")

menu=0
while menu==0:
    print('')
    print('Menu docente')
    print("")   
    print(f"Ingrese que opción desea ingresar:\n1.Docente regular\n2.Docente adjunto ")
    op2=int(input("Opción: "))
    if op2==1:
        Regulares(regular)
    if op2==2:
        Adjuntos(adjunto)
    
