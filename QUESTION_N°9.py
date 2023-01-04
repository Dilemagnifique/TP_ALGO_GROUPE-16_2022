# -*- coding:UTF-8 -*-

"""
Created on Mon Jan  2 23:30:43 2023

@author: GROUPE 16  
"""
"""ce programme , nous servira de calculer les perimetre et surface des differentes figures en utilisant une autre methode (nouvelle impementation)
vu nous avons déjà la connaissance sur les  figures géometrique dans la première implementation ,nous pouvons directement calculer leurs sufaces et perimetre"""
import math
from math import pi
from math import sqrt
from abc import ABC, abstractmethod
#la classe créée ci-dessous (formegeometrique) est une classe abstraite 
class formegeometrique(ABC):
    @abstractmethod
    def Masurface(self):
        pass

    @abstractmethod
    def Monperimetre(self):
        pass
    #A présentnous allons créér une classe rectangle qui calculera le perimetre et la surface de rectangle 
class rectangle(formegeometrique):
    def __init__(self, long, larg):
        self.long=long
        self.larg=larg
    def Masurface(self):
        return (self.long*self.larg)
    def Monperimetre(self):
        return(2*(self.long+self.larg))
 #A présentnous allons créér une classe cercle qui calculera le perimetre et la surface du cercle
class cercle(formegeometrique):
    def __init__(self,rayon):
        self.rayon=rayon
    def Masurface(self):
        return(pi*(self.rayon)**2)
    def Monperimetre(self):
        return(pi*self.rayon*2)
 #A présentnous allons créér une classe triangle qui calculera le perimetre et la surface du triangle 
class triangle(formegeometrique):
    def __init__(self,hauteur,CA,CB,CC):
        self.hauteur=hauteur
        self.CA=CA
        self.CB=CB
        self.CC=CC
    def surface(self):
        return(self.cotéa*self.hauteur/2)
    def Monperimetre(self):
        return(self.cotéa+self.cotéb+self.cotéc)

class carre(rectangle):
    def __init__(self,coté):
        rectangle.__init__(self,long=coté,larg=coté)
 #A présentnous allons créér une classe trianglerectangle qui calculera le perimetre et la surface de trianglerectangle 
class trianglerectangle(triangle):
    def __init__(self,base,hauteur):
        triangle.__init__(self,cotéa=base,cotéb=hauteur,hauteur=hauteur,cotéc=sqrt(base**2+hauteur**2))

def perimetre_et_surf(form):
    perimetre = form.perimetre()
    surface =  form.surface()
    print("Le périmètre de notre figure est de {} UL et sa surface est de {} US".format(perimetre, surface))
#Affichage des resultats.
#fin du progrmme !