from texturas import (analizar_brillos, generar_patron_aleatorio, generar_patron_cuadros, 
                        generar_patron_rectangulos, transformar_a_grises, ordenar_por_brillo, 
                        rotar_textura, reorganizar_por_componente)
from pixels import espera, cargar_lienzo_desde_imagen, pinta_lienzo



def main():
    ancho, alto = 20, 20
    
    lienzo = cargar_lienzo_desde_imagen("cafe_small.gif")
    
    pinta_lienzo(transformar_a_grises(lienzo))
    espera()

    # Lista de rectángulos a dibujar
    rectangulos = [
        {'x': 2, 'y': 2, 'ancho': 5, 'alto': 3, 'color': (255, 0, 0), 'relleno': True},  # Rectángulo rojo relleno
        {'x': 8, 'y': 5, 'ancho': 6, 'alto': 4, 'color': (0, 255, 0), 'relleno': False}, # Rectángulo verde sin relleno
        {'x': 0, 'y': 10, 'ancho': 10, 'alto': 2, 'color': (0, 0, 255), 'relleno': True}, # Rectángulo azul relleno
    ]

    # Generar el patrón de rectángulos
    lienzo_rectangulos = generar_patron_rectangulos(100, 100, rectangulos)
    pinta_lienzo(lienzo_rectangulos)
    espera()

    # Generar patrones
    lienzo_aleatorio = generar_patron_aleatorio(ancho, alto)
    pinta_lienzo(lienzo_aleatorio)
    espera()

    lienzo_cuadros = generar_patron_cuadros(ancho, alto, (255, 0, 0), (0, 255, 0))
    pinta_lienzo(lienzo_cuadros)
    espera()

    # Analizar brillos
    brillos = analizar_brillos(lienzo_aleatorio)
    print("Análisis de brillos:", brillos)

    # Ordenar por brillo
    lienzo_ordenado = ordenar_por_brillo(lienzo_aleatorio, "ascendente")
    pinta_lienzo(lienzo_ordenado)
    espera()

    # Rotar textura
    lienzo_rotado = rotar_textura(lienzo_aleatorio, 90)
    pinta_lienzo(lienzo_rotado)
    espera()

    # Reorganizar por zonas
    lienzo_reorganizado = reorganizar_por_componente(lienzo_aleatorio, 'r')
    pinta_lienzo(lienzo_reorganizado)
    espera()


if __name__ == "__main__":
    main()
