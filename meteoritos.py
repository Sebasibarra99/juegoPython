import pygame
from pygame.locals import *
import sys
import pygame.locals
from clases import jugador
from clases import asteroide
from random import randint
import time

#VARIABLES
ANCHO = 1034
ALTO = 547
listaAsteroide = []
puntos = 0
colorFuente = (120,200,40)
#booleano juego
jugando = True


#FUNCION PRINCIPAL
#CARGA DE ASTEROIDES
def cargarAsteroide(x,y):
    meteoro = asteroide.Asteroide(x,y)
    listaAsteroide.append(meteoro)

def gameOver():
    global jugando
    jugando = False
    for meteoritos in listaAsteroide:
        listaAsteroide.remove(meteoritos)

def meteroritos():
    tecla_izquierda_pulsada = False
    tecla_derecha_pulsada = False    
   
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    #IMAGEN DE FONDO
    fondo = pygame.image.load("METEORITOS/IMAGENES/asteroides.png")
    
    #TITULO
    pygame.display.set_caption("Meteoritos asesinos")
    #CREAR OBJETO DEL JUGADOR
    nave = jugador.Nave()
    contador = pygame.time.get_ticks()
    #SONIDOS
    pygame.mixer.music.load("METEORITOS/sonidos/fondo.wav")
    pygame.mixer.music.play(10)
    sonidoColision = pygame.mixer.Sound("METEORITOS/sonidos/colisionreal.wav")

    #FUENTE DEL MARCADOR
    fuenteMarcador = pygame.font.SysFont("Arial",20)
    #CICLO DE JUEGO
    while True:
        
        ventana.blit(fondo, (0,0))
        nave.dibujar(ventana)
        #TIEMPO
        tiempo = pygame.time.get_ticks()
        #MARCADOR
        global puntos
        textoMarcador = fuenteMarcador.render("Puntos: "+str(puntos),0,colorFuente)
        ventana.blit(textoMarcador,(0,0))
        #CREAR ASTEROIDES
        if tiempo - contador > 250:
            contador = tiempo
            posX = randint(2,990)
            cargarAsteroide(posX, 0)
        #COMPROBAR LISTA ASTEROIDES
        if len(listaAsteroide) > 0:
            for x in listaAsteroide:
                if jugando == True:
                    x.dibujar(ventana)
                    x.recorrido()
                if x.rect.top > 990:
                    listaAsteroide.remove(x)
                else:
                    if x.rect.colliderect(nave.rect):
                        listaAsteroide.remove(x)
                        sonidoColision.play()
                        #print("Colision nave / meteorito")
                        nave.vida = False
                        gameOver()
 
        #DISPARO DE NAVE
        if len(nave.listaDisparo) > 0:
            for x in nave.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top < -10:
                    nave.listaDisparo.remove(x)
                else:
                    for meteoritos in listaAsteroide:
                        if x.rect.colliderect(meteoritos):
                            listaAsteroide.remove(meteoritos)
                            nave.listaDisparo.remove(x)
                            puntos += 1
                            #print("Colision disparo / meteoro")
        nave.mover()



        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if jugando == True:
                    if evento.key == K_LEFT:
                        tecla_izquierda_pulsada = True
                    elif evento.key == K_RIGHT:
                        tecla_derecha_pulsada = True
                    elif evento.key == K_SPACE:
                        x,y = nave.rect.center
                        nave.dispara(x,y)
            elif evento.type == pygame.KEYUP:
                if evento.key == K_LEFT:
                    tecla_izquierda_pulsada = False
                if evento.key == K_RIGHT:
                    tecla_derecha_pulsada = False
        if tecla_izquierda_pulsada:
            nave.rect.left -= nave.velocidad
        elif tecla_derecha_pulsada:
            nave.rect.right += nave.velocidad    
        
        if jugando == False:
            fuenteGameOver = pygame.font.SysFont("Arial",40)
            textoGameover = fuenteGameOver.render("Game over",0,colorFuente)
            ventana.blit(textoGameover,(480,270))
            pygame.mixer.music.fadeout(3000)
        pygame.display.update()

#LLAMADA DE FUNCION PRINCIPAL
meteroritos()



















