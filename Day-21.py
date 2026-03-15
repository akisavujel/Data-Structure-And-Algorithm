# 350. Intersection of Two Arrays II

class Solution(object):
    def intersect(self, nums1, nums2):
        count = {} #create a hashmap
        list = [] #creare an empty list

        for i in nums1: #use loop in nums1
            if i in count: #if the element exist in hashmap
                count[i]+=1 # iterate
            else:
                count[i] = 1 #if not value remains one
        
        for i in nums2: #use loop in nums2
            if i in count and count[i] > 0: #if element exist in hashmap and count is 1 or more
                list.append(i) #append the value in list
                count[i]-=1 #and negative iterate from hashmap
        return list #return list values
