import pygame

# Inicializar Pygame antes de obtener la información de la pantalla
pygame.init()
info_pantalla = pygame.display.Info()

# Tamaño de la ventana (pantalla pequeña)
ANCHO_VENTANA = 800  # Tamaño de la ventana más pequeño
ALTO_VENTANA = 600

# Tamaño del personaje
ALTO_PERSONAJE = 48
ANCHO_PERSONAJE = 48

# Configuración del juego
FPS = 60
VELOCIDAD = 3
SCALA_PERSONAJE = 1

# Tamaño de los tiles en el mapa
TILE_SIZE = 32  # Cada tile mide 32x32 píxeles

# Tamaño del mapa en tiles (1600x1600 tiles)
MAP_WIDTH = 50
MAP_HEIGHT = 50

# Colores
COLOR_BG = (62, 95, 138)

# Zoom de la cámara
ZOOM = 2
