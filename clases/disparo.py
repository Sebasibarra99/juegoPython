import pygame

class Misil(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenMisil = pygame.image.load("METEORITOS/IMAGENES/misildef.png")
        self.rect = self.imagenMisil.get_rect()
        self.velocidadDisparo = 10
        self.rect.top = posy
        self.rect.left = posx

    def recorrido(self):
        self.rect.top -= self.velocidadDisparo
    def dibujar(self,superficie):
        superficie.blit(self.imagenMisil,self.rect)






















