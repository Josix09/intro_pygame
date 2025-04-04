# importamos la libreria pygame

import pygame
import random

#inicializamos los modulos de pygame

pygame.init()

#establecer titulo a la ventana
pygame.display.set_caption("surface")
#establecemos las dimensiones de la ventana
ventana=pygame.display.set_mode(size=(300,300), flags = pygame.RESIZABLE)

#definimos un color
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)

color_aleatorio=(red,green,blue)

#creamos una superficie
color_aleatorio_superficie = pygame.display.get_surface


#rellenamos la superficie de azul
color_aleatorio_superficie.fill(color_aleatorio)

# inserto o muevo la superficie en la ventana
ventana.blit(color_aleatorio_superficie, (100,100))


# actualizala visualización de la ventana
pygame.display.flip()

# bucle del juego

while True:
    event=pygame.event.wait()
    if event.type == pygame.event.QUIT:
        break

pygame.quit()

