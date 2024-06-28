import pygame
import copy

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)



def procesar_preguntas(lista_preguntas:list) -> list:
    """
    Toma una lista de preguntas en formato de diccionarios y devuelve una copia profunda de la lista procesada.

    Parametros:
    - lista_preguntas: Una lista de diccionarios que representa las preguntas del juego.

    Retorno:
    - lista_procesada: Una copia profunda de la lista de preguntas original.

    """
    
    lista_procesada = copy.deepcopy(lista_preguntas)
    
    return lista_procesada



def dibujar_texto(text:str, font, color, surface, position):
    """
    Toma un texto, una fuente, un color, una superficie y una posición, y dibuja el texto en la superficie con la fuente y el color especificados.

    Parametros:
    - text (str): El texto que se va a dibujar.
    - font: La fuente que se utilizará para dibujar el texto.
    - color: El color del texto.
    - surface: La superficie en la que se dibujará el texto.
    - position: La posición en la que se dibujará el texto en la superficie, especificada como una tupla de coordenadas (x, y).

    Retorno:
    - text_rect: Un objeto Rect que representa el rectángulo que contiene el texto dibujado en la superficie.
    """
    
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=position)
    
    surface.blit(text_surface, text_rect)
    
    return text_rect




def mostrar_pregunta_y_tema(screen, font, lista_preguntas:list, indice_pregunta_actual:int, mostrar_opciones:bool):
    """
    Toma la pantalla, la fuente, la lista de preguntas, el índice de la pregunta actual y una bandera para mostrar las opciones. Si se permite mostrar las opciones, dibuja el tema y la pregunta en la pantalla.

    Parametros:
    - screen: La pantalla en la que se mostrará la pregunta y el tema.
    - font: La fuente que se utilizará para mostrar el texto.
    - lista_preguntas: Una lista de diccionarios que representa las preguntas del juego.
    - indice_pregunta_actual: El índice de la pregunta actual en la lista de preguntas.
    - mostrar_opciones: Una bandera booleana que indica si se deben mostrar las opciones de respuesta.
    """
    
    if mostrar_opciones:
    
        # Toma el diccionario en el indice indicado
        pregunta_actual = lista_preguntas[indice_pregunta_actual]
        
        tema = pregunta_actual["tema"]
        pregunta = pregunta_actual["pregunta"]
        
        # Mostrar tema y pregunta
        dibujar_texto(tema, font, BLANCO, screen, (30, 250))
        dibujar_texto(pregunta, font, BLANCO, screen, (300, 250))




def mostrar_respuestas(screen, font, lista_preguntas: list, 
                       indice_pregunta_actual: int, mostrar_opciones: bool) -> list:
    """
    Toma la pantalla, la fuente, la lista de preguntas, el índice de la pregunta actual y una bandera para indicar si se deben mostrar las opciones de respuesta. Si se permite mostrar las opciones, dibuja las opciones de respuesta en la pantalla y devuelve una lista de rectángulos que representan las áreas clicables de las opciones.

    Parametros:
    - screen: La pantalla en la que se mostrarán las opciones de respuesta.
    - font: La fuente que se utilizará para mostrar el texto.
    - lista_preguntas: Una lista de diccionarios que representa las preguntas del juego.
    - indice_pregunta_actual: El índice de la pregunta actual en la lista de preguntas.
    - mostrar_opciones: Una bandera booleana que indica si se deben mostrar las opciones de respuesta.

    Retorno:
    - opciones_rects: Una lista de tuplas que contiene los rectángulos y las opciones de respuesta dibujadas en la pantalla.
    """
    
    if mostrar_opciones:
    
        # Toma el diccionario en el indice indicado
        pregunta_actual = lista_preguntas[indice_pregunta_actual]
        
        opcion_a = pregunta_actual["a"]
        opcion_b = pregunta_actual["b"]
        opcion_c = pregunta_actual["c"]

        # Mostrar opciones de respuesta
        rect_a = dibujar_texto(f"A. {opcion_a}", font, NEGRO, screen, (60, 380))
        rect_b = dibujar_texto(f"B. {opcion_b}", font, NEGRO, screen, (350, 380))
        rect_c = dibujar_texto(f"C. {opcion_c}", font, NEGRO, screen, (700, 380))
                
        # Guardar rectángulos y opciones en la lista
        opciones_rects = [(rect_a, "a"), (rect_b, "b"), (rect_c, "c")]
                
        return opciones_rects

    return []



