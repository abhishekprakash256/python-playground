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
        queue.append(lst[0])
        #start the queue addition

        for i in lst:
            if queue[len(queue)-1] < i:
                
                while len(queue) !=0:
                    queue.pop(0)
            queue.append(i)

        return queue
    
    def find_max(self,lst,window_size):
        """
        Find the max size in the window 
        """
        step = window_size
        queue = []
        count = 0
        max_val = []

        for i in lst:

            if count >= window_size:
                queue.pop(0)
            
            count +=1
            queue.append(i)
        
        return queue




if __name__ == "__main__":
    sol = Solution()
    res = sol.monotonic_queue(lst2)
    small_queue = sol.find_max(lst1,3)
    print(res)
    print(small_queue)
