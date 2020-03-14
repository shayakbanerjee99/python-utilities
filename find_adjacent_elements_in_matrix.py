# mat: matrix
# x: x coordinate
# y: y coordinate
# n: order of the matrix
def find_dir(x, y, m, n):
	#possible directions for adjacent elements
	adj_p = 0
	if y == 0:
		if x == 0:
			adj_p = ['R', 'D']
		elif x < m-1:
			adj_p = ['L', 'R', 'D']
		else: # x == m-1
			adj_p = ['L', 'D']
	elif y < n-1:
		if x==0:
			adj_p = ['U', 'R', 'D']
		elif x < m-1:
			adj_p = ['U', 'R', 'D', 'L']
		else: # x == m-1
			adj_p = ['U', 'L', 'D']
	else: # y == n-1
		if x == 0:
			adj_p = ['U', 'R']
		elif x < m-1:
			adj_p = ['U', 'L', 'R']
		else: # x == m-1
			adj_p = ['U', 'L']
	return adj_p
	
def get_val_from_dir(mat, x, y, directions):
	# values are returned in the order UP, LEFT, RIGHT, DOWN in a list and -1, in case there is no value
	list_of_values = list()
	if 'U' in directions:
		list_of_values.append(mat[y-1][x])
	else:
		list_of_values.append(-1)
	
	if 'L' in directions:
		list_of_values.append(mat[y][x-1])
	else:
		list_of_values.append(-1)
	
	if 'R' in directions:
		list_of_values.append(mat[y][x+1])
	else:
		list_of_values.append(-1)
	
	if 'D' in directions:
		list_of_values.append(mat[y+1][x])
	else:a
		list_of_values.append(-1)
	return list_of_values
	
def get_adjacent(mat, x, y):
	return get_val_from_dir(mat, x, y, find_dir(x, y, len(mat[0]), len(mat)))
	

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# 01 02 03 04
# 05 06 07 08
# 09 10 11 12
# 13 14 15 16

print(get_adjacent(mat, 1, 1))
