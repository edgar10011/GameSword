import pygame
import constantes as constantes

class Personaje:
    def __init__(self, x, y, animaciones, idle, ataque):
        self.flip = False
        self.animaciones = animaciones
        self.idle = idle
        self.ataque = ataque
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[0]
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)
        self.en_movimiento = False
        self.atacando = False

    def movimiento(self, delta_x, delta_y, ancho_mapa, alto_mapa):
        """ Mueve al jugador dentro de los límites del mapa """
        if self.atacando:
            return

        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False

        # Movimiento del personaje con límites del mapa
        nueva_x = self.forma.x + delta_x
        nueva_y = self.forma.y + delta_y

        # Verifica que el nuevo movimiento no saque al personaje del mapa
        if 0 <= nueva_x <= ancho_mapa * constantes.TILE_SIZE - constantes.ANCHO_PERSONAJE:
            self.forma.x = nueva_x
        if 0 <= nueva_y <= alto_mapa * constantes.TILE_SIZE - constantes.ALTO_PERSONAJE:
            self.forma.y = nueva_y

        self.en_movimiento = delta_x != 0 or delta_y != 0

    def actualizar_animacion(self):
        cooldown_animacion = 75
        if self.atacando:
            if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
                self.frame_index = (self.frame_index + 1) % len(self.ataque)
                self.update_time = pygame.time.get_ticks()
                if self.frame_index == 0:
                    self.atacando = False
            self.image = self.ataque[self.frame_index]
        elif self.en_movimiento:
            if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
                self.frame_index = (self.frame_index + 1) % len(self.animaciones)
                self.update_time = pygame.time.get_ticks()
            self.image = self.animaciones[self.frame_index]
        else:
            self.image = self.idle

    def dibujar(self, ventana, camara):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        ventana.blit(image_flip, camara.aplicar((self.forma.x, self.forma.y)))

    def atacar(self):
        if not self.atacando:
            self.atacando = True
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
