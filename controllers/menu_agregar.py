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
import controllers.menu_principal as menu
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

        if opcion == "1":
            return agregar_elemento()
        elif opcion == "2":
            return menu_ver()
        elif opcion=="3":
            pass
        elif opcion == "4":
            return menu.menu_principal()
        elif opcion == "8":
            print("Saliendo del programa ")
            break
        else:
            print("Opcion no valida. Intente de nuevo...")
            terminal.congelar()
        tipo={'1': 'libro', '2': 'Pelicula', '3': 'Musica'}
        if opcion in tipo:
            agregar_elemento(tipo[opcion])


_contador_id=0   
def generar_id():
     global _contador_id
     _contador_id +=1

def agregar_elemento(tipo):
    terminal.limpiar()
    titulo=input("TITULO: ").strip()
    autor=input("AUTOR: "). strip()
    genero=input("GENERO: ").strip() 
    nuevo_elemento = {
            'id': generar_id(),
            'tipo' : tipo,
            'titulo': titulo,
            'autor': autor,
            'genero': genero
            
        }

    