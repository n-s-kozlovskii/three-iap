import numpy as np


def random_prem(n):
    return np.random.permutation(n)


def reversed_prem(prem):
    d = np.zeros(prem.shape, dtype=np.uint8)
    for i in range(prem.shape[0]):
        d[prem[i]] = i
    return d


def d_matrix(cube, prem):
    n = cube.shape[0]

    d = np.zeros((n, n), dtype=np.uint8)
    prem_rev = reversed_prem(prem)
    for j in range(n):
        for k in range(n):
            d[(j, k)] = cube[(prem_rev[k], j, k)]
    return d


def main_algo(cube, pi):
    f = 0
    j = 0
    d = d_matrix(cube, pi)
    n = d.shape[0]
    k_set = set([i for i in range(n)])
    while j < n:
        s = np.argmin([d[j][i] for i in k_set])
        k_set = set(k_set) - {s}
        f = f + d[j][s]
        k = j + s
        if k < n:
            k_set = k_set | {k}  # union
        j += 1
        # print('iteration j=', j)
        # print('\tk: ', k)
        # print('\tsignum =', s)
        # print('\tdelta =', d[j][s])
        j += 1
    return f


def naive_algo(cube, n_iteration):
    i = 1
    prem = random_prem(cube.shape[0])
    m = main_algo(cube, prem)
    while i < n_iteration:
        prem = random_prem(cube.shape[0])
        tmp = main_algo(cube, prem)
        if tmp < m:
            m = tmp
        i += 1
    return m


if __name__ == "__main__":
    n = 1000
    x = np.random.randint(1, 9, n ** 3, dtype=np.uint8).reshape((n, n, n))
    print(naive_algo(x, 100))
