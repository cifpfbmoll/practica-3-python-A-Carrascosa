#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


producto = input("Que producto quieres comprar?\n > ")
precio = int(input("Cuanto cuesta el producto?\n > "))

iva = precio * 21 / 100

final = precio + iva

print("\n >>> El producto %s con un 21 de IVA cuesta %d" % (producto, final))