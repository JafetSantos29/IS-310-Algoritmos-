import pygame
import sys
import time

# Inicializar Pygame
pygame.init()
colision = pygame.mixer.Sound("colision.wav")
colision.set_volume(1.5)

# Dimensiones de la pantalla
ancho_pantalla = 800
alto_pantalla = 600

# Calcular la altura de las barras
alto_barra = int(alto_pantalla * 0.4)

# Crear la pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Pong')

# Colores
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)

# Coordenadas de las barras
x_barra_izquierda = 50
y_barra_izquierda = alto_pantalla / 2 - alto_barra / 2
x_barra_derecha = ancho_pantalla - 50 - 5
y_barra_derecha = alto_pantalla / 2 - alto_barra / 2

# Radio de los bordes redondos de las barras
radio_bordes = 10

# Coordenadas de la pelota
x_pelota = ancho_pantalla / 2
y_pelota = alto_pantalla / 2
radio_pelota = 20

# Velocidad de la pelota
velocidad_pelota_x = 0.5
velocidad_pelota_y = 0.5

# Velocidad de las barras
velocidad_barra_izquierda = 0
velocidad_barra_derecha = 0

# Tiempo de inicio del cronómetro
inicio_cronometro = pygame.time.get_ticks()

# Puntaje inicial
puntaje_jugador1 = 0
puntaje_jugador2 = 0

