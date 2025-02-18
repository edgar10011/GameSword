import pygame
import pytmx
import constantes
from personaje import Personaje
from camara import Camara

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Excalibur")

# Cargar el mapa TMX
tmx_data = pytmx.load_pygame('assets/imagenes/mundos/mapa.tmx')

# Función para dibujar el mapa
def dibujar_mapa(ventana, camara):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, tile in layer:
                tile_image = tmx_data.get_tile_image_by_gid(tile)
                if tile_image:
                    ventana.blit(tile_image, camara.aplicar((x * constantes.TILE_SIZE, y * constantes.TILE_SIZE)))

# Función para escalar imágenes
def escalar_img(image, scale):
    w, h = image.get_size()
    return pygame.transform.scale(image, (int(w * scale), int(h * scale)))

# Cargar animaciones del personaje
idle = escalar_img(pygame.image.load("assets/imagenes/characters/Player/_Idle_0.png"), constantes.SCALA_PERSONAJE)
animaciones = [escalar_img(pygame.image.load(f"assets/imagenes/characters/Player/_Run_{i}.png"), constantes.SCALA_PERSONAJE) for i in range(10)]
animacion_ataque = [escalar_img(pygame.image.load(f"assets/imagenes/characters/Player/_Attack{i}.png"), constantes.SCALA_PERSONAJE) for i in range(3)]

# Crear al jugador
jugador = Personaje(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2, animaciones, idle, animacion_ataque)

# Crear la cámara
camara = Camara(constantes.MAP_WIDTH, constantes.MAP_HEIGHT)

# Variables de movimiento
mover_arriba = mover_abajo = mover_izquierda = mover_derecha = False
reloj = pygame.time.Clock()
run = True

while run:
    ventana.fill(constantes.COLOR_BG)
    
    # Actualizar la cámara para que siga al jugador
    camara.actualizar(jugador)

    # Dibujar el mapa con la cámara
    dibujar_mapa(ventana, camara)

    # Movimiento del jugador
    delta_x = (constantes.VELOCIDAD if mover_derecha else 0) - (constantes.VELOCIDAD if mover_izquierda else 0)
    delta_y = (constantes.VELOCIDAD if mover_abajo else 0) - (constantes.VELOCIDAD if mover_arriba else 0)

    # Mover el personaje con límites del mapa
    jugador.movimiento(delta_x, delta_y, constantes.MAP_WIDTH, constantes.MAP_HEIGHT)
    jugador.actualizar_animacion()

    # Dibujar al jugador con la cámara aplicada
    jugador.dibujar(ventana, camara)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: mover_izquierda = True
            if event.key == pygame.K_d: mover_derecha = True
            if event.key == pygame.K_w: mover_arriba = True
            if event.key == pygame.K_s: mover_abajo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: mover_izquierda = False
            if event.key == pygame.K_d: mover_derecha = False
            if event.key == pygame.K_w: mover_arriba = False
            if event.key == pygame.K_s: mover_abajo = False

    pygame.display.update()
    reloj.tick(constantes.FPS)

pygame.quit()
