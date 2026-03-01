# 169. Majority Element

class Solution(object):
    def majorityElement(self, nums):
    
        num_list = dict()
        for i in nums:
            if not i in num_list:
                num_list[i] = 1
            else:
                num_list[i] += 1

        return max(num_list, key = num_list.get)
        
