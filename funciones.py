from modelos import Pelicula, Genero, Catalogo
import sql

def agregar_pelicula():

    print("AGREGAR UNA PELÍCULA.\n")

    try:
        nombre = str(input("Ingrese el nombre de la película que desea agregar: "))
        duracion = int(input("Ingrese la duracion en minutos de la pelicula: "))
        genero_nombre = input("Ingrese el genero de la pelicula: ").capitalize()

    except ValueError as error:
        print(f"Algún valor ingresado no es válido. Error: {error}")
        return

    id_genero = sql.obtener_id_genero_por_nombre(genero_nombre) # Asignarle el id al género introducido

    if id_genero is None:
        print("El género aún no existe en la base de datos. Agréguelo y vuelva a intentar.")
        return

    pelicula = Pelicula(nombre, duracion, id_genero)    # Crear objeto Pelicula
    sql.agregar_pelicula(pelicula)             # Función para agregar el objeto a la base de datos
    print("\nPelícula agregada con éxito.")



def obtener_peliculas():
    catalogo = Catalogo("Todas las películas")
    peliculas = sql.obtener_peliculas()
    
    for pelicula in peliculas:
        guardar_pelicula = Pelicula(pelicula[1], pelicula[2], pelicula[3])  # Crear instancia para cada película
        catalogo.peliculas.append(guardar_pelicula) # Agregar al catálogo
    
    
    print("PELÍCULAS:")
    for pelicula in catalogo.peliculas:     # Desplegar el catálogo
        print(f"""
Nombre de la pelicula: {pelicula.nombre}
Duracion de la pelicula: {pelicula.duracion} minutos
Genero de la pelicula: {pelicula.genero}""")


def agregar_genero():
    print("AGREGAR UN GÉNERO:\n")
    nombre = str(input("Ingrese el nombre del genero que desea agregar: "))
    genero_nombre = Genero(nombre)
    sql.agregar_genero(genero_nombre)

    print("\nGénero agregado exitosamente.")


def obtener_generos():
    generos = sql.obtener_generos()
    
    generos = [Genero(genero[0]) for genero in generos]

    print("GÉNEROS:")
    for genero in generos:
        print(genero.nombre)
