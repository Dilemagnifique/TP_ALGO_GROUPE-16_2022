# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:16:32 2023 TP ALGO PROJET 1
@author: 
    Groupe16 :
        LABULU IBAM Danny
        ONKETU ANTEMBA Beni
       KABANGU MWATA Olivier
"""
"""REPONSE 7"""
from PROJET_1_Groupe16 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, GeoFig

if __name__ == '__main__':
    print("Depuis les classes seules :")
    print()
    try:
        for i in range (1,501):
            rectangle = Rectangle("Rectangle K1", 12+i, 7)
            cercle = Cercle("Cercle L2", 14)
            triangle = Triangle("Triangle M3", 9, 6, 7)
            carre = Carre("Carré Z4", 6)
            t_rectangle = TriangleRectangle("Triangle Rectangle I5", 5, 7)
        
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
    
    print("_"*50)
    print("*"*50)
    print("    *COMMENCER A PARTIR DE LA CLASSE GLOBALE*     : ")
    print("_"*50)
    for i in range (1,501):
        figureA = GeoFig() 
        figureB = GeoFig() 
        figureC = GeoFig()
        figureD = GeoFig()
        figureE = GeoFig()
        
        figureA.add(Rectangle("Rectangle K1", 12, 5))
        figureB.add(Cercle("Cercle L2", 5))
        figureC.add(Triangle("Triangle M3", 9, 6, 7))
        figureD.add(Carre("Carré Z4", 10))
        figureE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
        
        figureA.decris_toi()
        figureB.decris_toi()
        figureC.decris_toi()
        figureD.decris_toi()
        figureE.decris_toi()
        
        try:
            figureA.add(Rectangle("Rectangle K1", 12, 5))
            figureB.add(Cercle("Cercle L2", 5))
            figureC.add(Triangle("Triangle M3", 9, 6, 7))
            figureD.add(Carre("Carré Z4", 10))
            figureE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
            
            figureA.decris_toi()
            figureB.decris_toi()
            figureC.decris_toi()
            figureD.decris_toi()
            figureE.decris_toi()
        except Exception:
            print("Parametres non pris en charge.")

print("Apres execution le temps d'excès est de : ",elaps)
