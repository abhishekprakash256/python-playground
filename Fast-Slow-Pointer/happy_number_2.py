"""
The question is to find the happy number by squared 
and not have a cycle and return 1 at a point 

example 
28 = 68
68 = 100 
100 = 1

so 28 is a happy number 
"""

#---------------------------optimize approach ----------------------------------
#--------------------------- the code works -------------------------------------

from happy_number import * 


class Solution:

    def is_happy_number_2(self,nums):
        """
        The function uses a fast and slow pointer approach to check the number is happy or not 

        Args:
            nums (int) : the number to be checked 
        
        Return:
            True or False (bool): return the bool value true or false
        """

        if nums == 1:
            return True

        slow = nums
        fast = self.get_digit_sum(self.get_digit_sum(slow))
        
        while True:

            if slow == fast:
                break
            
            elif slow == 1 or fast == 1:
                return True
            
            slow = self.get_digit_sum(slow)
            fast = self.get_digit_sum(self.get_digit_sum(fast))
        
        return False


    def get_digit_sum(self,nums):
        """
        The supporting function to find the sum of digit 

        """

        total_sum = 0 

        while nums > 0 :

            digit = nums % 10
            nums = nums // 10 
            total_sum = total_sum + digit*digit
        
        return total_sum


if __name__ == "__main__":
    sol = Solution()
    res1 = sol.is_happy_number_2(test1['input'])
    res2 = sol.is_happy_number_2(test2['input'])
    res3 = sol.is_happy_number_2(test3['input'])
    res4 = sol.is_happy_number_2(test4['input'])

    print(res1 == test1['output'])
    print(res2 == test2['output'])
    print(res3 == test3['output'])
    print(res4 == test4['output'])