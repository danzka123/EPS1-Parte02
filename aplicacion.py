# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:45:43 2022

@author: Kevin Pinedo
"""

def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido
def menu():
    print("\n*********Datos Persona***********")
    print("1. Listar persona")
    print("2. Agregar persona")
    print("3. Salir")
contador = 1
def salir():
    print("\nGracias... Vuelva pronto")  

def validar(a):
    
    usuario = leer_archivo('login.txt')
    contraseña = leer_archivo('clave.txt')
    numero = a
    
    print("\n\n*********LOGIN***********")
        
    dato1 = input('\nIngrese usuario: ')
    dato2 = input('Ingrese la clave: ')
    
    if numero <= 2:
        if usuario == dato1 and contraseña == dato2:
             print("\n¡BIENVENIDO AL PROGRAMA!\n")             
             menu()
                     
        else:            
            print("\n*Usuario y/o clave incorrectos...*\n")               
            contador = numero+1                
            validar(contador)
         
    else:
          print("\n***Ha sobrepasado el número de intentos. BYE :D...***\n")
          salir()
        
validar(1)
