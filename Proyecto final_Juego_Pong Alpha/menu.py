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

# Colores
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)

# Fuente
fuente_titulo = pygame.font.SysFont(None, 50)
fuente_botones = pygame.font.SysFont(None, 50)

# Coordenadas de los botones
x_boton_jugar = ancho_pantalla / 2 - 100
y_boton_jugar = 250
x_boton_salir = ancho_pantalla / 2 - 100
y_boton_salir = 350

# Fuente
fuentebot = pygame.font.SysFont(None, 25, bold=True)
# Coordenadas del botón "Atrás"
x_atras = 0
y_atras = 0

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
                subprocess.run(['python3', 'pong.py'])

            if x_boton_salir <= evento.pos[0] <= x_boton_salir + 200 and y_boton_salir <= evento.pos[1] <= y_boton_salir + 50:
                # Abrir el programa bot.py
                subprocess.run(['python3', 'bot.py'])


            if evento.type == pygame.MOUSEBUTTONDOWN:
                if x_atras <= evento.pos[0] <= x_atras + 20 and y_atras <= evento.pos[1] <= y_atras + 20:
                    # Acción al hacer clic en "Atrás"
                    pygame.quit()
                    sys.exit()
            

    # Dibujar el fondo negro
    pantalla.fill(COLOR_NEGRO)

    # Dibujar el botón "Atrás"
    atras = fuentebot.render("←", True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_atras, y_atras, 25, 25))
    pantalla.blit(atras, (x_atras, y_atras))

    # Dibujar el título "Pong"
    titulo = fuente_titulo.render("Selecciona un modo de juego", True, COLOR_BLANCO)
    pantalla.blit(titulo, (ancho_pantalla/2 - titulo.get_width()/2, 100))

    # Dibujar el botón "Jugar"
    boton_jugar = fuente_botones.render("P VS P", True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_boton_jugar, y_boton_jugar, 200, 50))
    pantalla.blit(boton_jugar, (ancho_pantalla/2 - boton_jugar.get_width()/2, y_boton_jugar + 10))

    # Dibujar el botón "Salir"
    boton_salir = fuente_botones.render("VS PC", True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_boton_salir, y_boton_salir, 200, 50))
    pantalla.blit(boton_salir, (ancho_pantalla/2 - boton_salir.get_width()/2, y_boton_salir + 10))

    # Actualizar la pantalla
    pygame.display.flip()
