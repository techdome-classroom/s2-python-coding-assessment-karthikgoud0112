class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')':'(','{':'}',']':'['}
        for char in mapping:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char]
        """
        :type s: str
        :rtype: bool
        """
        pass







    



  

