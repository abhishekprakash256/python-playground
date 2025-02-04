"""
To find the dupliacte number in the list 
using the fast and the slow pointer and without using the extra space 
"""
#----------------------------- the soln works and passes the test cases ------------------
#test cases

test1 = {
	'input': [3,4,5,5,1,6,5],
	'output': 7
}

test2 = {
	'input': [0],
	'output': None
}

test3 = {
	'input': [1,2,3,4,4],
	'output': 4
}

test4 = {
	'input': [1,1,1,1,1,1],
	'output': 1
}


class Solution:
	def find_duplicate(self,nums):
		"""
		The function to find the duolicate number in the list
		Args:
			duo_lst (list): The list of the numbers duolicate 
		Return:
			repeated_num (int) : the repeated number in the list
		"""

		fast = slow = nums[0]
	
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if slow == fast:
				break
		
		slow = nums[0]
	
		while slow != fast:
			slow = nums[slow]
			fast = nums[fast]
		
		return fast



if __name__ == "__main__":
	sol = Solution()
	res = sol.find_duplicate(test1['input'])

	print(res)