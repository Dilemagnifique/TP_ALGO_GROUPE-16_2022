# -*- coding:UTF-8 -*-

"""
Created on Mon Jan  2 23:30:43 2023

@author: Danny LABULU,OLIVIER KABANGU 
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
