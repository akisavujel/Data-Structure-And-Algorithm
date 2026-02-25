# 283. Move Zeroes 

class Solution(object):
    def moveZeroes(self, nums):
        
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1
        return nums    
'''
This code follows a two pointers technique.
starting from the left pointer considered as zero and 
the right pointer starting from left will iterate the value
if the right pointer value is non zero 
it is replaced value with left pointer
'''

# 217. Contains Duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
'''
we need to compare every number with all element in list
create a hashset
start a loop for each element in nums 
if the nums is present in hashset return true
if nums isnt present in hashset append and return false
'''        

# 26. Remove Duplicate From Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
    
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
'''
left pointer placed at index 1
if right pointer in nums isnot equal to num - 1
index change in left pointer and right pointer
increment left pointer
'''

# 69. Sqrt(x)

class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r-1)//2)
            if m**2 > x:
                r = m-1
            elif m**2 < x:
                l = m + 1
                res = m
            else:
                return m
        return res
        

        