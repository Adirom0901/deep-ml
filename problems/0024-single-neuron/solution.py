import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	import numpy as np

	features= np.asarray(features)
	
	weights= np.asarray(weights)
	m,n= np.shape(features)

	forw= np.matmul(features,weights.T) +bias

	probabilities= [round(1.0/(1+math.e**(-i)),4) for i in forw]
	

	mse=0
	for i in range(m):
		mse+= (probabilities[i]-labels[i])**2

	mse=round(mse/m,4)

		



	return probabilities, mse