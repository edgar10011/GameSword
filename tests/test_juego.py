import pygame
import constantes as constantes
import constantes  # Directamente desde la raíz del proyecto


def test_pygame_init():
    """ Verifica que Pygame se inicializa correctamente """
    pygame.init()
    assert pygame.get_init() == True
    pygame.quit()

def test_pantalla_creacion():
    """ Verifica que la ventana se puede crear """
    pygame.init()
    screen = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
    assert screen is not None
    pygame.quit()
