import json
import re

def load_levels(level_data : str) -> list:
    '''load the information from a json to a list
    param: a path of an archive json
    return: a list of levels'''
    with open(level_data,"r") as file_object:
        levels_list = json.load(file_object)["levels"]
        return levels_list

def validate_name(received_string : str) -> bool:
    '''Esta funcion que recibe un string y devuelva True 
    en caso de que trate solo de 5 caracteres alfabéticos y False en el caso contrario'''
    m_return = False
    if re.match("[^A-Z]{1,5}",received_string):
        m_return = True
    else:
        m_return = False
    return m_return
