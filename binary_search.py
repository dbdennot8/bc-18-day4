class BinarySearch(list):
	def __init__(self, first, a, b):
		"""Variables a,b are respectivery the length and step of 
		the list we're creating, when subclassing list"""
		super(BinarySearch, self).__init__(self)
		"""i.e., Inherit to 
		BinarySearch the arguments of the  parent class, list"""

		array_ = [num for num in range(first,a*b+1, b)]
		"""creates and array with the bracketed characteristics
		start at 0, step = (a*b) + 1, end at b"""
		self.a = len(array_) 
		self.extend(array_)
		length = self.a #initializing instance variable called length	

	def search(self, querry):
		"""method iterates thro' array and returns dict with
		count of number of iterations, and index of querry"""				
		count = 0
		index = 0
		first_element = 0
		last_element = len(self) - 1
		found = False		

		while first_element <= last_element and not found:
			midpoint = (first_element + last_element) // 2
			count += 1

			if self[midpoint] == querry:
				found = True
				index = self.index(querry)
			else:
				if querry < self[midpoint]:
					last_element = midpoint - 1					
				else:
					first_element = midpoint + 1							
		return {"count": count, "index":self.index(querry)}		 


paul = BinarySearch(10,100,10)
print
print len(paul)
print
print paul
print
print paul.search(500)
print
