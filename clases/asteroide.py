import pygame

class Asteroide(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenAsteroide = pygame.image.load("METEORITOS/IMAGENES/asteroide.png")
        self.rect = self.imagenAsteroide.get_rect()
        self.velocidad = 10
        self.rect.top = posy
        self.rect.left = posx
        self.listaAsteroide = []

    def recorrido(self):
        self.rect.top += self.velocidad

    def dibujar(self,superficie):
        superficie.blit(self.imagenAsteroide,self.rect)





















