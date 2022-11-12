#Multimi

#ex3

import functools

def my_filter(f, s):
    return functools.reduce(lambda acc, element_multime: acc | {element_multime} if f(element_multime) else acc, s, set())

m3 = my_filter(lambda x: x % 2 == 0, {1, 2, 3, 4})
print("ex3: ", m3)

#ex5


#ex5 a)

def reuniune_lista(lista):
    if len(lista) > 0:
        head = lista[0]
        tail = lista[1:]
        return head | reuniune_lista(tail)
    else:
        return set()

print("ex5 a) reuniune: ", reuniune_lista([{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]))

#ex5 b)

reuniune = reuniune_lista([{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}])

def intersectie_lista(lista):
    if len(lista) > 0:
        head = lista[0]
        tail = lista[1:]
        return head & intersectie_lista(tail)
    else:
        return reuniune

print("ex5 b) intersectie: ", intersectie_lista([{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]))
#ex6

#ex6a)

def mult_cif(n):
    if n == 0:
        return set()
    else:
        cf = n % 10
        return mult_cif(n // 10) | {cf}

m6a = mult_cif(127)
print("ex6 a) reuniune: ", m6a)

#ex6b)

def mult_cif_mult_reuniune(m):
    return functools.reduce(lambda acc, element: mult_cif(element) | acc, m, set())

m6b = mult_cif_mult_reuniune({1234, 123, 127})
print("ex6 b) reuniune mult cif: ", m6b)

#ex6c)

def mult_cif_mult_intersectie(m):
    return functools.reduce(lambda acc, element: mult_cif(element) & acc, m, mult_cif_mult_reuniune(m))

m6c = mult_cif_mult_intersectie({1234, 123, 127})
print("ex6 c): intersectie mult cif", m6c)

#Dictionare

#ex5

def adauga_pereche(pereche, d, f):
    cheie, valoare = pereche
    d[cheie] = f(valoare)
    return d

def my_map(d, f):
    return functools.reduce(lambda d_nou, pereche: adauga_pereche(pereche, d_nou, f), d.items(), {})

print("ex5: ", my_map({'a': 5, 'b': 7, 'c': 6}, lambda x: x + 1))

#ex6

def mult_comune(dictionar, lista):
    if len(lista) > 1:
        head = lista[0]
        tail = lista[1:]
        if head in dictionar.keys():
            return {dictionar[head]} | mult_comune(dictionar, tail)
        else:
            return mult_comune(dictionar, tail)
    else:
        return set()

print("ex6: ", mult_comune({'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']))