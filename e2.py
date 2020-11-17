#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Pida al usuario el espacio recorrido por un coche y el tiempo que ha tardado
# en horas y que calcule a qué velocidad media había realizado el recorrido.

espacio = int(input("Inserta el espacio recorrido en km:\n> "))
tiempo = int(input("Inserta el tiempo transcurrido en horas:\n> "))

velocidad = espacio / tiempo

print("La velocidad del coche es de: %s km/h" % velocidad)