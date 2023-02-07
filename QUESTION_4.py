# -*- coding:UTF-8 -*-

"""
Created on Mon Jan  2 23:30:43 2023

@author:GROUPE 16
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


class triangle(formegeometrique):
    def __init__(self,hauteur,CA,CB,CC):
        self.hauteur=hauteur
        self.CA=CA
        self.CB=CB
        self.CC=CC
    def surface(self):
        return(self.CA*self.hauteur/2)
    def perimetre(self):
        return(self.CA+self.CB+self.CC)
class carre(rectangle):
    def __init__(self,coté):
        rectangle.__init__(self,long=coté,larg=coté)
class trianglerectangle(triangle):
    def __init__(self,base,hauteur,hypoténuse):
        triangle.__init__(self,CA=base,CB=hauteur,hauteur=hauteur,CC=hypoténuse)
print("*TESTE DU PROGRAMME*")
print("_"*20)
L =triangle (2,5,6,9)
print("  *RESULTAT TRIANGLE* ")
print("la surface du triangle est de ", L.surface(),"u.s")
print("le perimetre du triangle est de ", L.perimetre(),"m")
print("    _fin du test de la classe  triangle_   ")
print("*"*90)
K =carre (9)
print("    *RESULTAT CARRE*   ")
print("la surface du carré est de ", K.surface(),"u.s")
print("le perimetre du carré est de ", K.perimetre(),"m")
print("    _fin du test de la classe  carré_   ")
print("*"*90)
O =trianglerectangle (9,2,3)
print("    *RESULTAT TRIANGLERECTANGLE*   ")
print("la surface du trianglerectangle est de ", O.surface(),"u.s")
print("le perimetre du trianglerectangle est de ", O.perimetre(),"m")
print("    _fin du test de la classe  trianglerectangle_   ")
print("*"*90)
