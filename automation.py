def automation(rule,iteration,N,init_condition): 

	# initialize initial state
	init_state = [int(x) for x in bin(init_condition)[2:]] # convert state to binary representation
	temp = N - len(init_state)
	while temp > 0:
		init_state = [0] + init_state
		temp = temp - 1
	#print init_state
	# convert rule to binary format:
	rule_bin = [int(x) for x in bin(rule)[2:]] 
	temp = 8 - len(rule_bin)
	while temp > 0:
		rule_bin = [0] + rule_bin
		temp = temp - 1
	#print rule_bin
	x = ''
	for i in range(N):
			if str(init_state[i]) == '0':
				temp = ' '
			else:
				temp = "*"
			x = x + temp
	out = []
	out_with_counter = ''
	out.append('-'+x+'-')
	out_with_counter = '1   '+out[-1]
	print out_with_counter
	counter = 2
	while counter <= iteration:
		new_state = []
		i_prev = 0
		i_next = 0
		#print init_state
		for i in range(N):
			#deal with out-of-range blocks
			if i==0:
				i_prev = 0
				i_next = init_state[i+1]
			elif i+1==N:
			        i_prev = init_state[i-1]
				i_next = 0
			else: 
				i_prev = init_state[i-1]
				i_next = init_state[i+1]
			current_state = [i_prev,init_state[i],i_next]
			new_state.append(Rule(current_state,rule_bin))
		#print new_state
		init_state = new_state
		#print init_state
		new_state_output = ''
		for i in range(N):
			if str(new_state[i]) == '0':
				temp = ' '
			else:
				temp = "*"
			new_state_output = new_state_output + temp
		out.append('-'+new_state_output+'-')
                if out[-1] == out[-2]:
                    pass
                else:
                    out_with_counter = str(counter).ljust(4,' ') + out[-1]
		    print out_with_counter
		counter += 1
		#init_state = new_state
		#print init_state


# return next state based on rule and current state
def Rule(current_state,rule):
	next_state = []
	if current_state == [1,1,1]:
		next_state = rule[0]
	elif current_state == [1,1,0]:
		next_state = rule[1]
	elif current_state == [1,0,1]:
		next_state = rule[2]
	elif current_state == [1,0,0]:
		next_state = rule[3]
	elif current_state == [0,1,1]:
		next_state = rule[4]
	elif current_state == [0,1,0]:
		next_state = rule[5]
	elif current_state == [0,0,1]:
		next_state = rule[6]
	elif current_state == [0,0,0]:
		next_state = rule[7]
	return next_state





automation(40, 30, 8, 16)