def dibujar_boton(rect, text, color, font, screen):
    """
    Toma un rectángulo que representa el área del botón, el texto a mostrar en el botón, el color del botón, la fuente del texto y la pantalla en la que se dibujará el botón. Dibuja el botón con el texto centrado en el rectángulo y el color especificado.

    Parametros:
    - rect: Un objeto Rect que representa el área del botón.
    - text: El texto que se mostrará en el botón.
    - color: El color del botón.
    - font: La fuente que se utilizará para el texto del botón.
    - screen: La pantalla en la que se dibujará el botón.
    """

    # Dibujar el rectángulo del botón
    pygame.draw.rect(screen, color, rect)
    
    # Renderizar el texto del botón
    text_surface = font.render(text, True, NEGRO)
    text_rect = text_surface.get_rect(center=rect.center)
    
    # Dibujar el texto en el centro del rectángulo del botón
    screen.blit(text_surface, text_rect)




def comprobar_respuesta(opcion_selecionada, lista_preguntas: list, indice_pregunta_actual: int) -> bool:
    """
    Toma la opción seleccionada por el jugador, la lista de preguntas y el índice de la pregunta actual para determinar si la opción seleccionada coincide con la respuesta correcta en la pregunta actual.

    Parametros:
    - opcion_selecionada: La opción seleccionada por el jugador (por ejemplo, "a", "b", "c").
    - lista_preguntas: Una lista de diccionarios que representa las preguntas del juego.
    - indice_pregunta_actual: El índice de la pregunta actual en la lista de preguntas.

    Retorno:
    - bool: True si la opción seleccionada es la respuesta correcta, False de lo contrario.
    """

    # Obtener la pregunta actual
    pregunta_actual = lista_preguntas[indice_pregunta_actual]

    # Obtener la respuesta correcta de la pregunta actual
    respuesta_correcta = pregunta_actual["correcta"]

    # Comparar la opción seleccionada con la respuesta correcta y devolver el resultado
    return opcion_selecionada == respuesta_correcta

    
def actualizar_puntaje(score, font):
    """
    Toma el puntaje actual y la fuente para crear una superficie de texto que muestra el puntaje actualizado. Devuelve la superficie de texto creada.

    Parametros:
    - score: El puntaje actual del jugador.
    - font: La fuente que se utilizará para mostrar el texto del puntaje.

    Retorno:
    - score_surface: La superficie de texto que muestra el puntaje actualizado.
    """

    # Renderizar el texto del puntaje con el puntaje actualizado
    score_surface = font.render("Score: " + str(score), True, NEGRO)
    
    return score_surface

    

def procesar_respuesta(score):
    """
    Aumenta el puntaje del jugador en 10 puntos, desactiva la opción de mostrar las opciones de respuesta y muestra un mensaje indicando que la respuesta fue correcta.

    Parametros:
    - score: El puntaje actual del jugador.

    Retorno:
    - score: El puntaje actualizado después de sumar 10 puntos.
    - mostrar_opciones: Un valor booleano que indica si se deben mostrar las opciones de respuesta.
    """
    
    # Aumentar el puntaje en 10 puntos
    score += 10

    # Desactivar la opción de mostrar las opciones de respuesta
    mostrar_opciones = False

    # Imprimir mensaje indicando que la respuesta fue correcta
    print("Respuesta correcta!")

    return score, mostrar_opciones

