#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:23:15 2021
@author: Oscar Talero
"""

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
from collections import namedtuple


def separar_cadenas(lista_datos):
    """ 
    Parameters
    ----------
    lista_datos:string
      Una cadena con los datos de todos los IoT de una smarth-home 
    Returns
    -------
    lista_IoT:[(namedtuple)]
      una lista de tuplas cada una de ellas con los datos de un dispositivo IoT     
    """  
   lista_t = []
   lista = lista_datos.split('@') #eliminamos el separador @
   for i in range(len(lista)):
       lista_uno = lista[i].split(',')  
       lista_t.append(lista_uno)
       lista_IoT = nombrar_tupla(lista_t)
   return lista_t


def nombrar_tupla(lista_t):
    """ 
    Parameters
    ----------
    lista_t:lista
        Una lista con los datos de todos los IoT de una smarth-home 
    Returns
    -------
    lista_IoT:[(namedtuple)]
        una lista de tuplas cada una de ellas con los datos de un dispositivo IoT     
    """  
    #creamos la nametupled para guardar los datos de los dispositivos
    Dispositivo = namedtuple('Dispositivo','tipo identificador estado') 
    lista_IoT = []
    for i in range(len(lista_t)):
        x,y,z = lista_t[i]
        #creamos los dispositivos y agragamos los datos
        dispositivo_crear = Dispositivo(x,y,z) 
        #creamos una lista que almacena las tuplas
        lista_IoT.append(dispositivo_crear) 
    return lista_IoT  
    
    
def calcular_estadisticas(lista_IoT):
    """ 
    Parameters
    ----------
    lista_IoT:[(namedtuple)]
      Una lista de tuplas con los datos de los dispositivos IoT 
      Returns
      -------
    estadistica:(total_on, total_off)
      una tupla con  el total de dispositivos IoT en estado ON y otra con el total de estado     
    """ 
    lista_on = []
    lista_off = []
    contador_on = 0
    contador_off = 0
    Tabla = """\
        +----------------------------------+
        | Tipo      Identificador   Estado |
        |----------------------------------|
        {}
        +----------------------------------+\
        """
    for i in range(len(lista_IoT)):
      if lista_IoT[i][2] == 'ON':
          contador_on += 1
          lista_on.append(lista_IoT[i])
      elif lista_IoT[i][2] == 'OFF':
              contador_off += 1
              lista_off.append(lista_IoT[i])
  
    tupla_on = tuple(lista_on)
    tupla_off = tuple(lista_off)
    print('Dispositivos que se encuentran en estado ON: ',contador_on)
    Tabla_on = (Tabla.format('\n'.join("| {:<10} {:<10} {:>10} |".format(*fila)for fila in tupla_on)))       
    print(Tabla_on,end = '\n''\n')    
    tupla_on = tuple(lista_on)
    print('Dispositivos que se encuentran en estado OFF: ',contador_off)
    Tabla_off = (Tabla.format('\n'.join("| {:<10} {:<10} {:>10} |".format(*fila)for fila in tupla_off)))       
    print(Tabla_off)       
    return 'FIN'
  
    
    
  
    
  
    
  
    