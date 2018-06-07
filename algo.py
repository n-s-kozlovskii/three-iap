from random import shuffle

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


print_cube(random_cube(5))