import pygame
import sys
import subprocess

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ancho_pantalla = 800
alto_pantalla = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Pong')

ms = pygame.mixer.Sound("fondo.mp3")
ms.set_volume(0.2)
ms.play(-1)

# Colores
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)

# Fuente
fuente_titulo = pygame.font.SysFont(None, 70, bold=True)
fuente_botones = pygame.font.SysFont(None, 50)

# Coordenadas de los botones
x_boton_jugar = ancho_pantalla / 2 - 100
y_boton_jugar = 250
x_boton_salir = ancho_pantalla / 2 - 100
y_boton_salir = 450
x_instru = ancho_pantalla / 2 - 100
y_instru = 350



# Loop del juego
while True:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if x_boton_jugar <= evento.pos[0] <= x_boton_jugar + 200 and y_boton_jugar <= evento.pos[1] <= y_boton_jugar + 50:
                # Abrir el programa pong.py
                subprocess.run(['python3', 'menu.py'])
            if x_instru <= evento.pos[0] <= x_instru + 200 and y_instru <= evento.pos[1] <= y_instru + 50:
                # Abrir el programa instru.py
                subprocess.run(['python3', 'instru.py'])
            elif x_boton_salir <= evento.pos[0] <= x_boton_salir + 200 and y_boton_salir <= evento.pos[1] <= y_boton_salir + 50:
                # Acción al hacer clic en "Salir"
                pygame.quit()
                sys.exit()

    # Dibujar el fondo negro
    pantalla.fill(COLOR_NEGRO)

    # Dibujar el título "Pong"
    titulo = fuente_titulo.render("Pong", True, COLOR_BLANCO)
    pantalla.blit(titulo, (ancho_pantalla/2 - titulo.get_width()/2, 100))

    # Dibujar el botón "Jugar"
    boton_jugar = fuente_botones.render("Jugar", True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_boton_jugar, y_boton_jugar, 200, 50))
    pantalla.blit(boton_jugar, (ancho_pantalla/2 - boton_jugar.get_width()/2, y_boton_jugar + 10))

    # Dibujar el botón "Instrucciones"
    boton_instru = fuente_botones.render("Como jugar", True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_instru, y_instru, 200, 50))
    pantalla.blit(boton_instru, (ancho_pantalla/2 - boton_instru.get_width()/2, y_instru + 10))

    # Dibujar el botón "Salir"
    boton_salir = fuente_botones.render("Salir", True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_boton_salir, y_boton_salir, 200, 50))
    pantalla.blit(boton_salir, (ancho_pantalla/2 - boton_salir.get_width()/2, y_boton_salir + 10))

    # Actualizar la pantalla
    pygame.display.flip()
