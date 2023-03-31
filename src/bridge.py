from pyswip import Prolog

prolog = Prolog()
prolog.consult("familia.pl")

lista = list(prolog.query("nieto(alan,X)"))

print(lista)
