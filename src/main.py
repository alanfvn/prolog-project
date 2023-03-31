from converter import construct_query, search_parameters, check_sentence
from util import sanitize_input,clean
from prolog_bridge import ask_query


while True:
    try:
        clean()
        answer = sanitize_input(input("Ingresa tu pregunta: "))
        params = search_parameters(answer)
        good_sentence = check_sentence(params)


        print('\n')
        if not good_sentence:
            print('❌ No he podido entender tu pregunta, porfavor intenta de nuevo...')
        else:
            query = construct_query(params)
            result = ask_query(query)
            print(result)

        input("\n\nPresiona cualquier tecla para continuar...")
    except (EOFError, KeyboardInterrupt):
        exit()
