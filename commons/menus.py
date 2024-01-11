from commons.utils import option_validation,clean_screen,print_modified

def main_menu():
    clean_screen()
    print_modified("-","SISTEMA GESTOR DE PELICULAS BLOCKBUSTER","-","|")
    print("1. Administrador de Generos")
    print("2. Administrador de Actores")
    print("3. Administrador de Formatos")
    print("4. Gestor de Peliculas")
    print("5. Gestor de Informes")
    print("6. Salir")       

    op=option_validation("Opcion: ",1,6)
    return op

def genres_menu():
    clean_screen()
    print_modified("-","GESTOR DE GENEROS","-","|")
    print("1. Crear genero")
    print("2. Listar generos")
    print("3. Ir a Menu principal")
    op=option_validation("Opcion: ",1,3)
    return op

def actors_menu():
    clean_screen()
    print_modified("-","GESTOR DE ACTORES","-","|")
    print("1. Crear Actor")
    print("2. Listar Actores")
    print("3. Ir a menu principal")
    op=option_validation("Opcion: ",1,3)
    return op

def formats_menu():
    clean_screen()
    print_modified("-","GESTOR DE FORMATOS","-","|")
    print("1. Crear formatos")
    print("2. Listar formatos")
    print("3. Ir a menu principal")
    op=option_validation("Opcion: ",1,3)
    return op

def movies_menu():
    clean_screen()
    print_modified("-","GESTOR DE PELICULAS","-","|")
    print("1. Agregar pelicula")
    print("2. Editar pelicula")
    print("3. Eliminar pelicula")
    print("4. Eliminar Actor")
    print("5. Buscar pelicula")
    print("6. Listar todas las peliculas")
    print("7. Ir a menu principal")
    op=option_validation("Opcion: ",1,7)
    return op

def reports_menu():
    clean_screen()
    print_modified("-","GESTOR DE INFORMES","-","|")
    print("1. Listar las peliculas de un genero especifico")
    print("2. Listar las peliculas donde el protagonista sea Silvester Stallone")
    print("3  Buscar pelicula,mostrar la sinopsis y los actores ")
    print("4. Ir a menu principal")
    op=option_validation("Option: ",1,4)
    return op

def yes_or_no_menu(question):
    print(question)
    print("1. Si")
    print("2. No")
    op = option_validation("Opcion: ",1,2)
    return op

def key_menu(dictionary_name):#return the key that the user decide
    keys = list(dictionary_name.keys())
    n = len(keys)
    op = 0
    for i  in range(1,n+1):
        print(str(i)+". "+keys[i-1].replace("_"," ")+": "+dictionary_name[keys[i-1]]["nombre"].replace("_"," "))
    op = option_validation("Opcion: ",1,n)
    return keys[op-1]

def key_menu_movies(dictionary_name):#return the key that the user decide
    keys = list(dictionary_name.keys())
    n = len(keys)
    op = 0
    for i  in range(1,n+1):
        print(str(i)+". "+keys[i-1].replace("_"," ")+": ")
    op = option_validation("Opcion: ",1,n)
    return keys[op-1]