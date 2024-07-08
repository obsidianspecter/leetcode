class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        return original == reversed_num

solution = Solution()
x = 121
print(solution.isPalindrome(x))  

x = -121
print(solution.isPalindrome(x))  

x = 10
print(solution.isPalindrome(x)) 
