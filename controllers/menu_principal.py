from utils import (
    errores,
    generadores,
    terminal,
    validaciones
)
from controllers import (
    menu_agregar,
    menu_categorias,
    menu_buscar,
    menu_eliminar,
    menu_editar,
    menu_guardar,
    menu_ver

)
    
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

        if opcion == "1":
            menu_agregar.menu_agregar1()
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
        elif opcion == "8":
            print("Saliendo del programa ")
            break
        else:
            print("Opcion no valida. Intente de nuevo...")
            terminal.congelar()