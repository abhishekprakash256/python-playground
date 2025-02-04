"""
make the maximum sliding window for the array 
"""

lst1 = [4,5,4,4,6,1,7,8,0]
lst2 = [8,6,4,7,0,1,4,3,6,4,3,2,1,0]



class Solution:
    def monotonic_queue(self,lst):
        """
        find the max value in the sliding window to find in the window
        """
        queue = []
        l = 0
        r = 0

        