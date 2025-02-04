"""
Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.

print(lst1.pop(0))

"""

#-----------------code fixed for popping of the monotonic stack------------------------

#for this question we need to make a deccreasing monotonic queue 


#test cases

lst1 = [4,5,4,4,6,1,7,8,0]


lst2 = [8,6,4,7,0,1,4,3,6,4,3,2,1,0]



class Solution:
	def decrease_queue(self,lst):
		"""
		The function to make the decreasing queue

		"""
		lst_queue = []

		#start the comparision and popping 

		for i in lst:

			#monotonic decreasing
			while True:

				if len(lst_queue) == 0:

					lst_queue.append(i)
					break

				elif lst_queue[len(lst_queue) - 1]  >= i:

					lst_queue.append(i)

					break

				else:

					lst_queue.pop(0)

		return lst_queue

	def maximum_window(self,lst,k):
		"""
		The maximum sliding window finding on the stack

		"""
		pass

		

		



if __name__ == "__main__":
	sol = Solution()
	res = sol.decrease_queue(lst2)

	print(res)