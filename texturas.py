from pixels import pinta_lienzo, espera, cargar_lienzo_desde_imagen


def generar_patron_aleatorio(ancho, alto):
    """
    Genera un lienzo con colores aleatorios.

    Args:
        ancho (int): Número de píxeles de ancho.
        alto (int): Número de píxeles de alto.

    Returns:
        dict: Lienzo representado como un diccionario.
    """
    pass


def generar_patron_cuadros(ancho, alto, color1, color2):
    """
    Genera un lienzo con un patrón de cuadros.

    Args:
        ancho (int): Número de píxeles de ancho.
        alto (int): Número de píxeles de alto.
        color1 (tuple): Color de los cuadros claros en formato RGB.
        color2 (tuple): Color de los cuadros oscuros en formato RGB.

    Returns:
        dict: Lienzo representado como un diccionario.
    """
    pass


def generar_patron_rectangulos(ancho, alto, rectangulos):
    """
    Genera un lienzo con un patrón de rectángulos.

    Args:
        ancho (int): Número de píxeles de ancho del lienzo.
        alto (int): Número de píxeles de alto del lienzo.
        rectangulos (list): Lista de rectángulos a dibujar. Cada rectángulo es un diccionario con:
            - 'x': Coordenada X de la esquina superior izquierda.
            - 'y': Coordenada Y de la esquina superior izquierda.
            - 'ancho': Ancho del rectángulo.
            - 'alto': Alto del rectángulo.
            - 'color': Color del rectángulo en formato RGB.
            - 'relleno': Booleano, si es True, el rectángulo estará relleno.

    Returns:
        dict: Lienzo representado como un diccionario con los rectángulos dibujados.
    """
    pass


def analizar_brillos(lienzo):
    """
    Analiza los brillos de los píxeles del lienzo.

    Args:
        lienzo (dict): Lienzo representado como un diccionario.

    Returns:
        dict: Diccionario con claves 'brillos', 'promedio', 'max', 'min'.
    """
    pass



def ordenar_por_brillo(lienzo, orden="ascendente"):
    """
    Ordena los píxeles del lienzo por brillo usando el algoritmo de selección.

    Args:
        lienzo (dict): Lienzo representado como un diccionario.
        orden (str): 'ascendente' o 'descendente'.

    Returns:
        dict: Nuevo lienzo con los píxeles ordenados por brillo.
    """
    pass


def rotar_textura(lienzo, angulo):
    """
    Rota el lienzo en el ángulo especificado.

    Args:
        lienzo (dict): Lienzo representado como un diccionario.
        angulo (int): Ángulo de rotación (90, 180, 270).

    Returns:
        dict: Lienzo rotado.
    """
    pass


def reorganizar_por_componente(lienzo, componente):
    """
    Reorganiza el lienzo dividiéndolo en cuadrantes según una componente (R, G o B).

    Args:
        lienzo (dict): Lienzo representado como un diccionario.
        componente (str): Componente del color ('r', 'g' o 'b').

    Returns:
        dict: Lienzo reorganizado por la componente seleccionada.
    """
    pass


def transformar_a_grises(lienzo):
    """
    Convierte el lienzo a escala de grises.

    Args:
        lienzo (dict): Lienzo representado como un diccionario.

    Returns:
        dict: Lienzo transformado a escala de grises.
    """
    pass


########## PARTE OPCIONAL ##########


def generar_degradado(ancho, alto, color_inicio, color_fin):
    """
    Genera un lienzo con un degradado entre dos colores.

    Args:
        ancho (int): Ancho del lienzo.
        alto (int): Alto del lienzo.
        color_inicio (tuple): Color inicial en formato RGB.
        color_fin (tuple): Color final en formato RGB.

    Returns:
        dict: Lienzo con el degradado aplicado.
    """
    pass


def ajustar_contraste(lienzo, factor):
    """
    Ajusta el contraste del lienzo.

    Args:
        lienzo (dict): Lienzo representado como un diccionario.
        factor (float): Factor de ajuste de contraste (>1 aumenta, <1 reduce).

    Returns:
        dict: Lienzo con el contraste ajustado.
    """
    pass


def comprimir_colores(lienzo, niveles):
    """
    Reduce la cantidad de colores del lienzo agrupándolos en niveles definidos.

    Args:
        lienzo (dict): Lienzo representado como un diccionario.
        niveles (int): Número de niveles de color.

    Returns:
        dict: Lienzo con los colores comprimidos.
    """
    pass


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
