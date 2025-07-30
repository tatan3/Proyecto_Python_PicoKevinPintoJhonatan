import utils.terminal as control
import controllers.funciones as fun
def menu_principal():
    while True:
        control.limpiar()
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
        if opcion == "1":
            return menu_agregar1()
        elif opcion == "2":
            menu_ver()
        elif opcion=="3":
            menu_buscar()
        elif opcion == "4":
            menu_editar()
        elif opcion == "5":
            menu_eliminar()
        elif opcion == "6":
            menu_categorias()
        elif opcion == "7":
            menu_guardar()
        else:
            print("Saliendo del programa")
            control.congelar()
            break
    

def menu_agregar1():
    while True:
        control.limpiar()

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

        if opcion == "1":
            return fun.crear_elemento()
        elif opcion == "2":
            return menu_ver()
        elif opcion=="3":
            return menu_buscar()
        elif opcion == "4":
            return menu_principal()
        else:
            print("Opcion no valida. Intente de nuevo...")
            control.congelar()
            tipo={'1': 'libro', '2': 'Pelicula', '3': 'Musica'}
        if opcion in tipo:
            agregar_elemento(tipo[opcion])


def menu_ver():
    while True:
        control.limpiar()
        print("""
===========================================
        Ver Todos los Elementos
===========================================
¿Qué categoría deseas ver?
1. Ver Todos los Libros
2. Ver Todas las Películas
3. Ver Toda la Música
4. Regresar al Menú Principal
=========================================== """)
        opcion = input("/ seleccione una opcion (1-4): ")
        if opcion == "1":
            return fun.ver_elementos()
        elif opcion == "2":
            return menu_ver()
        elif opcion=="3":
            return menu_buscar()
        else:
            print("Saliendo del programa")
            control.congelar()
            break
            
def menu_buscar():
    while True:
        control.limpiar()
        print("""
        ===========================================
            Buscar un Elemento
    ===========================================
    ¿Cómo deseas buscar?
    1. Buscar por Título
    2. Buscar por Autor/Director/Artista
    3. Buscar por Género
    4. Regresar al Menú Principal
    ===========================================""")
        opcion = input("/ seleccione una opcion (1-4): ")
        if opcion == "1":
            return agregar_elemento()
        elif opcion == "2":
            return menu_ver()
        elif opcion=="3":
            return menu_buscar()
        elif opcion == "4":
            return menu_principal()
        elif opcion == "8":
            print("Saliendo del programa ")
            break
        else:
            print("Opcion no valida. Intente de nuevo...")
            control.congelar()
            

def menu_editar():
    while True:
        control.limpiar()
        print("""
        ===========================================
        Editar un Elemento
===========================================
¿Qué tipo de cambio deseas realizar?
1. Editar Título
2. Editar Autor/Director/Artista
3. Editar Género
4. Editar Valoración
5. Regresar al Menú Principal
===========================================""")
        opcion = input("/ seleccione una opcion (1-5): ")
        if opcion == "1":
            return agregar_elemento()
        elif opcion == "2":
            return menu_ver()
        elif opcion=="3":
            return menu_buscar()
        elif opcion == "4":
            return menu_principal()
        elif opcion == "5":
            print("Saliendo del programa ")
            break
        else:
            print("Opcion no valida. Intente de nuevo...")
            control.congelar()
            tipo={'1': 'libro', '2': 'Pelicula', '3': 'Musica'}
        if opcion in tipo:
            agregar_elemento(tipo[opcion])

def menu_eliminar():
    while True:
        control.limpiar()
        print("""
        ===========================================
        Eliminar un Elemento
===========================================
¿Cómo deseas eliminar?
1. Eliminar por Título
2. Eliminar por Identificador Único
3. Regresar al Menú Principal
===========================================
""")
        opcion = input("/ seleccione una opcion (1-3): ")
        if opcion == "1":
            return agregar_elemento()
        elif opcion == "2":
            return menu_ver()
        elif opcion=="3":
            return menu_principal()
        elif opcion == "4":
            return menu_principal()
        elif opcion == "5":
            print("Saliendo del programa ")
            break
        else:
            print("Opcion no valida. Intente de nuevo...")
            control.congelar()
            

def menu_categorias():
    while True:
        control.limpiar()
        print("""
    ===========================================
        Ver Elementos por Categoría
===========================================
¿Qué categoría deseas ver?
1. Ver Libros
2. Ver Películas
3. Ver Música
4. Regresar al Menú Principal
===========================================
""")
        opcion = input("/ seleccione una opcion (1-4): ")
        if opcion == "1":
            return agregar_elemento()
        elif opcion == "2":
            return menu_ver()
        elif opcion=="3":
            return menu_principal()
        elif opcion == "4":
            return menu_principal()
        elif opcion == "5":
            print("Saliendo del programa ")
            break
        else:
            print("Opcion no valida. Intente de nuevo...")
            control.congelar()
            

def menu_guardar():
    while True:
        control.limpiar()
        print("""
    ===========================================
        Guardar y Cargar Colección
===========================================
¿Qué deseas hacer?
1. Guardar la Colección Actual
2. Cargar una Colección Guardada
3. Regresar al Menú Principal
===========================================
""")
        opcion = input("/ seleccione una opcion (1-4): ")
        if opcion == "1":
            return agregar_elemento()
        elif opcion == "2":
            return menu_ver()
        elif opcion=="3":
            return menu_principal()
        else:
            print("Saliendo del programa ")
            break






