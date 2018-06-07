from tabulate import tabulate
from random import shuffle

class Premutation:
	"""
	Описывает перестановку.
	Перестановка -- отображение {1,2, ... N} на себя
	
	Premutation((4,1,5,3,1)

	  1    2    3    4    5
	 ---  ---  ---  ---  ---
  	  4    1    5    3    1

	"""

	def random(n):
		data = [i for i in range(1,n+1)]
		shuffle(data)
		return Premutation(data)
	
	def __validate_input(self, prem):
		return len(range(max(prem))) == len(prem) \
			and set(range(1, len(prem)+1))==set(prem)

	def __init__(self, prem):
		if self.__validate_input(prem):
			self._data = prem
		else:
			raise Exception('prem not correct')
		self._str_repesentation = tabulate(
			[[str(i) for i in self._data]], 
			headers=[str(i) for i in range(1, len(self._data)+1)]
			)
		self._data_len = len(prem)

	def __len__(self):
		return self._data_len

	def __getitem__(self, key):
		return self._data[key-1]

	def __str__(self):
		return self._str_repesentation

	def __mul__(self, other):
		assert len(self) == len(other)
		data = [self[other[i]] for i in range(1, len(self)+1)]
		return Premutation(data)

	def reversed(self):
		data = [0 for i in range(len(self))]
		for i in range(len(self)):
			# self -- перестановка, нумерация ячеек
			# начиается с 1 до N, где N=len(self)
			# data -- список, нумерация ячеек 0 .. N-1,
			# но data должна быть легальной перестановкой, 
			# любой элемент data[i] in 1..N
			data[self[i+1]-1] = i+1
		return Premutation(data)
