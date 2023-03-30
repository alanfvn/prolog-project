from pyswip import Prolog

prolog = Prolog()
prolog.consult("familia.pl")

lista = list(prolog.query("madre(X,raquel)"))

print(lista)
