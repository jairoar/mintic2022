# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:42:59 2021

@author: Jairo Rodriguez
"""

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

user = 51658
pw = 85615

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
        #verificar sesion iniciada
        verificador = int(input(f"{first_term} + {second_term}=" ))
        if (verificador == (first_term+second_term)):
            print("Sesión iniciada")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")