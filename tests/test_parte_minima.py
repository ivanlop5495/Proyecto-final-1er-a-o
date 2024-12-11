import unittest
from texturas import (generar_patron_aleatorio, generar_patron_cuadros,
                               generar_patron_rectangulos, analizar_brillos,
                               ordenar_por_brillo, transformar_a_grises)
from pixels import cargar_lienzo_desde_imagen


class TestGenerarPatrones(unittest.TestCase):
    def test_generar_patron_aleatorio(self):
        ancho, alto = 10, 10
        lienzo = generar_patron_aleatorio(ancho, alto)
        self.assertEqual(lienzo["width"], ancho)
        self.assertEqual(lienzo["height"], alto)
        self.assertEqual(len(lienzo["pixels"]), alto)
        for fila in lienzo["pixels"]:
            self.assertEqual(len(fila), ancho)

    def test_generar_patron_cuadros(self):
        ancho, alto = 4, 4
        color1, color2 = (255, 0, 0), (0, 255, 0)
        lienzo = generar_patron_cuadros(ancho, alto, color1, color2)
        self.assertEqual(lienzo["width"], ancho)
        self.assertEqual(lienzo["height"], alto)
        for y, fila in enumerate(lienzo["pixels"]):
            for x, pixel in enumerate(fila):
                expected_color = color1 if (x + y) % 2 == 0 else color2
                self.assertEqual(pixel, expected_color)

    def test_generar_patron_rectangulos(self):
        ancho, alto = 10, 10
        rectangulos = [
            {"x": 1, "y": 1, "ancho": 3, "alto": 2, "color": (255, 0, 0), "relleno": True},
            {"x": 5, "y": 5, "ancho": 2, "alto": 3, "color": (0, 255, 0), "relleno": False},
        ]
        lienzo = generar_patron_rectangulos(ancho, alto, rectangulos)
        self.assertEqual(lienzo["width"], ancho)
        self.assertEqual(lienzo["height"], alto)
        for rect in rectangulos:
            for y in range(rect["y"], rect["y"] + rect["alto"]):
                for x in range(rect["x"], rect["x"] + rect["ancho"]):
                    if rect["relleno"] or y in (rect["y"], rect["y"] + rect["alto"] - 1) or x in (rect["x"], rect["x"] + rect["ancho"] - 1):
                        self.assertEqual(lienzo["pixels"][y][x], rect["color"])


class TestAnalizarBrillos(unittest.TestCase):
    def test_analizar_brillos(self):
        lienzo = {
            "width": 2,
            "height": 2,
            "pixels": [
                [(10, 20, 30), (40, 50, 60)],
                [(70, 80, 90), (100, 110, 120)],
            ],
        }
        resultado = analizar_brillos(lienzo)
        self.assertEqual(resultado["promedio"], 65)
        self.assertEqual(resultado["max"], 110)
        self.assertEqual(resultado["min"], 20)


class TestOrdenarPorBrillo(unittest.TestCase):
    def test_ordenar_por_brillo(self):
        lienzo = {
            "width": 2,
            "height": 2,
            "pixels": [
                [(10, 20, 30), (100, 110, 120)],
                [(70, 80, 90), (40, 50, 60)],
            ],
        }
        lienzo_ordenado = ordenar_por_brillo(lienzo, orden="ascendente")
        brillos = [
            (p[0] + p[1] + p[2]) // 3 for fila in lienzo_ordenado["pixels"] for p in fila
        ]
        self.assertEqual(brillos, sorted(brillos))


class TestTransformaciones(unittest.TestCase):
    def test_transformar_a_grises(self):
        lienzo = {
            "width": 2,
            "height": 2,
            "pixels": [
                [(10, 20, 30), (40, 50, 60)],
                [(70, 80, 90), (100, 110, 120)],
            ],
        }
        resultado = transformar_a_grises(lienzo)
        esperado = {
            "width": 2,
            "height": 2,
            "pixels": [
                [(20, 20, 20), (50, 50, 50)],
                [(80, 80, 80), (110, 110, 110)],
            ],
        }
        self.assertEqual(resultado, esperado)


class TestImagenes(unittest.TestCase):
    def test_cargar_lienzo_desde_imagen(self):
        lienzo = cargar_lienzo_desde_imagen("cafe_small.gif")
        self.assertGreater(lienzo["width"], 0)
        self.assertGreater(lienzo["height"], 0)
        self.assertIsInstance(lienzo["pixels"], list)


if __name__ == "__main__":
    unittest.main()