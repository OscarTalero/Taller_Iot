#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:20:17 2021
@author: Oscar Talero
"""
#---------------- Zona librerias------------
import smarth_home as sh


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

lista_datos = 'electrico,luces,OFF@sensor,humedad,ON@alarma,movimiento,ON'


lista_separada = sh.separar_cadenas(lista_datos)
print(sh.calcular_estadisticas(lista_separada))
