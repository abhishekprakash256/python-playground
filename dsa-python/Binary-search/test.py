"""
test the binary search from the file 

"""

from Binary_search import Solution

test1 = [10,9,8,7,6,5,4,2]

sol = Solution()

res = sol.find_element_binary_search(test1,5)

"""
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

#res = binary_search(test1,6)
"""

print(res)