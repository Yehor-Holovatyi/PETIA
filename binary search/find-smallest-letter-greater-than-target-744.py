class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #guess numbers with binary search

        left = 0
        # list started 0
        
        right = len(letters) - 1

        while left <= right:

            mid = ( left + right )//2

            if letters[mid] <= target:

                left = mid + 1

            else:

                right = mid -1

        return letters[left % len(letters)]
    # if you don't find it we will return the previous one