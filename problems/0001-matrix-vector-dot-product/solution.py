def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	import numpy as np
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a= np.array(a)
	b=np.array(b)
	if len(np.shape(a))==1:
		return -1
	if np.shape(a)[1]!=np.shape(b)[0]:
		return -1
	ans= np.matmul(a,b)
	return ans
	pass