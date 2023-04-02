from pyswip import Prolog

prolog = Prolog()
prolog.consult("familia.pl")


def construct_query(qst):
    rel = qst['relation']
    p1 = qst['f_parameter']
    p2 = qst['s_parameter']
    return f'{rel}({p1}, {p2})'


def construct_response(qst, resp):
    response = ''
    rel = qst['relation']
    p1 = qst['f_parameter']
    p2 = qst['s_parameter']

    for index, result in enumerate(resp, start=1):
        if not result:
            # dictionary is empty so response is true
            return "✅ Verdadero\n"

        response += f'{index}.) '
        if "X" in result and "Y" in result:
            response += f'{result["X"]} es {rel} de {result["Y"]}'
        elif "X" in result:
            response += f'{result["X"]} es {rel} de {p2}'
        elif "Y" in result:
            response += f'{p1} es {rel} de {result["Y"]}'
        response += '\n'

    return response

def ask_query(question):
    query = construct_query(question)
    result = list(prolog.query(query))

    if len(result) >= 1:
        response = construct_response(question, result)
        return response
    else:
        # returns a empty list if the query is false
        return "❌ Falso\n"
