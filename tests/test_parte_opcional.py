import unittest
from texturas import (generar_degradado, ajustar_contraste, 
                                  comprimir_colores, generar_patron_custom)


class TestGenerarDegradado(unittest.TestCase):
    def test_generar_degradado(self):
        ancho, alto = 10, 10
        color_inicio, color_fin = (255, 0, 0), (0, 0, 255)
        lienzo = generar_degradado(ancho, alto, color_inicio, color_fin)
        self.assertEqual(lienzo["width"], ancho)
        self.assertEqual(lienzo["height"], alto)
        for y, fila in enumerate(lienzo["pixels"]):
            for x, pixel in enumerate(fila):
                proporción = x / (ancho - 1)
                r = int(color_inicio[0] + proporción * (color_fin[0] - color_inicio[0]))
                g = int(color_inicio[1] + proporción * (color_fin[1] - color_inicio[1]))
                b = int(color_inicio[2] + proporción * (color_fin[2] - color_inicio[2]))
                self.assertEqual(pixel, (r, g, b))


class TestAjustarContraste(unittest.TestCase):
    def test_ajustar_contraste(self):
        lienzo = {
            "width": 2,
            "height": 2,
            "pixels": [
                [(100, 100, 100), (150, 150, 150)],
                [(200, 200, 200), (250, 250, 250)],
            ],
        }
        factor = 1.5
        resultado = ajustar_contraste(lienzo, factor)
        esperado = {
            "width": 2,
            "height": 2,
            "pixels": [
                [(86, 86, 86), (161, 161, 161)],
                [(236, 236, 236), (255, 255, 255)],
            ],
        }
        self.assertEqual(resultado, esperado)


class TestComprimirColores(unittest.TestCase):
    def test_comprimir_colores(self):
        lienzo = {
            "width": 3,
            "height": 2,
            "pixels": [
                [(50, 120, 200), (60, 130, 210), (70, 140, 220)],
                [(80, 150, 230), (90, 160, 240), (100, 170, 250)],
            ],
        }
        niveles = 4
        intervalo = 256 // niveles
        resultado = comprimir_colores(lienzo, niveles)
        esperado = {
            "width": 3,
            "height": 2,
            "pixels": [
                [
                    (pixel[0] // intervalo * intervalo,
                     pixel[1] // intervalo * intervalo,
                     pixel[2] // intervalo * intervalo)
                    for pixel in fila
                ] for fila in lienzo["pixels"]
            ],
        }
        self.assertEqual(resultado, esperado)


class TestGenerarPatronCustom(unittest.TestCase):
    def test_generar_patron_custom(self):
        ancho, alto = 5, 5
        configuracion = {
            (1, 1): (255, 0, 0),
            (3, 3): (0, 255, 0),
        }
        color_fondo = (0, 0, 0)
        lienzo = generar_patron_custom(ancho, alto, configuracion, color_fondo)
        self.assertEqual(lienzo["width"], ancho)
        self.assertEqual(lienzo["height"], alto)
        for y, fila in enumerate(lienzo["pixels"]):
            for x, pixel in enumerate(fila):
                if (x, y) in configuracion:
                    self.assertEqual(pixel, configuracion[(x, y)])
                else:
                    self.assertEqual(pixel, color_fondo)


if __name__ == "__main__":
    unittest.main()
