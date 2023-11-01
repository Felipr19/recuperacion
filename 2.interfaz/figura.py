from punto import Punto
from math import pi
import pygame

class Figura:

    def __init__(self, punto1, punto2):
        self.origen = punto1
        self.fin = punto2
        self.area = 0
        self.perimetro = 0
    
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def informar_popiedades(self):
        print("tipo de figura ",str(type(self)).split(".")[1][:-2])
        print(f"el area es {self.area}")
        print(f"el perimetro es {self.perimetro}")

    def dibujar(self):
        pass

class Cuadrado(Figura):
    
    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.area = lado * lado
    
    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.perimetro= lado * 4
    
    def dibujar(self,pantalla):
        rect = pygame.Rect((self.origen.x, self.origen.y) , (self.fin.x, self.fin.y))
        pygame.draw.rect(pantalla,'black',rect)

class Rectangulo(Figura):
    
    def calcular_area(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x , self.origen.y))
        altura = self.origen.calcular_distancia(Punto(self.origen.x , self.fin.y))
        self.area = base * altura

    def calcular_perimetro(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x , self.origen.y))
        altura = self.origen.calcular_distancia(Punto(self.origen.x , self.fin.y))
        self.perimetro = 2*(base+altura)

    def dibujar(self,pantalla):
        rect = pygame.Rect((self.origen.x, self.origen.y) , (self.fin.x, self.fin.y))
        pygame.draw.rect(pantalla,'black',rect)


class Triangulo(Figura):
    
    def calcular_area(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x , self.origen.y))
        altura = self.origen.calcular_distancia(Punto(self.origen.x , self.fin.y))
        self.area = (base * altura)/2

    def calcular_perimetro(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x , self.origen.y))
        altura = self.origen.calcular_distancia(Punto(self.origen.x , self.fin.y))
        hipotenusa = self.origen.calcular_distancia(self.fin)
        self.perimetro = base + altura + hipotenusa

    def dibujar(self,pantalla):
        pygame.draw.polygon(pantalla,'black', [(self.origen.x,self.origen.y), (self.origen.x, self.fin.y), (self.fin.x,self.fin.y)])


class Circulo(Figura):
    
    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.area = (radio**2) * pi

    def calcular_perimetro(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.perimetro = 2 * radio * pi

    def dibujar(self,pantalla):
        radio = self.origen.calcular_distancia(self.fin)
        pygame.draw.circle(pantalla,'black', (self.origen.x,self.origen.y), radio)