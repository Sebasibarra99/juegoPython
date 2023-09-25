import pygame
from clases import disparo

class Nave (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("METEORITOS/IMAGENES/navefinal.png")
        self.imagenDestruida = pygame.image.load("METEORITOS/IMAGENES/fuego.png")
        #TOMAR RECTANGULO DE NAVE
        self.rect = self.imagenNave.get_rect()
        #POSICION INCIAL DE LA NAVE
        self.rect.centerx = 516
        self.rect.centery = 500
        self.velocidad = 8
        self.vida = True
        self.listaDisparo = []
        self.sonidoDisparo = pygame.mixer.Sound("METEORITOS/sonidos/disparo.wav")
    def mover(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 1034:
                self.rect.right = 1034
    def dispara(self,x,y):
        if self.vida == True:
            misil = disparo.Misil(x,y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()
    def dibujar(self,superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave,self.rect)
        else:
            superficie.blit(self.imagenDestruida,self.rect)

















