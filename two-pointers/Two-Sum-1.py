class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two numbers that add up to target

        seen = {}
        #

        for i, num in enumerate(nums):
            #look at the number and index (0-0)

             diff = target - num
             #the number that is missing

             if diff in seen:
                 #for the number that was it we will return it to the index

                 return [seen[diff], i]
             seen[num]=i
             #save current number and its index

