hombre(argelio).
hombre(david).
hombre(humberto).
hombre(alan).
mujer(florinda).
mujer(ericka).
mujer(olga).
mujer(jackeline).
progenitor(argelio, olga).
progenitor(florinda, olga).
progenitor(david, humberto).
progenitor(ericka, humberto).
progenitor(olga, alan).
progenitor(humberto, alan).
progenitor(olga, jackeline).
progenitor(humberto, jackeline).
madre(M,H):- progenitor(M,H), mujer(M).
padre(P,H):- progenitor(P,H), hombre(P).
hijo(H,P):- progenitor(P,H), hombre(H).
hija(H, P):- progenitor(P,H), mujer(H).
hermana(HA, HO):- progenitor(X, HA), progenitor(X, HO), mujer(HA).
hermano(HO, HA):- progenitor(X, HO), progenitor(X, HA), hombre(HO).
abuelo(A, N):- progenitor(X, N), progenitor(A, X), hombre(A).
abuela(A, N):- progenitor(X, N), progenitor(A, X), mujer(A).
nieta(N, A):- progenitor(A, X), progenitor(X, N), mujer(N).
nieto(N, A):- progenitor(A, X), progenitor(X, N), hombre(N).
