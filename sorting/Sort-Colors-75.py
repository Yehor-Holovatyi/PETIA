class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        # (nums.sort()) the command rearranges the numbers in order: num [1 4 0 3 2]; nums.sort() [0 1 2 3 4]