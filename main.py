import pygame
import random

# Inicializar pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('Images\\3.1 ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Images\\10.1 Fondo.jpg')

# Variables del jugador
img_jugador = pygame.image.load('Images\\4.1 cohete.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variables del enemigo
img_enemigo = pygame.image.load('Images\\8.1 enemigo.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.5
enemigo_y_cambio = 50

# Variables de la bala
img_bala = pygame.image.load('Images\\11.1 bala.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.5
enemigo_y_cambio = 50

# Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))
    
# Funcion enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Imagen de fondo
    pantalla.blit(fondo, (0,0))
    
    # Iterar eventos 
    for evento in pygame.event.get():
        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
        # Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
                
        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            
    # Modificar ubicación del jugador
    jugador_x += jugador_x_cambio
    
    # Mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
        
    # Modificar ubicación del enemigo
    enemigo_x += enemigo_x_cambio
    
    # Mantener dentro de bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.5
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.5
        enemigo_y += enemigo_y_cambio
    
    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)
    
    # Actualizar
    pygame.display.update()