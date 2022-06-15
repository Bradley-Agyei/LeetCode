class Solution(object):
    def maxPoints(self, cardPoints, k):
        # init left and right pointer, current_total, max_points 
        left, right = 0, (len(cardPoints) - k)
        current_total = sum(cardPoints[right:])
        max_points = current_total 

        # loop to ensure all subarrays are calculated
        while right < len(cardPoints):
            # update current_total
            current_total += (cardPoints[left] - cardPoints[right])

            # update max_points
            max_points = max(max_points, current_total)

            # increment pointers
            left += 1
            right += 1

        # return max_points
        return max_points

# time comp: O(k)
# space comp: O(1)