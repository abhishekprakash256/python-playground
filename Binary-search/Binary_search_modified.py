"""
The implementation of the modified binary search 
for the repetative element in the list
"""

#----------------------------------the working code for the problem---------------------------------------------#

from Binary_search import * 

class Modify_Sol(Solution):

    def modified_binary_search(self,lst,query)-> int:
        """
        The function to find the value in the list even repeated elements 
        Args:
            lst (list) : The sorted list of integers 
            query (int) : The query to find in the list 

        Returns:
            index (int) : The index value of the query 
        """

        left = 0 
        right = len(lst) - 1 

        while left <= right:

            mid = (left+right) // 2

            if lst[mid] == query:
                
                if mid == 0:
                    return mid
                
                elif lst[mid - 1] > query:
                    return mid
                else:
                    right = mid - 1        
 
            elif lst[mid] > query:

                left = mid + 1

            else:
                right = mid - 1

        return -1



if __name__ == "__main__":
    sol = Modify_Sol()
    res = sol.modified_binary_search(test3['input']['cards'], test3['input']['query'])
    res2 = sol.modified_binary_search(test5['input']['cards'], test5['input']['query'])

    print(res == test3['output'])
    print(res2 == test5['output'])