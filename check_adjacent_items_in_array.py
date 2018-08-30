def adjacent(nums):
	i=0
	
	while i<len(nums)-1:
		#print("present")
		if nums[i]==nums[i+1]:
			#print("present")
			i=i+1
			return True
			
			print(i)
		else:
			i=i+1
			print(i)
			return False

print(adjacent([1,2,3,3,5,6]))