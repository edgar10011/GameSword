import pygame
import constantes

class Camara:
    def __init__(self, ancho_mapa, alto_mapa):
        # Tamaño total del mapa en píxeles
        self.ancho_mapa = ancho_mapa * constantes.TILE_SIZE  # Ancho total del mapa
        self.alto_mapa = alto_mapa * constantes.TILE_SIZE  # Alto total del mapa
        self.x = 0
        self.y = 0

    def actualizar(self, jugador):
        """ Centra la cámara en el personaje y limita la vista al mapa. """
        # Calcula la posición de la cámara para que siga al jugador
        self.x = jugador.forma.centerx - constantes.ANCHO_VENTANA // 2
        self.y = jugador.forma.centery - constantes.ALTO_VENTANA // 2

        # Limitar la cámara para que no se mueva fuera del mapa
        self.x = max(0, min(self.x, self.ancho_mapa - constantes.ANCHO_VENTANA))  # Limite derecho
        self.y = max(0, min(self.y, self.alto_mapa - constantes.ALTO_VENTANA))  # Limite inferior

    def aplicar(self, pos):
        """ Transforma las coordenadas de los objetos en función de la cámara. """
        return pos[0] - self.x, pos[1] - self.y
