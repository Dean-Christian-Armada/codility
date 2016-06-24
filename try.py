# def solution(A):
#     n = len(A)
#     L = [-1] + A
#     count = 0
#     pos = n // 2
#     candidate = L[pos]
#     for i in xrange(1, n + 1):
#         if (L[i] == candidate):
#             count = count + 1
#     if (count > pos):
#         return candidate
#     return -1

# # array = [2, 2, 2, 2, 1, 50]
# array = [2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 1, 1, 1, 1, 6]
# # array = [1, 1, 1, 1, 1, 1, 50]
# print solution(array)

# def solution(A, B):
# 	indices_count = 0
# 	indices = []
# 	B = [float(x) / 1000000 for x in B] # Make everything on the second array fractional
# 	C = [x + y for x, y in zip(sorted(A), sorted(B))] # Sum of array "A" and array "B"
# 	for x in range(0, len(C)):
# 		for _x in range(0, len(C)):
# 			if _x != x:
# 				_prod = C[_x] * C[x]
# 				_sum = C[_x] + C[x]
# 				temp = (x, _x)
# 				reversed_check = tuple(reversed(temp))
# 				reversed_check = reversed_check in indices
# 				if(_prod >= _sum and not reversed_check):
# 					indices.append((x, _x))
# 					indices_count += 1
# 	if indices_count > 1000000000:
# 		indices_count = 1000000000
# 	print indices_count
# 	return indices_count

# ([2, 3, 5], [500000, 500000, 6000000, 700000])
# array1 = [2, 3, 5]
# array2 = [500000, 500000, 6000000]
# array1 = [0, 1, 2, 2, 3, 3, 5]
# array2 = [500000, 500000, 0, 0, 0, 20000]
# solution(array1, array2)