def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	from collections import defaultdict
	# Your code here
	mpp=defaultdict(list)
	for epoch in range(max_iterations):
		dis=[]
		for p in points:
			minn=float('inf')
			clu=-1
			for i in range(len(initial_centroids)):
				dist=0
				for j in range(len(initial_centroids[i])):
					dist= dist+ (initial_centroids[i][j]-p[j])**2
					
				dist= dist**0.5
				if minn>dist:
					minn=dist
					clu=i
			mpp[clu].append(p)

		for k,l in mpp.items():

			summ=[0 for _ in range(len(initial_centroids[0]))]
			for j in range(len(l)):
				for c in range(len(l[j])):
					summ[c]+=l[j][c]


			meann= tuple([i/len(l) for i in summ])

			initial_centroids[k]=meann
	return initial_centroids




	


	return final_centroids