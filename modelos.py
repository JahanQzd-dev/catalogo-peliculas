# Definición de los objetos Película, Género, Catálogo y sus atributos

class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

class Genero:
    def __init__(self, nombre):
        self.nombre = nombre

class Catalogo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []