# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


#metodasprawdza zbieżność do danego pierwiastka i zwraca do którego zbioru ma należeć
def newton(z, f, df, max_iter=300, tol=1e-6):
    for i in range(max_iter):
        move = f(z)/df(z)
        if abs(move) < tol:
            return i, z
        z -= move
    return i, z


#metoda ma za dla każdeku punktu sprawdzyć do którego zbieru należy i na tej podstawie generuje fraktal
def plot_newton_basins(p, pprime, n=1000, extent=[-1.5, 1.5, -1.5, 1.5], c_map='brg'):
    #przygotowanie zmiennych
    root_count = 0
    roots = {}
    m = np.zeros((n, n))
    x_min, x_max, y_min, y_max = extent
    #iterowanie po całej przestrzeni
    for r, x in enumerate(np.linspace(x_min, x_max, n)):
        for s, y in enumerate(np.linspace(y_min, y_max, n)):
            z = x + y*1j
            #pobiera przynależność do danego zrboru rozwiązania
            root = np.round(newton(z, p, pprime)[1], 1)
            #zapisywanie zbiorów rozwiązań
            if root not in roots:
                roots[root] = root_count
                root_count += 1
            #przypisanie danego punktu do zbioru rozwązań
            m[r, s] = roots[root]
    #generowanie wykresu
    plt.imshow(m.T, cmap=c_map, extent=extent)
    plt.show()


############################################################################

#zdefiniowanie badanej funckji
function = lambda x: x**5 + 1

#zdefiniowanie pochodnej badaniej funckji
derivative_function = lambda x: 5*x**4

#owywołanie metody odpowiedzialnej za wygenerowanie wykresu
plot_newton_basins(function, derivative_function)
