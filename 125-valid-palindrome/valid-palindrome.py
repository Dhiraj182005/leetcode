class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        def check(left,right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return check(left +1,right -1)
        return check(0,len(s)-1)
            

        