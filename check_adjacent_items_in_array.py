def adjacent(nums):
	i=0
	counter=0
	
	for i in range(len(nums)-1):
		
		if nums[i]==nums[i+1]:
			counter=counter+1
			return True
			
	if counter==0:
		return False
			


print(adjacent([1,2,3,4,5,6]))