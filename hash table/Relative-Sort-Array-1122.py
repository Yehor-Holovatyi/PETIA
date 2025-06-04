class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []  
        # this is an empty list, we will write the answer into it

        for num in arr2:
            # looks at each number from

            while num in arr1:
             # as long as this number is in arrq
               
                result.append(num)  
                # + number to result

                arr1.remove(num)  
                # - a number with arr1 so that it doesn't repeat  

        arr1.sort()  
        # sorting numbers in arr1

        for num in arr1:
            # add last
            
            result.append(num)

        return result  
        # enter list
