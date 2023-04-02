from converter import construct_query, search_parameters, check_sentence
from prolog_bridge import ask_query
from util import press_to_continue, sanitize_input,clean


while True:
    try:
        clean()
        answer = sanitize_input(input("\nIngresa tu pregunta: "))
        params = search_parameters(answer)
        good_sentence = check_sentence(params)

        print("\n💭 Respuesta:\n")
        if not good_sentence:
            print('🤔 No he podido entender tu pregunta, por favor, intenta de nuevo...\n')
        else:
            result = ask_query(construct_query(params))
            print(result)

        press_to_continue()

    except (EOFError, KeyboardInterrupt):
        exit()
