import math

def list_mean(L):
	if L is None:
		return None
	if len(L) == 0:
		return None
	
	s = 0

	for l in L:
		try:
			s += l
		except:   # value error not raising?
			raise ValueError(
				'Unsupported' +
				'value in list.')

	return s/len(L)


def list_stdev(L):
	s = 0
	for l in L:
		s += l
    
	return math.sqrt(sum([((s/len(L))-x)**2 for x in L]) / len(L))
