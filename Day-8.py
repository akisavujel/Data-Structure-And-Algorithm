# 344. Reverse string

class Solution(object):
    def reverseString(self, s):
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r],s[l]
            l,r = l+1,r-1        

'''
Lmao finally ek week leetcode question gere paxi
balla aja euta question buje .
String simple xa solution😁
'''
    
