class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #  set of numbers from nums1 nums2 so that they do not repeat

        set1= set(nums1)
        set2=set(nums2)
        # list=>set(nabor)

        result= set1 & set2
        # we take the numbers that are the same in both sets

        return list(result)
        # set=>list ┐(‘～` )┌


