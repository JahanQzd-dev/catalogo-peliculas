import funciones
import os

# Funciones simples

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nPresione ENTER para regresar al menú...")
    limpiar()


# Main

while True:

    limpiar()

    try:
        menu = int(input("""OPCIONES DEL PROGRAMA:
[1] Para agregar una nueva película
[2] Para obtener películas
[3] Para agregar un nuevo género
[4] Para obtener géneros
[5] Para ver los catálogos                         
[0] Para salir del programa
>>> """))
               
        
    except ValueError as error:
        print(f"Ingrese un valor válido. Error: {error}")

    if menu == 1:
        limpiar()
        funciones.agregar_pelicula()
        pausa()
        
    elif menu == 2:
        limpiar()
        funciones.obtener_peliculas()
        pausa()

    elif menu == 3:
        limpiar()
        funciones.agregar_genero()
        pausa()

    elif menu == 4:
        limpiar()
        funciones.obtener_generos()
        pausa()

    elif menu == 0:
        print("Saliendo del programa...")
        exit()
    
    else:
        print(f"La opción [{menu}] no existe. Intente nuevamente.")
        pausa()

    print("\n")