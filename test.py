def ranges(nums,limit=999):
	nums = sorted(set(nums))
	gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
	edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
	z = list(zip(edges, edges))
	newz = []
	for x in z:
		if x[1]-x[0] > limit:
			prev = x[0]
			for o in range((x[1]-x[0])//limit):
				newz.append((prev,prev+limit))
				prev = prev + limit
			newz.append((prev,prev+(x[1]-x[0])%limit))
			prev = prev + (x[1]-x[0])%limit
			
		else:
			newz.append(x)
	return newz

print(ranges([0,1,2,3,4,5,6,7,8,9,10,11,12,13,19,20,21,123,12345,12346],limit=2))