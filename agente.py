#Creación de la función para el funcionamiento del agente autónomo
def comedero_mascota():
    #Inicializar el estado_meta
    #Lleno=0; Vacio=1
    estado_meta = {'7am': '0', "12pm": '0', '7pm': '0'}
    costo = 0 #El costo inicializa en 0
    #El usuario ingresa la hora (locaciòn) para revisar el comedero para mascosats
    ingrese_hora = input("Ingrese la hora programada: ")
    ingrese_estado = input("Ingrese el estado del comedero para mascotas a las: "+ingrese_hora+" ")#El usuario ingresa el estado del comedero: lleno o vacio

    if (ingrese_hora == '7am'):#El usuario ingresa las horas programadas
        estado_hora2 = input("Ingrese el estado de la hora programada: ")#El usuario ingresa el estado del comedero: lleno o vacio
        estado_hora3 = input("Ingrese el estado de la hora programada: ")#El usuario ingresa el estado del comedero: lleno o vacio
        print("Meta Deseada:" + str(estado_meta))#Se muestran los resultados que se esperan
        #Muestra el horario en el que se encuentra el comedero para mascotas
        print("El comedero para mascotas se encuentra en el horario 7am")
        if(ingrese_estado == '1'):#Si el comedero para mascotas a las 7am se encuentra vacio
            print("El comedero para mascotas a las 7am esta vacio")#Muestra mensaje de que el comedero para mascotas esta vacio a las 7am
            estado_meta['7am'] ='0' #El comedero de mascotas debe llenarse
            costo += 1 #El costo aumentara cada vez que el comedero cambie de estado, es decir de estar vacio pase a estar lleno
            print("El comedero para mascotas se esta llenando a las 7am")#Muestra que el comedero para mascotas se esta llenando a esa hora
            print("El costo actual es: " +str(costo)) #Muestra el costo actual 
                
            if(estado_hora2 == '1'):#Si el comedero para mascotas a las 12pm se encuentra vacio
                print("El comedero para mascotas a las 12pm esta vacio")#Muestra mensaje de que el comedero para mascotas esta vacio a las 12pm
                print("El comedero de mascotas avanza a las 12pm") 
                costo += 1 #Incrementa el costo por avanzar a las 12pm
                print("El costo actual es: " +str(costo)) #Muestra el costo actual
                estado_meta['12pm'] ='0'#El comedero para mascotas a la hora 12pm se llenara
                costo += 1 #El costo aumentara cada vez que el comedero cambie de estado, es decir de estar vacio pase a estar lleno
                print("El comedero para mascotas se esta llenando a las 12pm")#Muestra que el comedero para mascotas se esta llenando a esa hora
                print("El costo actual es: " +str(costo)) #Muestra el costo actual
            else:
                print("El comedero para mascotas a las 12pm esta lleno")#Cuando el comedero para mascotas se encuentra lleno
                print("Ninguna acción. El costo actual es: "  +str(costo))#El costo se mantiene
                
            if(estado_hora3 == '1'):#Si el comedero para mascotas a las 7pm se encuentra vacio
                print("El comedero para mascotas a las 12pm esta vacio")
                print("EEl comedero de mascotas avanza a las 7pm") 
                costo += 1 #Incrementa el costo dado que el comedero para mascotas avanza
                print("El costo actual es: " +str(costo)) #Muestra el costo actual
                estado_meta['7pm'] ='0'
                costo += 1 #El costo aumentara cada que el comedero para mascotas se llene
                print("El comedero para mascotas se esta llenando a las 7pm")#Muestra que el comedero para mascotas se esta llenando a esa hora
                print("El costo actual es: "  +str(costo)) #Muestra el costo actual 
            else:
                print("El comedero para mascotas a las 12pm esta lleno")#Cuando el comedero para mascotas se encuentra lleno
                print("Ninguna acción. El costo actual es: "  +str(costo))#El costo se mantiene
                