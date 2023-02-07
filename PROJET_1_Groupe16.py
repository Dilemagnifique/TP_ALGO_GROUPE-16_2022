# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:16:32 2023 TP ALGO PROJET 1
@author: 
    Groupe16 :
        LABULU IBAM Danny
        ONKETU ANTEMBA Beni
       KABANGU MWATA Olivier
"""
"""SOLUTION N°1"""

from abc import ABCMeta, abstractmethod #importation du module abc qui gère les classes abstraites
from math import pi, sqrt #importation des fonctions pi et sqrt depuis la bibliothèque math de python 

class Geo_Form(metaclass = ABCMeta): #definition de la classe mère
    @abstractmethod     #mention d'appel pour rendre la methode abstraite
    def perimetre(): #methode abstraite pour perimetre sans retour
        pass

    @abstractmethod
    def surface():
        pass
    
    def decris_toi(self): #methode de la description complete d'une figure
        print("Pour la figure {}\nPerimetre : {}\nSurface : {}".format(self.nomf, self.perimetre(), self.surface()))

"""SOLUTION 2"""

#classe Retangle qui herite de la classe mère Geo_Form      
class Rectangle(Geo_Form): 
    try: #gestion des exceptions
        def __init__(self,nomf, longueur, largeur): #initialisation de la classe Rectangle avec nom, long, largueur
            #initialistation des variables internes de la classe
            self.nomf = nomf 
            self.longueur = longueur
            self.largeur = largeur
        #methode de calcul du perimetre
        def perimetre(self): 
            return 2*self.longueur + 2*self.largeur
        #methode de calcul de la surface
        def surface(self):
            return self.longueur*self.largeur
    except: #gestion des exceptions
        print("Parametres non pris en charge")

#classe Cercle qui herite de la classe mère Geometrie_Forme
class Cercle(Geo_Form):  
    try:
        def __init__(self, nomf, rayon):
            self.nomf = nomf
            self.rayon = rayon
        def perimetre(self):
            return 2*pi*self.rayon
        def surface(self):
            return  pi*(self.rayon**2)
    except:
        print("Parametres non pris en charge,veillez recommencer svp")

#classe Triangle qui herite de la classe mère Geo_Form 
class Triangle(Geo_Form):
    try:
        def __init__(self,nomf, CA,CB,CC):
            self.nomf = nomf
            self.CB = CB
            self.CA = CA
            self.CC = CC
        def perimetre(self):
            return self.CB + self.CA + self.CC

        def surface(self):
            p = self.perimetre()/2
            aire = sqrt(p*(p - self.CA)*(p - self.CB)*(p - self.CC))
            aire = aire.real
            return aire
    except:
        print("Parametres non pris en charge, veillez recommencer svp")

"""SOLUTION 4"""

#la classe Carre qui herite de la classe Retangle 
class Carre(Rectangle):
    try:
        def __init__(self,nomf, cote):
            Rectangle.__init__(self, nomf, cote, cote)
    except:
        print("Parametres non pris en charge ,veillez recommencer svp")

#la classe TriangleRectangle qui herite de la classe Triangle 
class TriangleRectangle(Triangle):
    try:
        def __init__(self,nomf, base, hauteur):
            hyp = sqrt(base**2+hauteur**2)
            Triangle.__init__(self, nomf, base, hauteur, hyp)
    except:
        print("Parametres non pris en charge ")

"""SOLUTION 5"""

#la classe GeoFig est la classe qui exploite d'autre classe.
class GeoFig():  
    try:
        def __init__(self):
            self.gGeo_rep = []
        def add(self, fig):
            self.gGeo_rep.append(fig)
        def decris_toi(self):
            for g in self.gGeo_rep:
                print("Pour la figure {}\nPerimetre : {}\nSurface : {}".format(g.nomF, g.perimetre(), g.surface()))
    except:
        print("Parametres non pris en charge")
        
