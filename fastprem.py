import numpy as np


def random_prem(n):
    return np.random.permutation(n)


def reversed_prem(prem):
    d = np.zeros(prem.shape, dtype=np.int16)
    for i in range(prem.shape[0]):
        d[prem[i]] = i
    return d


def d_matrix(cube, prem):
    n = cube.shape[0]

    d = np.zeros((n, n), dtype=np.int16)
    prem_rev = reversed_prem(prem)
    for j in range(n):
        for k in range(n):
            d[(j, k)] = cube[(prem_rev[k], j, k)]
    return d


if __name__ == "__main__":
    n = 10
    x = np.arange(27).reshape((3, 3, 3))
    print(d_matrix(x, random_prem(3)))
