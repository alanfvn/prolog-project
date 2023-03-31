from pyswip import Prolog

prolog = Prolog()
prolog.consult("familia.pl")

def ask_query(question):
    print(question)
    result = list(prolog.query(question))
    return result
