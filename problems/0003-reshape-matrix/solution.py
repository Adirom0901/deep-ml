import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	b,c= new_shape
	if b*c != (len(a)*len(a[0])):
		return []
	a= np.asarray(a)
	a= np.reshape((a), new_shape)
	a.tolist()
	return a