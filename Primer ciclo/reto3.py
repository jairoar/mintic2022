# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:42:59 2021

@author: Jairo Rodriguez
"""
import os

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

#Usuario y password predefinido
user = 51658
pw = 85615


#Opciones para crear el menu recurrente
opcion_1 = "1. Cambiar contraseña"
opcion_2 = "2. Ingresar coordenadas actuales"
opcion_3 = "3. Ubicar zona wifi más cercana"
opcion_4 = "4. Guardar archivo con ubicación cercana"
opcion_5 = "5. Actualizar registros de zonas wifi desde archivo"
opcion_6 = "6. Elegir opción de menú favorita"
opcion_7 = "7. Cerrar sesión"
menu = [opcion_1, opcion_2, opcion_3, opcion_4, opcion_5, opcion_6, opcion_7]

acumulador = 0

#matriz de coordenadas RETO3
matriz_coordenadas = []
bandera_coordenada = False
bandera_dato_vacio = False
lat_superior = 10.462
lat_inferior = 9.757
long_oriente = -72.987
long_occidente = -73.623

#inicio del programa (RETO 1)
user_persona = int(input("Ingrese el usuario\n"))

if user_persona == user:
    pw_persona = int(input("Ingrese password\n"))
    if pw_persona == pw:
        #volver el usuario un string para extraer los elementos
        value = str(user_persona)
        #convertirlo a entero una vez se concatenan los strings
        first_term = int(value[2]+value[3]+value[4])
        #operaciones matematicas segundo termino
        second_term = (5*1)+(6+1+1)-8 #debe dar 5
        #lista que contiene el menu principal
        #verificar sesion iniciada
        verificador = int(input(f"{first_term} + {second_term}=" ))
        if (verificador == (first_term+second_term)):
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("Sesión iniciada")
            #Aqui empieza el menu (RETO 2)
            while(True):
                #contador de errores
                contador_errores = 0
                #imprimir el menu
                print(f"{menu[0]}\n{menu[1]}\n{menu[2]}\n{menu[3]}\n{menu[4]}\n{menu[5]}\n{menu[6]}\n")
                seleccion = int(input("Elija una opción\n"))
                if seleccion == 1:
                    intento_validacion = input("Ingrese password actual\n")
                    if (str(pw) == str(intento_validacion)):
                        pw = input("Ingrese nuevo password\n")
                        if (str(pw) == str(intento_validacion)):
                            print("Error")
                            break
                        #limpiar la consola
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print("Error")
                        break
                if seleccion == 2:
                    if (len(matriz_coordenadas) == 0):
                        for organizador_matriz in range(3):
                            latitud = input("Ingrese latitud\n")
                            #verificar que latitud no este vacio
                            if (len(latitud) == 0):
                                bandera_dato_vacio = True
                                break
                            else:
                                latitud = float(latitud)
                            #verificar que latitud cumpla los requisitos (5)
                            if (latitud > lat_superior or latitud < lat_inferior):
                                bandera_coordenada = True
                                break
                            longitud = input("Ingrese longitud\n")
                            #verificar que longitud no este vacio
                            if (len(longitud) == 0):
                                bandera_dato_vacio = True
                                break
                            else:
                                longitud = float(longitud)
                            #verificar que longitud cumpla los requisitos (5)
                            if (longitud > long_oriente or longitud < long_occidente):
                                bandera_coordenada = True
                                break
                            vector_coordenadas = [latitud, longitud]
                            matriz_coordenadas.append(vector_coordenadas)
                        if (bandera_coordenada == True):
                            print("Error coordenada")
                            break
                        if (bandera_dato_vacio == True):
                            print("Error")
                            break
                    else:
                        for i in range(0,3):
                            print(f"coordenada [latitud, longitud] {i+1} : {matriz_coordenadas[i]}")
                        #Mensaje coordenadas oriente y promedio (8) +grande Oriente +pequeno Occidente
                        coord_oriente = matriz_coordenadas[0][1]
                        identificador_oriente = 1
                        for i in range(0,3):
                            if matriz_coordenadas[i][1] > coord_oriente:
                                coord_oriente = matriz_coordenadas[i][1]
                                identificador_oriente = i+1
                        print(f"La coordenada {identificador_oriente} es la que está más al oriente")
                        #Coordenada promedio
                        acum_latitud = 0
                        acum_longitud = 0
                        for i in range(0,3):
                            acum_latitud += matriz_coordenadas[i][0]
                            acum_longitud += matriz_coordenadas[i][1]
                        promedio_latitud = acum_latitud/3
                        promedio_longitud = acum_longitud/3
                        print(f"La coordenada promedio es : [{promedio_latitud}, {promedio_longitud}]")
                        print("Presione 1,2 o 3 para actualizar la respectiva coordenadas")
                        print("presione 0 para regresar al menu")
                        indicador_actualizar = int(input());
                        #en caso de ser diferente de 0 a 3
                        if indicador_actualizar > 3 or indicador_actualizar < 0:
                            print("Error actualización")
                            break
                        #en caso de ser 1, 2 o 3
                        if indicador_actualizar == 1 or indicador_actualizar == 2 or indicador_actualizar == 3:
                            latitud = input("Ingrese latitud\n")
                            #verificar que latitud no este vacio
                            if (len(latitud) == 0):
                                print("Error coordenada")
                                break
                            else:
                                latitud = float(latitud)
                            #verificar que latitud cumpla los requisitos (5)
                            if (latitud > lat_superior or latitud < lat_inferior):
                                bandera_coordenada = True
                            longitud = input("Ingrese longitud\n")
                            #verificar que longitud no este vacio
                            if (len(longitud) == 0):
                                print("Error coordenada")
                                break
                            else:
                                longitud = float(longitud)
                            #verificar que longitud cumpla los requisitos (5)
                            if (longitud > long_oriente or longitud < long_occidente):
                                print("Error coordenada")
                                break
                            vector_coordenadas = [latitud, longitud]
                            matriz_coordenadas[indicador_actualizar - 1] = vector_coordenadas
                    
                if seleccion == 3:
                    print("Usted ha elegido la opción 3")
                    break
                if seleccion == 4:
                    print("Usted ha elegido la opción 4")
                    break
                if seleccion == 5:
                    print("Usted ha elegido la opción 5")
                    break
                if seleccion == 6:
                    acumulador = 0
                    favorito = int(input("Seleccione opción favorita\n"))
                    if favorito >= 1 and favorito <= 5:
                        ad_1 = int(input("Para confirmar por favor responda: Los tienes en las manos y los tienes en los pies y en seguida sabrás qué número es. La respuesta es:\n"))
                        if ad_1 == 5:
                            ad_2 = int(input("Para confirmar por favor responda: Hay un número que muy valiente se creía, pero al quitarle su cinturón todo su valor perdía. ¿Cuál era?. La respuesta es:\n"))
                            if ad_2 == 8:
                                #Reordenamiento del menu
                                menu.insert(0, menu[0][:2] + menu[favorito-1][2:])
                                del menu[favorito]
                                for i in range(1,5):
                                    menu[i] = str(i+1) + "." + menu[i][2:]
                                #limpiar la consola
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print("Error")
                        else:
                            print("Error")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Error")
                        break
                if seleccion == 7:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Hasta pronto")
                    break
                if seleccion != 1 and seleccion != 2 and seleccion != 3 and seleccion != 4 and seleccion != 5 and seleccion != 6 and seleccion != 7:
                    acumulador+=1
                    print("Error")
                    if (acumulador == 3):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Error")
                        break
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error") 