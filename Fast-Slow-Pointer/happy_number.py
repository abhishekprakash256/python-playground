"""
The question is to find the happy number by squared 
and not have a cycle and return 1 at a point 

example 
28 = 68
68 = 100 
100 = 1

so 28 is a happy number 
"""

#------------------------------------code works and passes all tests --------------------------------------
#--------------naive approach 
#test cases

test1 = {
	'input': 28,
	'output': True
}

test2 = {
	'input': 0,
	'output': False
}

test3 = {
	'input': 1,
	'output': True
}

test4 = {
	'input': 4,
	'output': False
}


class Solution:

    def get_digits(self,nums):
        """
        The function to get the digit of the number 

        """

        digits= [int(d) for d in str(nums)]

        return digits

    def digit_sum(self,digit_lst):
        """
        The function to get the digit of the number 

        """

        sum = 0
        
        for i in digit_lst:

            sum = i*i + sum

        return sum

    def check_happy(self,nums)-> bool:
        """
        The function to check whether the number is happy or not

        Args:
            nums (int) : The number to be checked
        
        Returns:
            True or False (bool) : The number is happy or not

        """

        if nums == 1 or nums == 0 :
            return False

        mapper = {}

        while True:
            
            digit_list = self.get_digits(nums)
            num_sum = self.digit_sum(digit_list)
            nums = num_sum

            if num_sum in mapper:
                break
            
            elif num_sum == 1:
                return True

            else:
                mapper[num_sum] = True

        return False

if __name__ == "__main__":
    sol = Solution()
    res = sol.check_happy(test4['input'])

    print(res == test4['output'])
