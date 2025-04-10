import pygame
import sys
import random

verde=(45, 87, 44)

r = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
a = random.randint(50,400)
b = random.randint(100,400)
c = random.randint(50,400)
d = random.randint(100,400)
blanco = (255, 255, 255)

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("dibujar formas con pygame")

clock = pygame.time.Clock()
while 1:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ventana.fill(verde)

    fuente_area = pygame.font.SysFont("arial", 35, 1, 1)
    texto = fuente_area.render("colegio guenenta", 1, blanco)
    ventana.blit(texto, (100, 0))

    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("esp. sistemas", 1, blanco)
    ventana.blit(texto, (150, 30))

    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("Jorge Silva", 1, blanco)
    ventana.blit(texto, (0, 475))

    pygame.draw.rect(ventana, blanco, ((50, 50), (400, 400)), 1)

    pygame.draw.line(ventana, r, (a, b), (c, d))

    pygame.display.flip()