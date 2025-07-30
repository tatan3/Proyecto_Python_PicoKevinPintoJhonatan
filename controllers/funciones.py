import os
import json
from datetime import datetime

def crear_elemento():
    # Opciones válidas
    opciones = ['pelicula', 'musica', 'libro']


    tipo = input("¿Qué deseas agregar? (pelicula, musica, libro): ").lower().strip()
    while tipo not in opciones:
        print("Opción inválida. Elige entre: pelicula, musica o libro.")
        tipo = input("¿Qué deseas agregar? (pelicula, musica, libro): ").lower().strip()

    nombre = input("Nombre del elemento: ").strip()
    autor = input("Autor: ").strip()
    fecha = input("Fecha (YYYY-MM-DD): ").strip()

    # Validar fecha
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        print("⚠️ Fecha inválida. Usando fecha actual.")
        fecha = datetime.today().strftime('%Y-%m-%d')

    # Estructura de datos
    elemento = {
        'nombre': nombre,
        'autor': autor,
        'fecha': fecha
    }

    # Ruta del archivo
    carpeta = os.path.join("datos", tipo)
    os.makedirs(carpeta, exist_ok=True)  # Crea la carpeta si no existe

    # Nombre del archivo: nombre_sin_espacios_fecha.json
    nombrearchivo = f"{nombre.replace(' ', '')}_{fecha}.json"
    ruta_archivo = os.path.join("datos", "coleccion.json")

    # Guardar como JSON
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        json.dump(elemento, f, indent=4, ensure_ascii=False)

    print(f"✅ {tipo.capitalize()} guardado correctamente en: {ruta_archivo}")




import os
import json

def ver_elementos():
    # Opciones válidas
    opciones = ['pelicula', 'musica', 'libro']

#Pregunta al usuario
    tipo = input("¿Qué deseas ver? (pelicula, musica, libro): ").lower().strip()
    while tipo not in opciones:
        print("Opción inválida. Elige entre: pelicula, musica o libro.")
        tipo = input("¿Qué deseas ver? (pelicula, musica, libro): ").lower().strip()

    # Ruta de la carpeta
    carpeta = os.path.join("datos", tipo)

    if not os.path.exists(carpeta):
        print(f"⚠️ No hay datos guardados para '{tipo}'.")
        return

    archivos = [f for f in os.listdir(carpeta) if f.endswith(".json")]

    if not archivos:
        print(f"📂 La carpeta '{tipo}' está vacía.")
        return

    print(f"\n📚 Listando {tipo}s guardados:\n" + "-" * 30)
    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = json.load(f)
                print(f"📌 Nombre: {contenido.get('nombre', 'Desconocido')}")
                print(f"   Autor: {contenido.get('autor', 'Desconocido')}")
                print(f"   Fecha: {contenido.get('fecha', 'Desconocido')}")
                print("-" * 30)
        except Exception as e:
            print(f"❌ Error leyendo {archivo}: {e}")


