
# -*- coding:UTF-8 -*-

"""
Created on Mon Jan  2 23:30:43 2023

@author: OLIVIER KABANGU 
"""
from abc import ABC, abstractmethod

class formegeometrique(ABC):
    @abstractmethod
    def Surface(self):
        pass
    def Perimetre(self):
        pass
