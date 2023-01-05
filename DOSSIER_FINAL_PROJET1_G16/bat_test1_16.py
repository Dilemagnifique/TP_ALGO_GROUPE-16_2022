# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:16:32 2023 
@author: 
    Groupe16 :
        LABULU IBAM Danny
        ONKETU ANTEMBA Beni
        KABANGU MWATA Olivier
"""
"""REPONSE 7"""
from progr1_16 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, GeoFig

if __name__ == '__main__':
    print("Depuis les classes seules :")
    print()
    try:
        for i in range (1,5):
            rectangle = Rectangle("Rectangle LABULU1", 12+i, 7)
            cercle = Cercle("Cercle KABANGU2", 14)
            triangle = Triangle("Triangle ONKETU3", 9, 6, 7)
            carre = Carre("Carré ANTEMBA4", 6)
            t_rectangle = TriangleRectangle("Triangle Rectangle MWATA5", 5, 7)
        
            rectangle.decris_toi()
            print()
            cercle.decris_toi()
            print()
            triangle.decris_toi()
            print()
            carre.decris_toi()
            print()
            t_rectangle.decris_toi()
            print()
    except Exception:
        print("Parametres non pris en considération.")
    
    print()
    print()
    print("On comme à partir la classe <Globale> : ")
    print()
    for i in range (1,2):
        figureA = GeoFig() 
        figureB = GeoFig() 
        figureC = GeoFig()
        figureD = GeoFig()
        figureE = GeoFig()
        
        figureA.add(Rectangle("Rectangle IBAM1", 12, 5))
        figureB.add(Cercle("Cercle DANNY2", 5))
        figureC.add(Triangle("Triangle BENI3", 9, 6, 7))
        figureD.add(Carre("Carré B4", 10))
        figureE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
        
        figureA.decris_toi()
        figureB.decris_toi()
        figureC.decris_toi()
        figureD.decris_toi()
        figureE.decris_toi()
        
        try:
            figureA.add(Rectangle("Rectangle OLIVIER1", 12, 5))
            figureB.add(Cercle("Cercle AONIB2", 5))
            figureC.add(Triangle("Triangle VADA3", 9, 6, 7))
            figureD.add(Carre("Carré DIL4", 10))
            figureE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
            
            figureA.decris_toi()
            figureB.decris_toi()
            figureC.decris_toi()
            figureD.decris_toi()
            figureE.decris_toi()
        except Exception:
            print("Parametres non pris en charge.")
print(" *Fin du programme:)* ")
        
