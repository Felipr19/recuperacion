from math import sqrt

class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def informar_cordenadas(self):
        print(f"x = {self.x} , y = {self.y}")

    def calcular_distancia(self,Punto):
        return(sqrt((self.x - Punto.x)**2 + (self.y - Punto.y)**2))
    
    
if __name__ == "__main__":
    p1=Punto(0,0)
    p2=Punto(5,5)

    p1.informar_cordenadas()
    p2.informar_cordenadas()

    print(p1.calcular_distancia(p2))    