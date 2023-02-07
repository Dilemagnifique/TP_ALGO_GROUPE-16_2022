# -*- coding:UTF-8 -*-

"""
Created on Mon Jan  4 21:30:43 2023

@author: GROUPE 16.  
"""

from abc import ABCMeta, abstractmethod
from math import pi, sqrt
class Geo_Form(metaclass = ABCMeta):
    @abstractmethod
    def perimetre():
        pass

    @abstractmethod
    def surface():
        pass
        
class Rectangle(Geo_Form):
    try:
        def __init__(self,N16, longueur, largeur):
            self.N16 = N16
            self.longueur = longueur
            self.largeur = largeur
        def perimetre(self):
            return 2*self.longueur + 2*self.largeur
        
        def surface(self):
            return self.longueur*self.largeur
    except:
        print("Parametres non pris en charge")

class Cercle(Geo_Form):  
    try:
        def __init__(self, N16, rayon):
            self.N16 = N16
            self.rayon = rayon
        def perimetre(self):
            return 2*pi*self.rayon
        def surface(self):
            return  pi*(self.rayon**2)
    except:
        print("Parametres non pris en charge")

class Triangle(Geo_Form):
    try:
        def __init__(self,N16, côtéA,côtéB,côtéC):
            self.Nt = Nt
            self.côtéB= côtéB
            self.côtéA = côtéA
            self.côtéC = côtéC
        def perimetre(self):
            return self.côtéB + self.côtéA + self.côtéC

        def surface(self):
            p = self.perimetre()/2
            Aire = sqrt(p*(p - self.côtéA)*(p - self.côtéB)*(p - self.côtéC))
            Aire = Aire.real
            return Aire
    except:
        print("Parametres non pris en charge veillez recommencer")
class Carre(Rectangle):
    try:
        def __init__(self,N16, côté):
            Rectangle.__init__(self, N16, côté, côté)
    except:
        print("Parametres non pris en charge veillez recommencer")

class TriangleRectangle(Triangle):
    try:
        def __init__(self,N16, base, hauteur):
            hyp = sqrt(base**2+hauteur**2)
            Triangle.__init__(self, N16, base, hauteur, hyp)
    except:
        print("Parametres non pris en charge veillez recommencer")

class GeoFigure():  
    try:
        def __init__(self):
            self.gGeo_rep = []
        def add(self, fig):
            self.gGeo_rep.append(fig)
        
    except:
        print("Parametres non pris en charge veillez recommencer")

def tout_perimetre(obj):
    return obj.perimetre()

def tout_superficie(obj):
    return obj.surface()
    
def decris_toi(obj):
    print("Je suis {} \nMon perimetre : {} \nMa surface : {}".format(obj.N16, tout_perimetre(obj) ,tout_superficie(obj)))