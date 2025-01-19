#!/usr/bin/env python3

"""
Módulo para pintar pixels en un lienzo, usando tkinter

Un pixel es la menor unidad que se puede pintar en el lienzo.
En este programa, el tamaño del pixel está controlado por la variable
`tamano`.

El módulo proporciona tres funciones:

* `prepara`
* 'pinta'
* 'espera'

Cuando se usa como módulo, normalmente no hace falta llamar a `prepara`

Además, tiene una función que actúa como programa principal, `main()`,
que no se ejecuta cuando se importa este fichero como módulo.
"""

from tkinter import Tk, Canvas, PhotoImage, mainloop, _get_default_root, IntVar

tamano = 4
ancho = 800
alto = 800


def prepara():
    """Prepara la tortuga para que funcione la función pinta()"""

    window = Tk()
    canvas = Canvas(window, width=ancho, height=alto, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=ancho, height=alto)
    canvas.create_image((ancho // 2, alto // 2), image=img, state="normal")
    return img


def tam_lienzo():
    return ancho // 10, alto // 10


def pinta(x: int, y: int, color: str = 'black'):
    """Pinta un pixel de color `color_name` en las coordenadas `x` e `y`"""

    for x_real in range(x * tamano, x * tamano + tamano):
        for y_real in range(y * tamano, y * tamano + tamano):
            img.put(color, (x_real, y_real))


def pinta_lienzo(lienzo):
    """
    Pinta un lienzo representado como un diccionario.

    Args:
        lienzo (dict): Diccionario que representa el lienzo, con las claves:
            - 'width': Ancho del lienzo en píxeles.
            - 'height': Alto del lienzo en píxeles.
            - 'pixels': Lista bidimensional de tuplas (R, G, B).
    """
    pixels = lienzo['pixels']
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            # Convierte el píxel RGB en formato hexadecimal
            color = f"#{pixel[0]:02x}{pixel[1]:02x}{pixel[2]:02x}"
            pinta(x, y, color)
            

def cargar_lienzo_desde_imagen(ruta_imagen):
    """
    Carga una imagen desde un archivo y la convierte en un lienzo 
    compatible con pinta_lienzo.

    Args:
        ruta_imagen (str): Ruta de la imagen a cargar.

    Returns:
        dict: Diccionario que representa el lienzo con las claves:
            - 'width': Ancho de la imagen en píxeles.
            - 'height': Alto de la imagen en píxeles.
            - 'pixels': Lista bidimensional de tuplas (R, G, B).
    """
    # Cargar la imagen como PhotoImage
    img = PhotoImage(file=ruta_imagen)

    # Obtener las dimensiones de la imagen
    ancho = img.width()
    alto = img.height()

    # Crear la estructura del lienzo
    pixels = []
    for y in range(alto):
        fila = []
        for x in range(ancho):
            color_rgb = img.get(x, y)
            fila.append(color_rgb)
        pixels.append(fila)

    # Devolver el lienzo como diccionario
    return {"width": ancho, "height": alto, "pixels": pixels}


def espera():
    global img
    """Espera. Normalmente hay que llamarlo al terminar de pintar"""
    mainloop()
    img = prepara()

def main():
    """Programa principal"""

    pinta(1, 2, "red")
    pinta(6, 2, "blue")
    espera()

    # Ruta de la imagen
    ruta_imagen = "cafe_small.gif"
    # Cargar la imagen como lienzo
    lienzo = cargar_lienzo_desde_imagen(ruta_imagen)
    # Pintar el lienzo en la ventana
    pinta_lienzo(lienzo)
    # Mantener la ventana abierta
    espera()


img = prepara()

if __name__ == "__main__":
    main()


def append():
    return None