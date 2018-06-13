from random import shuffle, randint, seed

from munkres import Munkres
from premutation import Premutation
from multiprocessing import Process
from tqdm import tqdm

import sys


def random_vector(n):
    vector = [randint(0, 20) for i in range(1, n + 1)]
    shuffle(vector)
    return vector


def random_square(n):
    square = []
    for i in range(n):
        square.append(random_vector(n))
    return square


def random_cube(n):
    cube = []
    for i in range(n):
        cube.append(random_square(n))
    return cube


def empty_vector(n):
    return [1 for i in range(n)]


def empty_square(n):
    return [empty_vector(n) for i in range(n)]


def empty_cube(n):
    return [empty_square(n) for i in range(n)]


def id_cube(n):
    c = empty_cube(n)
    for i in range(n):
        c[i][i][i] = 0
    return c


def print_square(d):
    print('=' * 3, 'd_matrix', '=' * 3)
    for vector in d:
        print(' '.join([str(j) for j in vector]))
    print('=' * 3, '========', '=' * 3)


def print_cube(cube):
    print('begin', '=' * 10)
    for i, square in enumerate(cube):
        print('#', i, ' [')
        for vector in square:
            print(vector)
        print(']')
    print('end', '=' * 12)


def d_matrix(cube, pi):
    n = len(cube)
    pi_rev = pi.reversed()
    d = empty_square(n)
    for j in range(n):
        for k in range(n):
            d[j][k] = cube[pi_rev[j + 1] - 1][j][k]
    return d


def signum(d, k):
    """
    принимает d[j], где j это некоторое
    фиксированное число 1 .. n
    возвращает номер наименьшего элемента из множества
    d[j=const, k_ in k]
    """
    argmin = [(d[k_], k_) for k_ in k]
    signum_ = min(argmin, key=lambda x: x[0])[1]
    return signum_


def main_algo(cube, pi):
    f = 0
    j = 0
    d = d_matrix(cube, pi)
    # print_square(d)
    n = len(d)
    k = [i for i in range(n)]
    while j < n:
        s = signum(d[j], k)
        k = set(k) - set([s])
        f = f + d[j][s]

        # print('iteration j=', j)
        # print('\tk: ', k)
        # print('\tsignum =', s)
        # print('\tdelta =', d[j][s])

        j += 1
    return f


def naive_algo(cube, n_iteration):
    return min([main_algo(cube, Premutation.random(len(cube))) for i in range(n_iteration)])


def optimized_algo(cube, n_iteration):
    i = 0
    j = 0
    n = len(cube)
    answers = []
    pi = Premutation.random(n)
    m_value = 1000
    while i < n_iteration:
        res = main_algo(cube, pi)
        answers.append(res)
        if res == 0:
            return res
        elif res < m_value and j < n:
            m_value = res
            j = j + 1
            pi = pi.smart_shuffled()
        else:
            pi = Premutation.random(n)
            j = 0
        i += 1
    return min(answers)


def munkres(cube, n_iteration):
    i = 0
    n = len(cube)
    answers = []
    m = Munkres()
    while i < n_iteration:
        pi = Premutation.random(n)
        d = d_matrix(cube, pi)
        indexes = m.compute(d)
        total_cost = 0
        for r, e in indexes:
            x = d[r][e]
            total_cost += x
        answers.append(total_cost)
        i += 1
    return min(answers)


if __name__ == '__main__':
    # c = [[[]]]
    # if len(sys.argv) > 1:
    #     arg = sys.argv[1].split('=')
    #     if arg[0] == 'seed':
    #         seed(int(arg[1]))  # fix randomness
    #         c = random_cube(5)
    #     elif arg[0] == 'idcube':
    #         c = id_cube(50)
    # else:
    #     c = random_cube(100)
    lens = [3, 5, 10, 20, 50, 100, 200, 500, 1000]
    iters = [5, 10, 100, 150, 300, 500, 1000]
    funs = [naive_algo, optimized_algo, munkres]
    fun_namses = ['naive_algo', 'optimized_algo', 'munkres']
    for l in lens:
        c = id_cube(l)
        for itr in iters:
            print("len =", l, 'iter =', itr)
            for fun, name in zip(funs, fun_namses):
                asw = fun(c, itr)
                print('\t', name, ":", asw)
            print('='*20)
