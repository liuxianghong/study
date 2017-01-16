critics={'Lisa':{'Lady':1.8, 'Snakes1':3.0, 'Snakes2':3.0, 'Snakes3':3.0}
,'Lisb':{'Lady':5.5, 'Snakes1':2.0, 'Snakes2':4.0, 'Snakes3':3.5, 'Snakes4':1.8}
,'Lisc':{'Lady':4.5, 'Snakes1':6.0, 'Snakes2':4.4, 'Snakes3':2.5, 'Snakes4':2.8}
,'Lisd':{'Lady':2.5, 'Snakes1':2.1, 'Snakes2':4.5, 'Snakes3':1.5, 'Snakes4':3.4}
,'Lise':{'Lady':1.8, 'Snakes1':3.0, 'Snakes2':3.0, 'Snakes3':3.0, 'Snakes4':5.0}}

from math import sqrt

def sim_distance(prefs,person1,person2):
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	if len(si) == 0:
		return 0
	sum_of_squares = sum(pow(prefs[person1][item] - prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2])
	return 1/(1+sqrt(sum_of_squares))

def sim_pearson(prefs,person1,person2):
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	n = len(si)
	if n == 0:
		return 1
	sum1 = sum([prefs[person1][item] for item in si])
	sum2 = sum([prefs[person2][item] for item in si])

	sum1sq = sum([pow(prefs[person1][item],2) for item in si])
	sum2sq = sum([pow(prefs[person2][item],2) for item in si])

	psunm = sum([prefs[person1][item] * prefs[person2][item] for item in si])

	num = psunm - (sum1*sum2/n)

	sq = (sum1sq - pow(sum1,2)/n) * (sum2sq - pow(sum2,2)/n)
	den = sqrt(sq)
	if den == 0:
		return 0

	r = num/den
	return r

def topMatches(prefs,person,n=5,similarity=sim_pearson):
	scores = [(similarity(prefs,person,other), other) 
				for other in prefs if other!= person]
	scores.sort()
	scores.reverse()
	return scores[0:n]

def getRecommend(prefs,person,similarity=sim_pearson):
	totals = {}
	simSums = {}
	for other in prefs:
		if other == person:
			continue
		sim = similarity(prefs,person,other)
		if sim <= 0:
			continue
		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item] == 0:
				totals.setdefault(item,0)
				totals[item] += prefs[other][item] * sim
				simSums.setdefault(item,0)
				simSums[item] += sim
	rankings = [(total / simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
	return rankings

def transformPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person] = prefs[person][item]
	return result
			


