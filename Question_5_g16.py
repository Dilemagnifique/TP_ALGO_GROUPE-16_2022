# -*- coding:UTF-8 -*-

"""
Created on Mon Jan  2 23:30:43 2023

@author: groupe 16
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
    try:
        def __init__(self, long, larg):
            self.long=long
            self.larg=larg
        def surface(self):
            return (self.long*self.larg)
        def perimetre(self):
            return(2*(self.long+self.larg))
    except:
        print("Parametres non pris en charge,veillez recommencer svp")
class cercle(formegeometrique):
    try:
        def __init__(self,rayon):
            self.rayon=rayon
        def surface(self):
            return(pi*(self.rayon)**2)
        def perimetre(self):
            return(pi*self.rayon*2)
    except:
        print("Parametres non pris en charge ,veillez recommencer svp")
class triangle(formegeometrique):
    try:
        def __init__(self,hauteur,CA,CB,CC):
            self.hauteur=hauteur
            self.CA=CA
            self.CB=CB
            self.CC=CC
        def surface(self):
            return(self.CA*self.hauteur/2)
        def perimetre(self):
            return(self.CA+self.CB+self.CC)
    except:
            print("Parametres non pris en charge,veillez recommencer svp")

class carre(rectangle):
    try:
        def __init__(self,coté):
            rectangle.__init__(self,long=coté,larg=coté)
    except:
            print("Parametres non pris en charge,veillez recommencer svp")
class trianglerectangle(triangle):
    try:
        def __init__(self,base,hauteur):
            triangle.__init__(self,CA=base,CB=hauteur,hauteur=hauteur,CC=sqrt(base**2+hauteur**2))
    except:
            print("Parametres non pris en charge,veillez recommencer svp")
class nouvelleformegeometrique():
    try:
        def __init__(self,forme: formegeometrique):
            self.nouvelleforme=forme
        def nouvellesurface(self):
         return(self.nouvelleforme.surface())
        def nouveauperimetre(self):
            return(self.nouvelleforme.perimetre())
    except:
            print("Parametres non pris en charge,veillez recommencer svp")
    olivier=cercle(8.6)
    print("la surface du cercle est", olivier.surface())
    print("le perimetre du cercle est", olivier.perimetre())
    kabangu = carre(9)
    print("la surface du carré est de ", kabangu.surface())
