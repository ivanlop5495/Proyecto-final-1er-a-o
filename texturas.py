import pixels
from pixels import pinta_lienzo, espera, cargar_lienzo_desde_imagen, pinta
from tkinter import Tk, Canvas, PhotoImage, mainloop, IntVar
import tkinter as tk
import random

def generar_patron_aleatorio(ancho, alto):

    lienzo = {
        "width": ancho,
        "height": alto,
        "pixels": []
    }

    for _ in range(alto):
        fila = []
        for _ in range(ancho):
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            fila.append(color)
        lienzo["pixels"].append(fila)


    return lienzo
ancho = 20
alto = 20
lienzo_aleatorio = generar_patron_aleatorio(ancho, alto)
pinta_lienzo(lienzo_aleatorio)
espera()

def generar_patron_cuadros(ancho, alto, color1, color2):

    lienzo = {
        "width": ancho,
        "height": alto,
        "pixels": []
    }

    for y in range(alto):
        fila = []
        for x in range(ancho):
            color = color1 if (x + y) % 2 == 0 else color2
            fila.append(color)
        lienzo["pixels"].append(fila)

    return lienzo
lienzo = generar_patron_cuadros(20, 20, (255, 0, 0), (0, 255, 0))
pinta_lienzo(lienzo)
espera()

def generar_patron_rectangulos(ancho, alto, rectangulos):

    lienzo = {
        "width": ancho,
        "height": alto,
        "pixels": [[(0, 0, 0) for _ in range(ancho)] for _ in range(alto)]
    }

    for rect in rectangulos:
        x = rect["x"]
        y = rect["y"]
        rect_ancho = rect["ancho"]
        rect_alto = rect["alto"]
        color = rect["color"]
        relleno = rect["relleno"]

        if (x >= 0 and y >= 0 and
                x + rect_ancho <= ancho and
                y + rect_alto <= alto):

            for y2 in range(y, y + rect_alto):
                for x2 in range(x, x + rect_ancho):
                    if (relleno or
                            y2 == y or
                            y2 == y + rect_alto - 1 or
                            x2 == x or
                            x2 == x + rect_ancho - 1):
                        lienzo["pixels"][y2][x2] = color

    return lienzo
rectangulos = [
    {'x': 2, 'y': 2, 'ancho': 5, 'alto': 3, 'color': (255, 0, 0), 'relleno': True},
    {'x': 8, 'y': 5, 'ancho': 6, 'alto': 4, 'color': (0, 255, 0), 'relleno': False},
    {'x': 0, 'y': 10, 'ancho': 10, 'alto': 2, 'color': (0, 0, 255), 'relleno': True}
]

lienzo = generar_patron_rectangulos(20, 20, rectangulos)
pinta_lienzo(lienzo)
espera()

def analizar_brillos(lienzo):

    brillos = []

    for fila in lienzo["pixels"]:
        for pixel in fila:
            brillo = sum(pixel) // 3
            brillos.append(brillo)

    if brillos:
        promedio = sum(brillos) // len(brillos)
        maximo = max(brillos)
        minimo = min(brillos)
    else:
        promedio = maximo = minimo = 0

    resultados = {
        "brillos": brillos,
        "promedio": promedio,
        "max": maximo,
        "min": minimo
    }

    return resultados

resultados = analizar_brillos(lienzo_aleatorio)

print("Brillo promedio:", resultados["promedio"])
print("Brillo máximo:", resultados["max"])
print("Brillo mínimo:", resultados["min"])



