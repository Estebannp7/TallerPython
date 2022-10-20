#se crea la funcion
opcion=100
ciclista={}
    
ciclistas=[]
def agregarCiclista():
    ciclista['Nombre']= input ("Digite el nombre del  ciclista: ")
    ciclista['Edad']= int(input ("Digite la edad del  ciclista: "))
    ciclista['Pais']= input ("Digite el pais del  ciclista: ")
    ciclista['Equipo']= input ("Digite el equipo del  ciclista: ")
    ciclista['Tiempo']= int(input ("Digite el tiempo en minutos del  ciclista: "))
    
    ciclistas.append(ciclista)

    def verResultados():
        print(ciclistas)
        tiempoFinal=0
        for ciclista in ciclistas:

            if(ciclista['Tiempo']< tiempoFinal ):
                    tiempoFinal = ciclista['Tiempo'] 
                    
        
    
    

    
    



print("*****Tour De Francia****")
print("1. Agregar Ciclista")
print("2. Ver resultado ")
print("0. salir")
while (opcion!=0):
        opcion=int(input("Digite su opcion: "))

        if(opcion==1):
            agregarCiclista()
            
        elif(opcion==2):
            verResultados() 
            
        elif(opcion==0):
            break    
       


    