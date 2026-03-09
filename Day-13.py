# 49. Group Anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        dictionary = {} # create an empty dictionary
        for i in strs: # loop through every values in strs
            words = str(sorted(i)) # sort the word and convert to string
            if words not in dictionary:
                dictionary[words] = [] # if the word is not presnet in dictonary create a new empty list
            dictionary[words].append(i) # append the value in list

        return dictionary.values() # return list values
