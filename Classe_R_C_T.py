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
