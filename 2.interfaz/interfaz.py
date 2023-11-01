from figura import *
import sys
import pygame

class Interfaz:
    
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720

    def obtener_punto(self,screen):
        seleccionando = True
        p1=False

        while seleccionando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.circle(screen,'black', event.pos, 5)

                    if p1 == False:
                        coords = event.pos
                        punto1 = Punto(int(coords[0]),int(coords[1]))
                        p1 = True
                    else:
                        coords = event.pos
                        punto2 = Punto(coords[0],coords[1])
                        seleccionando = False
            
            pygame.display.flip()
        screen.fill("white")
        return punto1,punto2

    def iniciar(self):

        pygame.init()

        screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("interfaz figuras")
        screen.fill('white')
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        #Codigo principal de la interfaz

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:          #presionar espacio para elegir los puntos y reiniciar la pantalla
                    screen.fill('white')
                    punto1,punto2 = self.obtener_punto(screen)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:              #presionar c para dibujar circulo
                    c = Circulo(punto1,punto2)
                    c.dibujar(screen)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:              # r para rectangulo
                    r = Rectangulo(punto1,punto2)
                    r.dibujar(screen)
                
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:              # t para triangulo
                    t = Triangulo(punto1,punto2)
                    t.dibujar(screen)

                
                pygame.display.flip()    