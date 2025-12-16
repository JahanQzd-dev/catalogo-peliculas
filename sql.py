import sqlite3
from constantes import *

def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    return conexion, cursor


def agregar_pelicula(pelicula):
    conexion, cursor = conectar_db()

    try:
        cursor.execute("INSERT INTO pelicula (nombre, duracion, genero) VALUES (?, ?, ?);",
                       (pelicula.nombre, pelicula.duracion, pelicula.genero))
        conexion.commit()

    except sqlite3.Error as error:
        print(f"Error al agregar película. Error: {error}")

    finally:    
        conexion.close()
    



def obtener_peliculas():
    conexion, cursor = conectar_db()

    query = """
SELECT pelicula.id,
pelicula.nombre,
pelicula.duracion,
genero.nombre AS genero
FROM pelicula
JOIN genero ON pelicula.genero = genero.id"""
    cursor.execute(query)
    peliculas = cursor.fetchall()

    conexion.close()
    return peliculas


def agregar_genero(genero):
    conexion, cursor = conectar_db()

    try:
        cursor.execute("INSERT INTO genero (nombre) VALUES (?);", (genero.nombre,))
        conexion.commit()
        
    except sqlite3.Error as error:
        print(f"Error al agregar el género. Error: {error}")


    finally:    
        conexion.close()


def obtener_generos():
    conexion, cursor = conectar_db()
    query = "SELECT nombre FROM genero;"
    cursor.execute(query)
    generos = cursor.fetchall()

    conexion.close()
    return generos


def obtener_id_genero_por_nombre(nombre_genero):
    conexion, cursor = conectar_db()

    cursor.execute("SELECT id FROM genero WHERE nombre = ?;", (nombre_genero,))

    resultado = cursor.fetchone()
    conexion.close()

    return resultado[0] if resultado else None