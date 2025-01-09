class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=list(str(x))
        y.reverse()
        return y==list(str(x))
        