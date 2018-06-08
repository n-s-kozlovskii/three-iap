from random import shuffle
from premutation import Premutation

#размерность задачи


def random_vector(n):
	vector = [i for i in range(1,n+1)]
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

def print_cube(cube):
	print('begin', '='*10)
	for i, square in enumerate(cube):
		print('#', i, ' [')
		for vector in square:
			print(vector)
		print(']')
	print('end', '='*12)

def empty_vector(n):
	return [0 for i in range(n)]

def empty_square(n):
	return [empty_vector(n) for i in range(n)]



def d_matrix(cube):
	n = len(cube)
	pi = Premutation.random(n)
	pi_rev = pi.reversed()
	d = empty_square(n)
	for j in range(n):
		for k in range(n):
			d[j][k] = cube[pi_rev[j+1]-1][j][k]
	return d

def signum(d):
	js = []
	for vector in d:
		min_value = min(vector)
		js.append((vector.index(min_value), min_value))
	j, value = min(js, key=lambda x: x[1])


c = random_cube(5)
print_cube(c)
d = d_matrix(c)
for vector in d:
	print(' '.join([str(i) for i in vector])) 