def ordenar_por_brillo(lienzo, orden="ascendente"):

    pixels_con_brillo = []
    for fila in lienzo["pixels"]:
        for pixel in fila:
            brillo = sum(pixel) // 3
            pixels_con_brillo.append((brillo, pixel))

    n = len(pixels_con_brillo)
    for i in range(n):
        idx_seleccionado = i
        for j in range(i + 1, n):
            if orden == "ascendente":
                if pixels_con_brillo[j][0] < pixels_con_brillo[idx_seleccionado][0]:
                    idx_seleccionado = j
            else:  # descendente
                if pixels_con_brillo[j][0] > pixels_con_brillo[idx_seleccionado][0]:
                    idx_seleccionado = j

        pixels_con_brillo[i], pixels_con_brillo[idx_seleccionado] = \
            pixels_con_brillo[idx_seleccionado], pixels_con_brillo[i]

    pixels_ordenados = [pixel[1] for pixel in pixels_con_brillo]

    nuevo_lienzo = {
        "width": lienzo["width"],
        "height": lienzo["height"],
        "pixels": []
    }

    for i in range(0, len(pixels_ordenados), lienzo["width"]):
        fila = pixels_ordenados[i:i + lienzo["width"]]
        nuevo_lienzo["pixels"].append(fila)

    return nuevo_lienzo

lienzo_ordenado = ordenar_por_brillo(lienzo_aleatorio, "ascendente")
pinta_lienzo(lienzo_ordenado)
espera()


def rotar_textura(lienzo, angulo):
    if angulo not in [90, 180, 270]:
        return lienzo

    ancho_original = lienzo["width"]
    alto_original = lienzo["height"]
    pixels_original = lienzo["pixels"]

    # Para 90 y 270 grados, el ancho y alto se intercambian
    if angulo in [90, 270]:
        nuevo_ancho = alto_original
        nuevo_alto = ancho_original
    else:  # 180 grados
        nuevo_ancho = ancho_original
        nuevo_alto = alto_original

    nuevo_lienzo = {
        "width": nuevo_ancho,
        "height": nuevo_alto,
        "pixels": [[None for _ in range(nuevo_ancho)] for _ in range(nuevo_alto)]
    }

    for y in range(alto_original):
        for x in range(ancho_original):
            pixel = pixels_original[y][x]

            if angulo == 90:

                nuevo_lienzo["pixels"][x][alto_original - 1 - y] = pixel
            elif angulo == 180:

                nuevo_lienzo["pixels"][alto_original - 1 - y][ancho_original - 1 - x] = pixel
            elif angulo == 270:

                nuevo_lienzo["pixels"][ancho_original - 1 - x][y] = pixel

    return nuevo_lienzo

for angulo in [90, 180, 270]:
    lienzo_rotado = rotar_textura(lienzo_aleatorio, angulo)
    print(f"Rotación de {angulo} grados:")
    pinta_lienzo(lienzo_rotado)
    espera()


def reorganizar_por_componente(lienzo, componente):

    indice_componente = {'r': 0, 'g': 1, 'b': 2}[componente.lower()]

    cuadrantes = {
        1: [],  # 0-63
        2: [],  # 64-127
        3: [],  # 128-191
        4: []  # 192-255
    }

    for fila in lienzo["pixels"]:
        for pixel in fila:
            valor = pixel[indice_componente]
            if valor <= 63:
                cuadrantes[1].append(pixel)
            elif valor <= 127:
                cuadrantes[2].append(pixel)
            elif valor <= 191:
                cuadrantes[3].append(pixel)
            else:
                cuadrantes[4].append(pixel)

    total_pixels = len(lienzo["pixels"]) * len(lienzo["pixels"][0])
    nuevo_lado = int((total_pixels ** 0.5 + 1) // 2) * 2
    nuevo_lienzo = {
        "width": nuevo_lado,
        "height": nuevo_lado,
        "pixels": [[(0, 0, 0) for _ in range(nuevo_lado)] for _ in range(nuevo_lado)]
    }

    lado_cuadrante = nuevo_lado // 2

    for num_cuadrante, pixels in cuadrantes.items():
        offset_x = (num_cuadrante - 1) % 2 * lado_cuadrante
        offset_y = (num_cuadrante - 1) // 2 * lado_cuadrante

        for i, pixel in enumerate(pixels):
            if i >= lado_cuadrante * lado_cuadrante:
                break
            y = offset_y + (i // lado_cuadrante)
            x = offset_x + (i % lado_cuadrante)
            nuevo_lienzo["pixels"][y][x] = pixel

    return nuevo_lienzo

for componente in ['r', 'g', 'b']:
    print(f"Reorganización por componente {componente}:")
    lienzo_reorganizado = reorganizar_por_componente(lienzo_aleatorio, componente)
    pinta_lienzo(lienzo_reorganizado)
    espera()

def transformar_a_grises(lienzo):

    nuevo_lienzo = {
        "width": lienzo["width"],
        "height": lienzo["height"],
        "pixels": []
    }

    for fila in lienzo["pixels"]:
        nueva_fila = []
        for pixel in fila:
            gris = sum(pixel) // 3
            nueva_fila.append((gris, gris, gris))
        nuevo_lienzo["pixels"].append(nueva_fila)

    return nuevo_lienzo
lienzo = cargar_lienzo_desde_imagen("cafe_small.gif")

lienzo_grises = transformar_a_grises(lienzo)
pinta_lienzo(lienzo_grises)
espera()


########## PARTE OPCIONAL ##########


def generar_degradado(ancho, alto, color_inicio, color_fin):

    lienzo = {
        "width": ancho,
        "height": alto,
        "pixels": []
    }

    for y in range(alto):
        fila = []
        for x in range(ancho):
            if ancho == 1:
                proporcion = 0
            else:
                proporcion = x / (ancho - 1)

            r = int(color_inicio[0] + proporcion * (color_fin[0] - color_inicio[0]))
            g = int(color_inicio[1] + proporcion * (color_fin[1] - color_inicio[1]))
            b = int(color_inicio[2] + proporcion * (color_fin[2] - color_inicio[2]))

            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))

            fila.append((r, g, b))
        lienzo["pixels"].append(fila)

    return lienzo
