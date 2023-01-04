# -*- coding:UTF-8 -*-

"""
Created on Mon Jan  2 23:30:43 2023

@author:groupe 16 
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
print(" *TEST DE LA CLASSE CERCLE* ")
C=cercle(5)
print("la surface du cercle est",C.surface(),"u.s")
print("le perimetre du cercle est",C.perimetre(),"m")
print("*"*50)
print(" *TEST DE LA CLASSE CARRE* ")
Ca=carre(7)
print("la surface du carré est de ",Ca.surface(),"u.s")
print("le perimetre du carré est de",C.perimetre(),"m")
print("*"*50)
print(" *TEST DE LA CLASSE RECTANGLE* ")
Re=rectangle(9,6)
print("la surface du RECTANGLE est de ",Ca.surface(),"u.s")
print("le perimetre du RECTANGLE est de",C.perimetre(),"m")
print("*"*50)
print(" *TEST DE LA CLASSE TRIANGLE* ")
Re=triangle(9,6,10,7)
print("la surface du TRIANGLE est de ",Ca.surface(),"u.s")
print("le perimetre du TRIANGLE est de",C.perimetre(),"m")
print("*"*50)
