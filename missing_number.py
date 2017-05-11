
"""Compares two arrays, returns the values that are not common to both"""
def find_missing(list_1, list_2):
	combined_list = list_1 + list_2	#generates a new list to be iterated over
									 #by combining the two input lists"""
	output = [] #new list to be returned

	if list_1 == list_2: #i.e if all elements in list_1 are also in list_2
		return 0

	for num in combined_list:
		if num not in list_1 or num not in list_2: 
			output.append(num)
	return output

print
print find_missing([5,4,6,7,11,66], [5,4,1,7,6,11,66])
print find_missing([1,2], [1,2,5])
print find_missing([],[])
print find_missing([],[0])
print