def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	num_vec= len(vectors)

	cov= [[0]*num_vec for _ in range(num_vec)]

	l_mean= []
	for i in vectors:
		l_mean.append(1.0*sum(i)/len(i))
	
	for i in range(num_vec):
		for j in range(num_vec):
			a=0
			for k in range(len(vectors[0])):
				a= a+ (vectors[i][k]-l_mean[i])*(vectors[j][k]-l_mean[j])
			a=1.0*a/(len(vectors[0])-1)
			cov[i][j]=a

	return cov