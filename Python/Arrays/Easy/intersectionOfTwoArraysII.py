class Solution(object):
    def intersectionOfTwoArraysII(self, nums1, nums2):
        # init i, j pointers, results list 
        i, j = 0, 0
        result = []
        n = len(nums1)
        m = len(nums2)

        # sort lists
        nums1.sort()
        nums2.sort()

        # iterate through both list and make comparisons, if value in nums1 == nums2, place in result 
        while(i < n and j < m):
            if(nums1[i] < nums2[j]):
                i += 1
            elif (nums1[i] > nums2[j]):
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result

#Time comp: O(n log n)
#Space comp: O(N)

