from commons.utils import load_json,save_json,stop,print_modified,clean_screen

def new_actor(file_path_actors):
    actors = load_json(file_path_actors)
    name_actor = input("Ingrese el nombre del actor: ")
    new_id = "A"
    list_actors = list(actors.keys())
    for id in list_actors:#verificar si ya esta el actor
        if actors[id]["nombre"].lower() == name_actor.lower():
            print(f"{name_actor} ya esta registrado")
            stop()
            return
    n_actors =len(list_actors)#cantidad de actores
    n_actors += 1
    if(n_actors < 10):#cero a la izquierda para los numeros de un digito
        new_id += "0"
    new_id += str(n_actors)
    actors[new_id] = {
        "id" : new_id,
        "nombre" : name_actor
    }
    save_json(actors,file_path_actors)

def show_actors(file_path_actors):
    clean_screen()
    actors = load_json(file_path_actors)
    print_modified("-","","-","|")
    for id in actors:
        print_modified("",id+": "+actors[id]["nombre"]," ","|")
    stop()