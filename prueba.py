import pygame as pg
import pytmx
import constantes as constantes
from personaje import Personaje
from camara import Camara

# Inicializar Pygame
pg.init()

# Configurar la pantalla
ventana = pg.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pg.display.set_caption("Excalibur")

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
    return pg.transform.scale(image, (int(w * scale), int(h * scale)))

# Cargar animaciones del personaje
idle = escalar_img(pg.image.load("assets/imagenes/characters/Player/_Idle_0.png"), constantes.SCALA_PERSONAJE)
animaciones = [escalar_img(pg.image.load(f"assets/imagenes/characters/Player/_Run_{i}.png"), constantes.SCALA_PERSONAJE) for i in range(10)]
animacion_ataque = [escalar_img(pg.image.load(f"assets/imagenes/characters/Player/_Attack{i}.png"), constantes.SCALA_PERSONAJE) for i in range(3)]

# Crear al jugador
jugador = Personaje(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2, animaciones, idle, animacion_ataque)

# Crear la cámara
camara = Camara(constantes.MAP_WIDTH, constantes.MAP_HEIGHT)

# Variables de movimiento
mover_arriba = mover_abajo = mover_izquierda = mover_derecha = False
reloj = pg.time.Clock()
run = True

#Detección de Joystick
pg.joystick.init()
if pg.joystick.get_count() > 0:
    joystick = pg.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None
    print("No se detectó ningún joystick.")

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

    mover_arriba = mover_abajo = mover_izquierda = mover_derecha = False
    
    # Manejo de eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a: mover_izquierda = True
            if event.key == pg.K_d: mover_derecha = True
            if event.key == pg.K_w: mover_arriba = True
            if event.key == pg.K_s: mover_abajo = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_a: mover_izquierda = False
            if event.key == pg.K_d: mover_derecha = False
            if event.key == pg.K_w: mover_arriba = False
            if event.key == pg.K_s: mover_abajo = False

        if event.type == pg.JOYBUTTONDOWN:
            if event.button == 0:
                print("Atacar")
                jugador.atacar()
            elif event.button == 1:
                print("Defender")
            elif event.button == 2:
                print("Presionado 2")
            elif event.button == 3:
                print("Presionado 3")
            elif event.button == 4:
                print("Presionado 4")
            elif event.button == 5:
                print("Presionado 5")
            elif event.button == 6:
                print("Presionado 6")
            elif event.button == 7:
                print("Presionado 7")
            elif event.button == 8:
                print("Presionado 8")
            elif event.button == 9:
                print("Presionado 9")

        if event.type == pg.JOYBUTTONUP:
            if event.button == 0:
                print("Dejar de atacar")
            elif event.button == 1:
                print("Dejar de defender")
            elif event.button == 2:
                print("Soltado 2")
            elif event.button == 3:
                print("Soltado 3")
            elif event.button == 4:
                print("Soltado 4")
            elif event.button == 5:
                print("Soltado 5")
            elif event.button == 6:
                print("Soltado 6")
            elif event.button == 7:
                print("Soltado 7")
            elif event.button == 8:
                print("Soltado 8")
            elif event.button == 9:
                print("Soltado 9")
                

    #Eventos de Joystick
    if joystick:
        axis_x = joystick.get_axis(0) 
        axis_y = joystick.get_axis(1)

        if axis_x < -0.2: mover_izquierda = True
        elif axis_x > 0.2: mover_derecha =  True
        if axis_y < -0.2: mover_arriba = True
        elif axis_y > 0.2: mover_abajo = True

    

    pg.display.update()
    reloj.tick(constantes.FPS)

pg.quit()
