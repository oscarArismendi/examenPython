from commons.utils import load_json,save_json,stop,print_modified,clean_screen

def new_format(file_path_formats):
    formats = load_json(file_path_formats)
    name_format = input("Ingrese el nombre del formato: ")
    new_id = "F"
    list_formats = list(formats.keys())
    for id in list_formats:#verificar si ya esta el formato
        if formats[id]["nombre"].lower() == name_format.lower():
            print(f"{name_format} ya esta registrado")
            stop()
            return
    n_formats =len(list_formats)#cantidad de formatos
    n_formats += 1
    if(n_formats < 10):#cero a la izquierda para los numeros de un digito
        new_id += "0"
    new_id += str(n_formats)
    formats[new_id] = {
        "id" : new_id,
        "nombre" : name_format
    }
    save_json(formats,file_path_formats)

def show_formats(file_path_formats):
    clean_screen()
    formats = load_json(file_path_formats)
    print_modified("-","","-","|")
    for id in formats:
        print_modified("",id+": "+formats[id]["nombre"]," ","|")
    stop()