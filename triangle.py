import math

def triangle(N,a,b):
	for i in range(N):	
		# init coordinates
		x_a = -a[i]+1
		coord_list_a = []
		x_b = -b[i]+1
		coord_list_b = []

	        error_bound = 0.0000000001
		while x_a < abs(a[i]-1):
			if math.sqrt(a[i]**2-x_a**2) - int(math.sqrt(a[i]**2-x_a**2)) < error_bound:
				coord_list_a.append([x_a,int(math.sqrt(a[i]**2-x_a**2))])
				coord_list_a.append([x_a,-int(math.sqrt(a[i]**2-x_a**2))])
		   	x_a += 1
		while x_b < abs(b[i]-1):
			if math.sqrt(b[i]**2-x_b**2) - int(math.sqrt(b[i]**2-x_b**2)) < error_bound:
				coord_list_b.append([x_b,int(math.sqrt(b[i]**2-x_b**2))])
				coord_list_b.append([x_b,-int(math.sqrt(b[i]**2-x_b**2))])
		   	x_b += 1
		
		print coord_list_a
		print coord_list_b
		
		cnt = 0
		if (coord_list_a == [] or coord_list_b == []):
			print "FALSE"
		else:
			for i in range(len(coord_list_a)):
				for j in range(len(coord_list_b)):
					if coord_list_a[i][0] * coord_list_b[j][0] + coord_list_a[i][1] * coord_list_b[j][1] == 0:
						cnt += 1
			if cnt > 0:
				print "TRUE"
			else:
				print "FALSE"
			
triangle(3,[1,5,5],[1,5,10])