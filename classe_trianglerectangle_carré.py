class carre(rectangle):
    def __init__(self,coté):
        rectangle.__init__(self,long=coté,larg=coté)

class trianglerectangle(triangle):
    def __init__(self,base,hauteur):
        triangle.__init__(self,CA=base,CB=hauteur,hauteur=hauteur,CC=sqrt(base**2+hauteur**2))
