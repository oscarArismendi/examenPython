from commons.utils import load_json,save_json,stop,print_modified,clean_screen,option_validation
from commons.menus import key_menu,yes_or_no_menu,key_menu_movies

def show_genre(file_path_movies):
    clean_screen()
    movies = load_json(file_path_movies)
    movies = movies["blockbuster"]#acorto los diccionarios
    movies = movies["peliculas"]#vuelto a acortar los diccionarios
    genre_name = input("Ingrese el nombre del genero: ")
    found = False
    for id in movies:
        for id_g in movies[id]["generos"]:
            if(movies[id]["generos"][id_g]["nombre"].lower() == genre_name.lower()):
                print("Se encontro la pelicula")
                print("id :",movies[id]["id"])
                print("nombre :",movies[id]["nombre"])
                print("duracion :",movies[id]["duracion"])  
                print("sinopsis :",movies[id]["sinopsis"])
                print("genero:",genre_name)
                found = True  

    if(not found):
        print("No se encontraron peliculas de ese genero")
    stop()

def show_Silvestre(file_path_movies):
    clean_screen()
    movies = load_json(file_path_movies)
    movies = movies["blockbuster"]#acorto los diccionarios
    movies = movies["peliculas"]#vuelto a acortar los diccionarios
    actor_name = "Silvester Stallone"
    found = False
    for id in movies:
        for id_g in movies[id]["actores"]:
            if(movies[id]["actores"][id_g]["nombre"].lower() == actor_name.lower()):
                print("Se encontro la pelicula")
                print("id :",movies[id]["id"])
                print("nombre :",movies[id]["nombre"])
                print("duracion :",movies[id]["duracion"])  
                print("sinopsis :",movies[id]["sinopsis"])
                print("genero:",actor_name)
                found = True  

    if(not found):
        print("No se encontraron peliculas de ese genero")
    stop()

def search_movie(file_path_movies):
    clean_screen()
    movies = load_json(file_path_movies)
    movies = movies["blockbuster"]#acorto los diccionarios
    movies = movies["peliculas"]#vuelto a acortar los diccionarios
    movie_name = input("Ingrese el nombre de la pelicula: ")
    found = False
    for id in movies:
            if(movies[id]["nombre"].lower() == movie_name.lower()):
                print("Se encontro la pelicula")
                print("id :",movies[id]["id"])
                print("nombre :",movies[id]["nombre"])
                print("duracion :",movies[id]["duracion"])  
                print("sinopsis :",movies[id]["sinopsis"])
                print("genero:",movie_name)
                found = True  

    if(not found):
        print("No se encontraron peliculas de ese genero")
    stop()
