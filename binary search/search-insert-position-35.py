class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            # (range(6)): generated number from 0 to 5 (0; 1; 2; 3; 4; 5.)

            # (len): looks how many elements are inside

            if nums[i] >= target:

                return i
            
        return len(nums)
        
        # if the number doesn't match then it goes to the end
        # there was an error return was in the same line with IF and case 1 and 2 did not work I don't know why  ¯\_(ツ)_/¯
