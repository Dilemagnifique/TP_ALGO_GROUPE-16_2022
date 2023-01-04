# -*- coding:UTF-8 -*-

"""
Created on Mon Jan  2 23:30:43 2023

@author: Danny LABULU 
"""
from abc import ABC, abstractmethod
from math import pi
from math import sqrt
class formegeometrique(ABC):
    @abstractmethod
    def surface(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass
class rectangle(formegeometrique):
    def __init__(self, long, larg):
        self.long=long
        self.larg=larg
    def surface(self):
        return (self.long*self.larg)
    def perimetre(self):
        return(2*(self.long+self.larg))

class cercle(formegeometrique):
    def __init__(self,rayon):
        self.rayon=rayon
    def surface(self):
        return(pi*(self.rayon)**2)
    def perimetre(self):
        return(pi*self.rayon*2)

class triangle(formegeometrique):
    def __init__(self,hauteur,CA,CB,CC):
        self.hauteur=hauteur
        self.CA=CA
        self.CB=CB
        self.CC=CC
    def surface(self):
        return(self.cotéa*self.hauteur/2)
    def perimetre(self):
        return(self.CA+self.CB+self.CC)

class carre(rectangle):
    def __init__(self,coté):
        rectangle.__init__(self,long=coté,larg=coté)

class trianglerectangle(triangle):
    def __init__(self,base,hauteur):
        triangle.__init__(self,CA=base,CB=hauteur,hauteur=hauteur,CC=sqrt(base**2+hauteur**2))

class nouvelleformegeometrique():
    def __init__(self,forme: formegeometrique):
        self.nouvelleforme=forme
    def nouvellesurface(self):
        return(self.nouvelleforme.surface())
    def nouveauperimetre(self):
        return(self.nouvelleforme.perimetre())

    Cr=cercle(8)
    print("la surface du cercle est",Cr.surface())
    print("le perimetre du cercle est",Cr.perimetre())
