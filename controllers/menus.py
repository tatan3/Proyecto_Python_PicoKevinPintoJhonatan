def menu_agregar1():
    while True:
        terminal.limpiar()
        print("================================")
        print("--- Añadir un Nuevo Elemento ---")
        print("================================")
        print("¿Que tipo de elemento deseas añadir?")
        print("1. |   Libro    |")
        print("2. |  Pelicula  |")
        print("3. |   Musica   |")
        print("4. |  Regresar  |")
        print("================================")
        opcion = input("/ seleccione una opcion (1-4): ")


def menu_principal():
    while True:
        terminal.limpiar()
        print("================================")
        print("---Administrador de Coleccion---")
        print("================================")
        print("1. | Añadir un Nuevo Elemento  |")
        print("2. |  Ver Todos los Elementos  |")
        print("3. |    Buscar un Elemento     |")
        print("4. |    Editar un Elemento     |")
        print("5. |   Eliminar un Elemento    |")
        print("6. |Ver Elementos por Categoria|")
        print("7. |Guardar y Cargar Coleccion |")
        print("8. |           Salir           |")
        print("================================")
        opcion = input("/ seleccione una opcion (1-8): ")