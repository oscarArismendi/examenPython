import os
from commons.menus import main_menu,genres_menu,actors_menu,formats_menu,movies_menu,reports_menu
from commons.utils import stop,file_path_generator
from business.genres import new_genre,show_genres
from business.actors import new_actor,show_actors
from business.formats import new_format,show_formats
from business.movies import new_movie,edit_movie,show_movies,remove_movie,search_movie,remove_actor
from business.reports import show_genre,show_Silvestre,search_movie

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path_genres = file_path_generator(script_directory,"data","genres.json") # Initial path Json campers
file_path_actors = file_path_generator(script_directory,"data","actors.json") # Initial path Json campers
file_path_formats = file_path_generator(script_directory,"data","formats.json") # Initial path Json campers
file_path_movies = file_path_generator(script_directory,"data","movies.json") # Initial path Json campers

while (True):
    op = main_menu()
    if op == 1:#genere menu
        try:
            while(True):
                op = genres_menu()
                if(op == 1):
                    new_genre(file_path_genres)
                elif(op == 2):
                    show_genres(file_path_genres)
                elif(op == 3):
                    break
        except Exception as e:
            print(f"players menu has the next error {e}")
    elif (op == 2):#actors menu
        try:
            while(True):
                op = actors_menu()
                if(op == 1):
                    new_actor(file_path_actors)
                elif(op == 2):
                    show_actors(file_path_actors)
                elif(op == 3):
                    break
        except Exception as e:
            print(f"players menu has the next error {e}")
    elif (op == 3):#formats menu
        try:
            while(True):
                op = formats_menu()
                if(op == 1):
                    new_format(file_path_formats)
                elif(op == 2):
                    show_formats(file_path_formats)
                elif(op == 3):
                    break
        except Exception as e:
            print(f"players menu has the next error {e}")  
    elif (op == 4):#movies menu
        try:
            while(True):
                op = movies_menu()
                if(op == 1):
                    new_movie(file_path_genres,file_path_actors,file_path_formats,file_path_movies)
                elif(op == 2):
                     edit_movie(file_path_movies)
                elif(op == 3):
                    remove_movie(file_path_movies)
                elif(op == 4):
                     remove_actor(file_path_movies)
                elif(op == 5):
                     search_movie(file_path_movies)
                elif(op == 6):
                     show_movies(file_path_movies)
                elif(op == 7):
                    break
        except Exception as e:
            print(f"players menu has the next error {e}")
    elif (op == 5):#report menu
        try:
            while(True):
                op = reports_menu()
                if(op == 1):
                    show_genre(file_path_movies)
                elif(op == 2):
                    show_Silvestre(file_path_movies)
                elif(op == 3):
                    search_movie(file_path_movies)
                elif(op == 4):
                    break
        except Exception as e:
            print(f"players menu has the next error {e}")    
    elif(op == 6):
        print("Que tenga un buen dia!")
        break
    