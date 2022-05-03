class Solution(object):
    def containerWithMostWater(self, height):
        # init left, right, max_area, length 
        max_area = 0
        length = len(height)
        left_pointer = 0
        right_pointer = length - 1

        # condition to ensure within range
        while (left_pointer < right_pointer):
            # calculate max_area
            max_area = max(max_area, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))

            # move appro. pointer that is shorter in length 
            if (height[left_pointer] < height[right_pointer]):
                left_pointer += 1
            else:
                right_pointer -= 1

        # return max_area
        return max_area

#Time comp: O(n)
#Space comp: O(1)