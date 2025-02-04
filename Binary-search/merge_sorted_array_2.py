"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


"""


#make the test cases 


test1 = {
	'input': {
	'lst': [1,2,3],
    'lst2':[4,5,6],
	},

	'output': [1,2,3,4,5,6]
}  


test2 = {
	'input': {
	'lst': [1,2,3],
    'lst2':[3,3,3],
	},

	'output': [1,2,3,3,3,3]
}


test3 = {
	'input': {
	'lst': [1],
    'lst2':[3,3,3],
	},

	'output': [1,3,3,3]
}

test4 = {
	'input': {
	'lst': [1,2,3,7,8,9],
    'lst2':[4,5,6],
	},

	'output': [1,2,3,4,5,6,7,9]
}



class Solution:
	def merge_sorted_array(self,lst1,lst2):
		"""
		The function to merge the two sorted array 

		Args:
			lst1 (list): The list of sorted integers
			lst2 (list): The list of sorted integers

		Returns:
			sorted_lst (list) : The merged sorted list of integers 
		"""

		merge_lst = []

		len1 = len(lst1)
		len2 = len(lst2)


		left = 0 
		right = 0 


		while len(merge_lst) >= (len1 + len2):

			if left == len1:

				merge_lst.append(lst2[right])
				right +=1


			elif right == len2:

				merge_lst.append(lst1[left])
				left +=1


			elif lst1[left] < lst2[right]:

				merge_lst.append(lst1[left])
				left+=1

			elif lst2[right] < lst1[left]:

				merge_lst.append(lst2[right])
				right+=1

			else:

				merge_lst.append(lst1[left])
				merge_lst.append(lst2[right])

				left +=1
				right+=1


		return merge_lst



if __name__ == "__main__":
	sol = Solution()


	res = sol.merge_sorted_array(test2['input']['lst'],test2['input']['lst2'])


	print(res)



