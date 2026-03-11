# 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        # use two pointers
        left = 0
        right = len(s) - 1

        # while left pointer is less then right pointer
        while left < right:
            # if left pointer is not number iterate
            if not s[left].isalnum():
                left += 1
                continue
            # if right pointer is not number negative iterate
            if not s[right].isalnum():
                right -= 1
                continue
            # change to uppercase
            # if not same return false
            if s[right].upper() != s[left].upper():
                return False

            left += 1
            right -= 1
        return True
            
