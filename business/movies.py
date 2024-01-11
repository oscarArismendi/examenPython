from commons.utils import load_json,save_json,stop,print_modified,clean_screen,option_validation
from commons.menus import key_menu,yes_or_no_menu,key_menu_movies
def new_movie(file_path_genres,file_path_actors,file_path_formats,file_path_movies):
    movies = load_json(file_path_movies)
    genres = load_json(file_path_genres)
    actors = load_json(file_path_actors)
    formats = load_json(file_path_formats)
    name_movie = input("Ingrese el nombre del la pelicula: ")
    new_id = "P"
    movies = movies["blockbuster"]#acorto los diccionarios
    movies = movies["peliculas"]#vuelto a acortar los diccionarios
    list_movies = list(movies.keys())
    for id in list_movies:#verificar si ya esta la pelicula
        if movies[id]["nombre"].lower() == name_movie.lower():
            print(f"{name_movie} ya esta registrado")
            stop()
            return
    n_movies =len(list_movies)#cantidad de movieos
    n_movies += 1
    if(n_movies < 10):#cero a la izquierda para los numeros de un digito
        new_id += "0"
    new_id += str(n_movies)
    duration = input("Ingrese la duracion: ")
    synopsis = input("Ingrese la sinopsis: ")
    new_genres = {}
    while(True):#Agregar nuevos generos
        op = key_menu(genres)
        new_genres[op] = genres[op]
        op1 = yes_or_no_menu("Seguir agregando?")
        if(op1 == 2):
            break

    new_actors = {}
    while(True):#Agregar nuevos actores
        op = key_menu(actors)
        print("Seleccione el rol del actor: ")
        print("1. Protagonista")
        print("2. Antagonista")
        print("3. Reparto")
        op1 = option_validation("Opcion: ",1,3)
        new_rol = "protagonista"
        if(op1 == 2):
            new_rol = "antagonista"
        else:
            new_rol = "reparto"
        actors[op]["rol"] = new_rol
        new_actors[op] = actors[op]
        op1 = yes_or_no_menu("Seguir agregando")
        if(op1 == 2):
            break

    new_formats = {}
    while(True):#Agregar nuevo formato
        op = key_menu(formats)
        n_copias = 0
        valor_prestamo = 0
        while(True):
            try:
                n_copias = int(input("Ingrese el numero de copias que se tienen: "))
                if(n_copias < 0):
                    int("Fuerzo un error si es negativo")
                break
            except Exception:
                print("Porfavor ingrese un dato valido")
        while(True):
            try:
                valor_prestamo = int(input("Ingrese el valor del prestamo: "))
                if(valor_prestamo < 0):
                    int("Fuerzo un error si es negativo")
                break
            except Exception:
                print("Porfavor ingrese un dato valido")

        formats[op]["NroCopias"] = n_copias
        formats[op]["valorPrestamo"] = n_copias
        new_formats[op] = formats[op]
        op1 = yes_or_no_menu("Seguir agregando?")
        if(op1 == 2):
            break
    

    movies[new_id] = {
        "id" : new_id,
        "nombre" : name_movie,
        "duracion": duration,
        "sinopsis": synopsis,
        "generos": new_genres,
        "actores": new_actors,
        "formato": new_formats
    }
    movies = {
        "blockbuster":{
            "peliculas":movies
        }
    }   
    save_json(movies,file_path_movies)

def edit_movie(file_path_movies):
    clean_screen()
    movies = load_json(file_path_movies)
    movies = movies["blockbuster"]#acorto los diccionarios
    movies = movies["peliculas"]#vuelto a acortar los diccionarios
    op = key_menu(movies)
    op2 = key_menu_movies(movies[op])
    if(op2 != "actores" and op2 != "formato" and op2 != "generos"):
        new_value = input(f"el anterior valor era {movies[op][op2]}, digite el nuevo: ")
        movies[op][op2] = new_value
    else:
        op3 = key_menu_movies(movies[op][op2])
        op4 = key_menu_movies(movies[op][op2][op3])
        new_value = input(f"el anterior valor era {movies[op][op2][op3][op4]}, digite el nuevo: ")
        movies[op][op2][op3][op4] = new_value
    movies = {
        "blockbuster":{
            "peliculas":movies
        }
    }     
    save_json(movies,file_path_movies)

def remove_movie(file_path_movies):
    clean_screen()
    movies = load_json(file_path_movies)
    op = key_menu(movies["blockbuster"]["peliculas"])
    movies["blockbuster"]["peliculas"].pop(op)   
    save_json(movies,file_path_movies)

def remove_actor(file_path_movies):
    clean_screen()
    movies = load_json(file_path_movies)
    op = key_menu(movies["blockbuster"]["peliculas"])
    list_actors = list(movies["blockbuster"]["peliculas"][op]["actores"])
    if(len(list_actors) == 0):
        print("No se encuentran actores para eliminar")
        stop()
        return
    op2 = key_menu(movies["blockbuster"]["peliculas"][op]["actores"])
    movies["blockbuster"]["peliculas"][op]["actores"].pop(op2)   
    save_json(movies,file_path_movies)

def search_movie(file_path_movies):
    clean_screen()
    movies = load_json(file_path_movies)
    movies = movies["blockbuster"]#acorto los diccionarios
    movies = movies["peliculas"]#vuelto a acortar los diccionarios
    movie_name = input("Ingrese el nombre de la pelicula: ")
    found = False
    for id in movies:
        if(movies[id]["nombre"] == movie_name):
            print("Se encontro la pelicula")
            print("id :",movies[id]["id"])
            print("nombre :",movies[id]["nombre"])
            print("duracion :",movies[id]["duracion"])  
            print("sinopsis :",movies[id]["sinopsis"])
            found = True  

    if(not found):
        print("No se encontro una pelicula con ese nombre")
    stop()

def show_movies(file_path_movies):
    clean_screen()
    movies = load_json(file_path_movies)
    movies = movies["blockbuster"]#acorto los diccionarios
    movies = movies["peliculas"]#vuelto a acortar los diccionarios
    for id in movies:
        print_modified("-","","-","|")
        print_modified("",id+": "+movies[id]["nombre"]," ","|")
    stop()

