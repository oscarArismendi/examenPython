
from commons.utils import load_json,save_json,stop,print_modified,clean_screen
def new_genre(file_path_genres):
    genres = load_json(file_path_genres)
    name_genre = input("Ingrese el nombre del nuevo genero: ")
    new_id = "G"
    list_genres = list(genres.keys())
    for id in list_genres:#verificar si ya esta el genero
        if genres[id]["nombre"].lower() == name_genre.lower():
            print(f"Ya se ha ingresado el genero {name_genre}")
            stop()
            return
    n_generes =len(list_genres)#cantidad de generos
    n_generes += 1
    if(n_generes < 10):#cero a la izquierda para los numeros de un digito
        new_id += "0"
    new_id += str(n_generes)
    genres[new_id] = {
        "id" : new_id,
        "nombre" : name_genre
    }
    save_json(genres,file_path_genres)

def show_genres(file_path_genres):
    clean_screen()
    genres = load_json(file_path_genres)
    print_modified("-","","-","|")
    for id in genres:
        print_modified("",id+": "+genres[id]["nombre"]," ","|")
    stop()