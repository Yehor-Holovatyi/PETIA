class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #the program from two rows of numbers must build one in the correct order maybe ¯\_(ツ)_/¯

        count=Counter(nums) 
        #schitayem(count) the repetition of numbers

        nums.sort(key=lambda x: (count[x], -x)) 
        # (key=lambda x: (count[x], -x)) compare numbers; example x=5 and count[5]=3 we see it 3 time

        return nums

