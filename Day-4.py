# 66. Plus One
'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''
class Solution(object):
    def plusOne(self, digits):
        digits = digits[::-1] # Reverse the list
        a, i = 1, 0 # A represent the carry 
        while a: # Code runs till there is a carry
            if i < len(digits): # Check the digit one by one
                if digits[i] == 9: # If the digit is 9 then write 0 for 10
                    digits[i] = 0 
                else: # Else increment the number
                    digits[i] += 1
                    a = 0 # It means no carry, false
            else:
                digits.append(1) # If the list is 0 it adds one
                a = 0
            i += 1
        return digits[::-1]
        
