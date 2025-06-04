class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # +-like the game wordley, only harder

        left = 0
        # pointer on the left

        right = len(s) - 1 
        # (S) Length
        # it's like taking one away from the last element, and how people go towards each other
        # len s  last element

        while left < right:
            # people didn't reach each other

             temp = s[left]
             #saved the letter on the left
             
             s[left] = s[right]
             # put the letter on the left on the right 

             s[right] = temp 
             # standing on the left saved letter

             left += 1
             right -= 1
             # left to right, right to left
             