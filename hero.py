import math

# hero_STAT: [0]: name; [1]: ability, [2]: set of two numbers
def hero(N,hero_STAT):
	q = []
	f = 0
	z = 0

	# calculate hero score
	for i in range(len(hero_STAT[2])):
		f = int(float(hero_STAT[2][i][0])/(float(hero_STAT[2][i][1]) + float(hero_STAT[2][i][0]))*100)
		q.append(f*(i+1))
	q1 = sorted(q,reverse = True)
	print q
	print q1
	qN_index = []
	k = 0
	while k < N:
		indices = [i for i, x in enumerate(q) if x == q1[k]]
		print indices
		if len(indices) > N:
		      for j in range(N):
			 qN_index.append(indices[j])
			 k += len(indices)
		else:
		    for j in range(len(indices)):
			 qN_index.append(indices[j])
			 k += len(indices)
        print qN_index
	for i in range(len(qN_index)):
		print hero_STAT[0][qN_index[i]]
		
	# count_intelligence = 0
	# count_strength = 0
	# count_agility = 0
	# for i in range(len(hero_STAT[1])):
	# 	if hero_STAT[1][i] == 'intelligence':
	# 		count_intelligence += 1
	# 	elif hero_STAT[1][i] == 'strength':
	# 		count_strength += 1
	# 	elif hero_STAT[1][i] == 'agility':
	# 		count_agility += 1
	count_selected_intelligence = 0
	count_selected_strength = 0
	count_selected_agility = 0
	for i in range(len(qN_index)):
		if hero_STAT[1][qN_index[i]] == 'intelligence':
			count_selected_intelligence += 1
		elif hero_STAT[1][qN_index[i]] == 'strength':
			count_selected_strength += 1
		elif hero_STAT[1][qN_index[i]] == 'agility':
			count_selected_agility += 1
	ratio_intelligence = int((float(count_selected_intelligence)/float(N))*100)
	ratio_strength = int((float(count_selected_strength)/float(N))*100)
	ratio_agility = int((float(count_selected_agility)/float(N))*100)

	print ' '
	print 'This set of heroes:'
	print 'Contains %d percentage of Intelligence' %(ratio_intelligence)
	print 'Contains %d percentage of Strength' %(ratio_strength)
	print 'Contains %d percentage of Agility' %(ratio_agility)


hero(5,[['a,b','silencer','tiny','spectre','dazzle'],['intelligence','strength','agility','intelligence','intelligence'],[[60,40],[30,70],[20,80],[15,85],[12,88]]])
