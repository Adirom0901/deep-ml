def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	b=0
	for i in range(2):
		b+=matrix[i][i]
	
	
	c= matrix[0][0]*matrix[1][1]- matrix[1][0]*matrix[0][1]

	r1= (b+(b**2 - 4*c)**0.5)/2.0
	r2= (b-(b**2 - 4*c)**0.5)/2.0

	return sorted([r1,r2],reverse=True)


	
	
	return eigenvalues