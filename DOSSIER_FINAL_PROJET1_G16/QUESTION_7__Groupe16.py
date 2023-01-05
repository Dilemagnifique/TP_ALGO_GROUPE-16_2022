# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:16:32 2023 
@author: 
    Groupe16 :
        LABULU IBAM Danny
        ONKETU ANTEMBA Beni
       KABANGU MWATA Olivier
"""
from module_5_g16 import *

if __name__=='__main__':
    """"batterie de test classe rectangle """
    print("la classe rectangle")
AONIBE=rectangle(9,4)
    
print("la surface du rectangle est ", AONIBE.surface(),"u.s")
print("le perimetre du rectangle est ", AONIBE.perimetre(),"m")
print("*"*90)
"""batterie de test classe cercle """
print("la classe cercle")
VADA=cercle(7)
   
print("la surface du cercle est ",VADA.surface(), "u.s")
print("le perimetre du cercle est ",VADA.perimetre(),"m")
print("*"*90)
"""batterie de test classe triangle """
print("la classe triangle")
KABANGU=triangle(8,9,4,6)
    
print("la surface du triangle est ",KABANGU.surface(),"u.s")
print("le perimetre du triangle est",KABANGU.perimetre(),"m")
print("*"*90)
print("la classe carre")
"""batterie de test classe carree"""
LABULU=carre(5)
    
print("la surface du carre est ",LABULU.surface(),"u.s")
print("le perimetre du carre est ",LABULU.perimetre(),"m")
print("*"*90)
"""batterie de test class triangle rectangle"""
print("la classe trianglerectangle")
ONKETU=trianglerectangle(8,7)
print("la surface du triangle rectangle égale",ONKETU.surface())
print("le perimetre du triangle rectangle égale",ONKETU.perimetre())
print("*"*90)
"""batterie de test nouvelle forme geometrique"""
print("la classe tout geoform")
K=nouvelleformegeometrique(triangle(7,6,9,4))
print("la surface du triangle est",K.nouvellesurface())
print("le perimetre du triangle est",K.nouveauperimetre())
print("*"*90)
