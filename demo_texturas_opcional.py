from texturas import (generar_degradado, ajustar_contraste, comprimir_colores, 
                        generar_patron_custom)
from pixels import espera, pinta_lienzo


def main():
    ancho, alto = 20, 20

    # Generar degradado
    lienzo_degradado = generar_degradado(ancho, alto, (255, 0, 0), (0, 0, 255))
    pinta_lienzo(lienzo_degradado)
    espera()

    # Ajustar contraste
    lienzo_contraste = ajustar_contraste(lienzo_degradado, 1.5)
    pinta_lienzo(lienzo_contraste)
    espera()

    # Comprimir colores
    lienzo_comprimido = comprimir_colores(lienzo_degradado, 4)
    pinta_lienzo(lienzo_comprimido)
    espera()

    # Configuración personalizada
    configuracion = {
        (5, 5): (255, 255, 0),
        (6, 6): (0, 255, 255),
        (7, 7): (255, 0, 255),
    }
    lienzo_custom = generar_patron_custom(ancho, alto, configuracion, (0, 0, 0))
    pinta_lienzo(lienzo_custom)
    espera()


if __name__ == "__main__":
    main()
