class Solution:
    def reverse(self, x: int) -> int:
        new_dig = 0
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)

        while x > 0:
            mod_dig = x %10
            new_dig = new_dig * 10 + mod_dig
            x = x // 10
        if is_negative == True:
            new_dig = -new_dig
        if new_dig < -2**31 or new_dig > 2**31 - 1:
            return 0
        return new_dig