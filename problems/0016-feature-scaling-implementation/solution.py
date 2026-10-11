import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	
	mean= np.mean(data, axis=0)
	std=np.std(data, axis=0)

	standardized_data= np.round((data- mean)/std,4)
	maxx= np.max(data,axis=0)
	minn= np.min(data,axis=0)

	normalized_data=np.round((data-minn)/(maxx-minn),4)
	return standardized_data, normalized_data