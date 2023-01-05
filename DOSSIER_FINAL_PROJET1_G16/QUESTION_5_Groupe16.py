# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:16:32 2023 
@author: 
    Groupe16 :
        LABULU IBAM Danny
        ONKETU ANTEMBA Beni
       KABANGU MWATA Olivier
"""

"""RESOLUTION 5"""

#classe GeoFig exploite toutes les autres classes de la Geometrie_Forme
class GeoFig():  
    try:
        def __init__(self):
            self.LGeo_rep = []
        def add(self, fig):
            self.LGeo_rep.append(fig)
        def decris_toi(self):
            for L in self.LGeo_rep:
                print("Resultat de la figure{}\nle Perimetre est de : {}m\nla Surface est de : {} u.s".format(L.nomF, L.perimetre(), L.surface()))
    except:
        print("Parametres non pris en charge")
        
