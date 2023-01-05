# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:16:32 2023 
@author: 
    Groupe16 :
        LABULU IBAM Danny
        ONKETU ANTEMBA Beni
       KABANGU MWATA Olivier
"""
"""RESOLUTION 8"""
from progr2_16 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, tout_perimetre, tout_superficie
if __name__ == '__main__':
    try:
        for i in range (1,5):
            rectangle = Rectangle("Rectangle KABANGU1", 14, 7)
            print("*"*5)
            cercle = Cercle("Cercle ONKETU2", 14)
            print("*"*5)
            triangle = Triangle("Triangle LABULU3", 9, 6, 7)
            print("*"*5)
            carre = Carre("Carré VADA4", 6)
            print("*"*5)
            t_rectangle = TriangleRectangle("Triangle Rectangle DANNY5", 5, 7)
            print("*"*5)
            print("les résultats pour le polymorphisme\n")
            print("{} :\n Le perimetre est de : {} m \nSurface : {} u.s".format(rectangle.nomF, tout_perimetre(rectangle), tout_superficie(rectangle)))
            print("{} :\n Perimetre est de : {} m\nSurface : {}u.s".format(cercle.nomF, tout_perimetre(cercle), tout_superficie(cercle)))
            print("{} :\n Perimetre est de: {} m\nSurface : {}u.s".format(triangle.nomF, tout_perimetre(triangle), tout_superficie(triangle)))
            print("{} :\n Perimetre est de: {} m\nSurface : {}u.s".format(carre.nomF, tout_perimetre(carre), tout_superficie(carre)))
            print("{} :\n Perimetre est de: {} m\nSurface : {}u.s".format(t_rectangle.nomF, tout_perimetre(t_rectangle), tout_superficie(t_rectangle)))     
    except Exception:
        print("Parametres non pris en charge.")
print("          ")       

print("_"*50)
print("fin du programme:)!")