lienzo = generar_degradado(20, 20, (255, 0, 0), (0, 0, 255))
pinta_lienzo(lienzo)
espera()


def ajustar_contraste(lienzo, factor):

    nuevo_lienzo = {
        "width": lienzo["width"],
        "height": lienzo["height"],
        "pixels": []
    }

    VALOR_MEDIO = 128

    # Procesar cada píxel
    for fila in lienzo["pixels"]:
        nueva_fila = []
        for pixel in fila:
            nuevo_pixel = []
            for componente in pixel:
                nuevo_valor = int(VALOR_MEDIO + factor * (componente - VALOR_MEDIO))

                nuevo_valor = max(0, min(255, nuevo_valor))
                nuevo_pixel.append(nuevo_valor)

            nueva_fila.append(tuple(nuevo_pixel))
        nuevo_lienzo["pixels"].append(nueva_fila)

    return nuevo_lienzo

lienzo_contrastado = ajustar_contraste(lienzo_aleatorio, 3)
pinta_lienzo(lienzo_contrastado)
espera()

def comprimir_colores(lienzo, niveles):

    nuevo_lienzo = {
        "width": lienzo["width"],
        "height": lienzo["height"],
        "pixels": []
    }

    intervalo = 256 // niveles

    for fila in lienzo["pixels"]:
        nueva_fila = []
        for pixel in fila:
            nuevo_pixel = tuple(
                (componente // intervalo) * intervalo
                for componente in pixel
            )
            nueva_fila.append(nuevo_pixel)
        nuevo_lienzo["pixels"].append(nueva_fila)

    return nuevo_lienzo

lienzo_comprimido = comprimir_colores(lienzo_aleatorio, 4)
pinta_lienzo(lienzo_comprimido)
espera()

def generar_patron_custom(ancho, alto, configuracion, color_fondo):
    """
    Genera un lienzo según una configuración específica de posiciones y colores.

    Args:
        ancho (int): Ancho del lienzo.
        alto (int): Alto del lienzo.
        configuracion (dict): Diccionario con coordenadas (x, y) y colores RGB.
        color_fondo (tuple): Color de fondo.

    Returns:
        dict: Lienzo generado.
    """
    pass


def main():
    lienzo_aleatorio = generar_patron_aleatorio(20, 20)
    pinta_lienzo(lienzo_aleatorio)
    espera()


if __name__ == "__main__":
    main()
