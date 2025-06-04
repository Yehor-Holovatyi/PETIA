class Solution:  # copy of LeetCode task number(1050) name(height checkers)
    def heightChecker(self, heights: List[int]) -> int: # copy of LeetCode task number(1050) name(height checkers)
        expected = sorted (heights)
        # sorting the  list by height; (expected)  na ruskom (pzhidayemyy) =D

        count=0 
        #count counter of loser students whore not their phase; (count) na ruskom (schitat')

        for i in range(len(heights)):
            # (range(6)): generated number from 0 to 5 (0; 1; 2; 3; 4; 5.)

            # (len): looks how many elements are inside; (len(heights)): counts elements in a list(height)

            # height=[180; 160; 188] (len) say its list have 3 elements; range(len(heights)) say its have 0; 1; 2

            # (i) is the number of elements start in 0; i=0 heights[i]=180
            if heights[i] != expected[i]:
                # (height[i]) how losers want to stand [170; 167; 180]; (expected[i]) but should stand [167; 170; 180]

                # (!=) its not the same ((5 !=110) true 5 not=3); (110 !=110) false (110=110)

                count += 1
        
        return count
    # all what is app copy add LeetCode link(https://leetcode.com/problems/height-checker/) 