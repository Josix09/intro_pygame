import pygame
import sys
import random
import math
color_ventana = (255, 255, 255)
negro = (0, 0, 0)
gris1=(128, 128, 128)
gris2=(137, 137, 137)
gris3=(112,112,112)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (225,225,225)
naranja = (255,165,0)
cian = (0, 255, 255)
cafe= (63, 30, 12)


PI= math.pi

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("lineas aleatorias")

clock = pygame.time.Clock()
while 1:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(cian)
    fuente_area = pygame.font.SysFont("arial", 35, 1, 1)
    texto = fuente_area.render("Colegio Guanenta", 1, negro)
    ventana.blit(texto, (100, 0))

    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("esp. sistemas", 1, negro)
    ventana.blit(texto, (150, 30))

    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("Jorge Silva", 1, negro)
    ventana.blit(texto, (0, 475))

    #rectangulo (bordes de la imagen)
    pygame.draw.rect(ventana, negro, ((50, 100), (400, 340)), 1)
    #tren
    pygame.draw.rect(ventana, gris3, (150,280, 270,100))
    pygame.draw.rect(ventana, gris1, (300, 200, 100,80))
    pygame.draw.rect(ventana, negro, (270, 150, 150,50))
    pygame.draw.rect(ventana, negro, (300, 130, 90,30))
    pygame.draw.rect(ventana, rojo, (300, 210, 100,60))
    pygame.draw.circle(ventana,gris3,(150,330),50,100)
    pygame.draw.rect(ventana,gris2,(130,280,20,100))
    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("Sangil Express", 1, negro)
    ventana.blit(texto, (170,300))
    #ruedas
    pygame.draw.circle(ventana, negro , (180,400),35,60)
    pygame.draw.circle(ventana, negro , (390,400),35,70)
    pygame.draw.circle(ventana, negro , (320,400),35,70)
    pygame.draw.circle(ventana, negro , (250,400),35,60)
    

    pygame.draw.rect(ventana, rojo, (207, 220, 55,20))
    pygame.draw.rect(ventana, negro, (215, 240, 40,40))
    #suelo
    pygame.draw.rect(ventana,verde,(0,420,500,60))

    #cara
    pygame.draw.circle(ventana,amarillo,(350,240),35,70)
    #ojos
    pygame.draw.circle(ventana,blanco,(335,230),10,70)
    pygame.draw.circle(ventana,blanco,(370,230),10,70)
    #pupilas
    pygame.draw.circle(ventana,negro,(335,230),5,70)
    pygame.draw.circle(ventana,negro,(370,230),5,70)
    pygame.draw.arc(ventana,negro, (350, 245, 20,20 ), PI/-0.5, PI, 1)
    #gorro
    pygame.draw.rect(ventana,cafe,(320,200,60,15))
 
    pygame.display.flip()