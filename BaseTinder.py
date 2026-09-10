def GuardarPersonas():

    nombre= input("Digite su nombre completo")
    edad= int (input("¿Que edad tienes?"))
    ciudad= input("¿De donde eres?")
    genero= input("Cual es tu genero?")
    gbusca= input("Que genero busca?")

     
    edadmin =int (input("Cual es la edad minima que buscas para tu futura cita?"))
    while edadmin < 18:
        print("Debe ser mayor de edad")
        edadmin = int (input("Por favor coloque una edad permitida"))
    
    edadmax = int (input("Cual es la edad maxima que buscas para tu futura cita?"))
    while 120 > edadmax:
        print("Estas buscando el ataud o que?")
        edadmax =input("Por favor coloque una edad permitida")
        edadmin or edadmax 

    distancia=input("Cuantos kilometros aceptas que este de distancia tu futura pareja?")

    individuo={"nombre":nombre,"edad":edad,"ciudad":ciudad,"genero":genero,"gbusca":gbusca,"edadmin":edadmin,"edadmax":edadmax,"distancia":distancia}
    return GuardarPersonas

def RegistrarPersonas():
    N=input("Cuantas personas vas a registrar?")
    for i in range (0,N):
       print("#i",i)
       print(usuario)
       usuario[i]= GuardarPersonas()
       
       

def main ():
    print ("----------------BIENVENIDO A TINDER CUN--------------")
    print ("La mejor plataforma para encontrar el amor")
    print ("")
    print ("--MENU--")
    print ("Por favor selecciona el numero de lo que quieres hacer")
    print ("")
    print ("1. Para registrar un nuevo usuario")
    print ("2. Mostrar personas registradas")
    print ("3. Buscar posibles coincidencias")
    print ("4. Mostrar el porcentaje de compatibilidad de cada coincidencia")
    print ("5. Mostrar los intereses que tienen en común")
    print ("6. Identificar cuál es la persona más compatible")
    print ("7. Mostrar las personas que no cumplen los requisitos mínimos de compatibilidad")
    print ("8. Consultar las coincidencias de cualquier persona registrada")
    menu=input()
    match menu:
        
        case "1":
         RegistrarPersonas()


main()