# Fuente para el texto del puntaje
fuente_puntaje = pygame.font.Font(None, 36)


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
            if x_atras <= evento.pos[0] <= x_atras + 20 and y_atras <= evento.pos[1] <= y_atras + 20:
                # Acción al hacer clic en "Atrás"
                pygame.quit()
                sys.exit()


     # Comprobar si la pelota ha salido de la pantalla en el eje x
    if x_pelota < 0:
        # Incrementar el puntaje del jugador 2
        puntaje_jugador2 += 1
        # Reubicar la pelota en la posición inicial
        x_pelota = ancho_pantalla // 2
        y_pelota = alto_pantalla // 2
        # Actualizar la velocidad de la pelota
        velocidad_pelota_x = -velocidad_pelota_x

    elif x_pelota > ancho_pantalla:
        # Incrementar el puntaje del jugador 1
        puntaje_jugador1 += 1
        # Reubicar la pelota en la posición inicial
        x_pelota = ancho_pantalla // 2
        y_pelota = alto_pantalla // 2
        # Actualizar la velocidad de la pelota
        velocidad_pelota_x = -velocidad_pelota_x

    # Mostrar puntajes en la pantalla
    fuente_puntaje = pygame.font.Font(None, 36)
    texto_puntaje = fuente_puntaje.render("Jugador 1: {}   Jugador 2: {}".format(puntaje_jugador1, puntaje_jugador2), True, COLOR_BLANCO)
    pantalla.blit(texto_puntaje, (ancho_pantalla / 2 - 100, 10))
    # Obtener el tiempo transcurrido desde el inicio del cronómetro
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - inicio_cronometro

    # Mostrar el contador en la pantalla
    if tiempo_transcurrido < 3000:  # Mostrar el contador durante 3 segundos
        contador = 3 - int(tiempo_transcurrido / 1000)  # Calcular el valor del contador
        fuente = pygame.font.Font(None, 100)
        texto = fuente.render(str(contador), True, COLOR_BLANCO)
        pantalla.blit(texto, (ancho_pantalla / 2 - 50, alto_pantalla / 2 - 50))
        pygame.display.flip()

    else:
        # Mover la pelota
        x_pelota += velocidad_pelota_x
        y_pelota += velocidad_pelota_y
        pygame.display.flip()



   

    # Rebotar la pelota en los bordes verticales
    if y_pelota <= 0 or y_pelota >= alto_pantalla - radio_pelota:
        velocidad_pelota_y *= -1
        colision.play()

    # Movimiento de la barra izquierda
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        velocidad_barra_izquierda = -1
    elif teclas[pygame.K_s]:
        velocidad_barra_izquierda = 1
    else:
        velocidad_barra_izquierda = 0

    # Movimiento de la barra derecha
    if teclas[pygame.K_UP]:
        velocidad_barra_derecha = -1
    elif teclas[pygame.K_DOWN]:
        velocidad_barra_derecha = 1
    else:
        velocidad_barra_derecha = 0

    # Colisión de la pelota con la barra izquierda
    if x_pelota - radio_pelota <= x_barra_izquierda + 5 and y_pelota >= y_barra_izquierda and y_pelota <= y_barra_izquierda + alto_barra:
        velocidad_pelota_x *= -1
        colision.play()

    # Colisión de la pelota con la barra derecha
    if x_pelota + radio_pelota >= x_barra_derecha and y_pelota >= y_barra_derecha and y_pelota <= y_barra_derecha + alto_barra:
        velocidad_pelota_x *= -1
        colision.play()

    # Actualizar las coordenadas de las barras
    y_barra_izquierda += velocidad_barra_izquierda
    y_barra_derecha += velocidad_barra_derecha

    # Verificar si algún jugador ha ganado
    if puntaje_jugador1 >= 10 or puntaje_jugador2 >= 10:
        ganador = ""
        if puntaje_jugador1 >= 10:
            ganador = "Jugador 1"
        else:
            ganador = "Jugador 2"
        
        # Mostrar mensaje de ganador en la pantalla
        fuente_ganador = pygame.font.Font(None, 36)
        texto_ganador = fuente_ganador.render("{} ha ganado!".format(ganador), True, COLOR_BLANCO)
        pantalla.blit(texto_ganador, (ancho_pantalla / 2 - 100, alto_pantalla / 2 - 50))
        
        # Mostrar botones de reiniciar y salir
        fuente_botones = pygame.font.Font(None, 24)
        texto_reiniciar = fuente_botones.render("Reiniciar", True, COLOR_BLANCO)
        texto_salir = fuente_botones.render("Salir", True, COLOR_BLANCO)
        pygame.draw.rect(pantalla, COLOR_NEGRO, (ancho_pantalla / 2 - 75, alto_pantalla / 2, 150, 30))
        pantalla.blit(texto_reiniciar, (ancho_pantalla / 2 - 40, alto_pantalla / 2 + 5))
        pygame.draw.rect(pantalla, COLOR_NEGRO, (ancho_pantalla / 2 - 75, alto_pantalla / 2 + 40, 150, 30))
        pantalla.blit(texto_salir, (ancho_pantalla / 2 - 20, alto_pantalla / 2 + 45))
        pygame.display.flip()



        # Esperar a que se presione alguno de los botones
        reiniciar = False
        salir = False
        while not reiniciar and not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = evento.pos
                    # Verificar si se ha presionado el botón de reiniciar
                    if ancho_pantalla / 2 - 75 <= x <= ancho_pantalla / 2 + 75 and alto_pantalla / 2 <= y <= alto_pantalla / 2 + 30:
                        reiniciar = True
                    # Verificar si se ha presionado el botón de salir
                    elif ancho_pantalla / 2 - 75 <= x <= ancho_pantalla / 2 + 75 and alto_pantalla / 2 + 40 <= y <= alto_pantalla / 2 + 70:
                        salir = True

        # Reiniciar el juego si se ha presionado el botón de reiniciar
        if reiniciar:
            # Restablecer las variables del juego
            puntaje_jugador1 = 0
            puntaje_jugador2 = 0
            # Resto del código para reiniciar el juego
            
        # Salir del juego si se ha presionado el botón de salir
        if salir:
            pygame.quit()
            sys.exit()




    # Dibujar el fondo negro
    pantalla.fill(COLOR_NEGRO)
    # Dibujar el botón "Atrás"
    atras = fuentebot.render("←", True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_atras, y_atras, 25, 25))
    pantalla.blit(atras, (x_atras, y_atras))

    # Dibujar la barra izquierda con bordes redondos
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_barra_izquierda, y_barra_izquierda, 5, alto_barra), border_radius=radio_bordes)

    # Dibujar la barra derecha con bordes redondos
    pygame.draw.rect(pantalla, COLOR_BLANCO, (x_barra_derecha, y_barra_derecha, 5, alto_barra), border_radius=radio_bordes)

    # Dibujar la pelota
    pygame.draw.circle(pantalla, COLOR_BLANCO, (int(x_pelota), int(y_pelota)), radio_pelota)

    

    
    
    
