from converter import search_parameters
from util import sanitize_input,delay,clean


while True:
    try:
        clean()
        answer = sanitize_input(input("Ingresa tu pregunta: "))
        params = search_parameters(answer)

        print(params)

        delay(5)
    except (EOFError, KeyboardInterrupt):
        exit()
