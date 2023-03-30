hombre(jorge).
hombre(miguel).
hombre(pedro).
mujer(maria).
mujer(teresa).
mujer(elena).
mujer(raquel).
progenitor(pedro,teresa).
progenitor(maria,teresa).
progenitor(maria,elena).
progenitor(teresa,jorge).
progenitor(teresa,raquel).
progenitor(raquel,miguel).
madre(X,W):- progenitor(X,W), mujer(X).
padre(X,W):- progenitor(X,W), hombre(X).
