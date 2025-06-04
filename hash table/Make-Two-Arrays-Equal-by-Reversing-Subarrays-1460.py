class Solution:
     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # i have target and arr, i have task if they match then it's true, if not then it's false 

        target_sorted=sorted(target)

        arr_sorted=sorted(arr)
        #sorts the numbers in this way [1 2 3 4 5 6]

        if target_sorted==arr_sorted:
        # if clones write true
            return True
        else:
            return False
        
