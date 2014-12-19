# a: how many branches can a node carry
# b: how long are the words
# c: how many words
def trie(a,b,c):
	branch = [0]*(b+1)
	branch[0] = 1

	i = 1
	while i < len(branch):
		if a**(i) < c:
			branch[i] = a**(i)
		else:
			branch[i] = c
		i+=1
	memory = sum(branch)*4*a
	return memory
print trie(26,10**5,10**7)