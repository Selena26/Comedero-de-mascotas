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
        ingrese_hora2 = input("Ingrese el estado de la hora programada: ")#El usuario ingresa el estado del comedero: lleno o vacio
        ingrese_hora3 = input("Ingrese el estado de la hora programada: ")#El usuario ingresa el estado del comedero: lleno o vacio
        print("Meta Deseada:" + str(estado_meta))#Se muestran los resultados