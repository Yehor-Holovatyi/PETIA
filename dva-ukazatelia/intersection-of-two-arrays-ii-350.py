class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # we look at what numbers are repeated and how many times

        count1 = Counter(nums1)  # Counter for nums1
        count2 = Counter(nums2)  # Counter for nums2
        # we count how many times it repeats

        result = []
        # empty list

        for num in count1:
            # look at the list of numbers 1

            if num in count2:
                # there is a number in the second list

                times = min(count1[num], count2[num])
                # number of repetitions

                result += [num] * times
                # add a number with repetition

        return result

