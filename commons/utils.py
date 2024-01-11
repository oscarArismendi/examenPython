import json,os

# # #functions about json
def save_json(database,file_path):
    try:
      with open(file_path, 'w') as archivo_json:
        json.dump(database, archivo_json, indent=2)
        
    except FileNotFoundError:
        print("The JSON doesn't exist")
    except json.JSONDecodeError:
        print("The format of the archive is not JSON")
    except Exception as e:
        print("Unknow error")
        
def load_json(file_path):
    try:
      with open(file_path, 'r') as archivo_json:        
        campers = json.load(archivo_json)
        # print("You have load the list of campers")
        return campers
    except Exception as e:
      print(f"Error to load: {e}")

def file_path_generator(original_path,directory_name,json_name):
    data_directory = os.path.join(original_path, directory_name)
    if not os.path.exists(data_directory):# Create the "data" directory if it doesn't exist
        os.makedirs(data_directory)
    rta = os.path.join(data_directory, json_name)
    return rta
# # # general functions

def clean_screen():
    os.system('clear' if os.name == 'posix' else 'cls')    


def option_validation(statement,lower,upper):#return a int >= lower and <= upper
    while True:
        try:
            option =int(input(statement))
            if option>=lower and option<=upper:
                return option
            else:
                print(f"The option is not in the interval: ({lower}-{upper})")
        except ValueError:
            print("Please, type a valid number.")

def print_modified(left_part,text,right_part,last_character):
    
    if(left_part == ""):
        left = 0
    else:
        left = int((50-len(text))/2)
    right = 50 - left - len(text)-1
    print((left_part*left)+text+(right_part*right)+last_character)

def stop():
    print_modified("-","","-","-")
    print_modified("-","Pulse enter para continuar:","-","|")
    input()

def search_for_keys(list_name,key,value):#return a list with dictionaries
    if(isinstance(value,str)):
        result = [data for data in list_name if data.get(key).lower() == value.lower()]
        return result
    else:
        result = []
        for data in list_name:
            if(data[key] == value):
                result.append(data)
        return result

def print_card(list_name):
    
    for person in list_name:
        print(("-"*49)+"|")
        for data in person:
            spaces_len = 44-len(data)
            if(isinstance(person[data],str)):
                spaces_len -= len(person[data])
                print(data,":",person[data],(" "*spaces_len),"|")    
            elif(isinstance(person[data],int),isinstance(person[data],float)):
                numero = str(person[data])
                spaces_len -= len(numero)
                print(data,":",numero,(" "*spaces_len),"|")  
            else:
                
                print_modified("",str(data).replace("_"," ")+":"," ","|")
                for value in person[data]:
                    print_modified("","-"+value," ","|")

def key_menu(dictionary_name):#return the key that the user decide
    keys = list(dictionary_name.keys())
    print(keys)
    stop()
    n = len(keys)
    op = 0
    for i  in range(1,n+1):
        print(str(i)+". "+keys[i-1].replace("_"," "))
    op = option_validation("Option: ",1,n)
    return keys[op-1]

