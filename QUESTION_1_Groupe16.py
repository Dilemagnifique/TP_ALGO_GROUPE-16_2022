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
