import platform
import time
import unicodedata
import re
from os import system

def clean():
    """
    Clears the console
    """
    os = platform.system().lower()
    if 'windows' in os:
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


def delay(secs):
    time.sleep(secs)
