import re
import platform
import unicodedata
from os import system

def get_os_name():
    return platform.system().lower()

def press_to_continue():
    if 'windows' in get_os_name():
        system('pause')

def clean():
    if 'windows' in get_os_name():
        system('cls')
    else:
        system('clear')


def sanitize_input(inpt):
    answer = inpt.lower()
    # remove accents 
    answer = ''.join(c for c in unicodedata.normalize('NFD', answer) if unicodedata.category(c) != 'Mn')
    # remove double spaces https://stackoverflow.com/a/1546245/20370244
    answer = re.sub("\s\s+" , " ", answer)
    # remove other characters
    answer = re.sub("[^a-z\s]+", "", answer)
    return answer
