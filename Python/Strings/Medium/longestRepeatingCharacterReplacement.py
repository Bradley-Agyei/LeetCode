class Solution(object):
    def longestRepeatingCharacterReplacement(self, s, k):
        # map to count the occurrences of characters
        count = {}
        length = len(s)

        # init left pointer, max_length, max_frequency
        left, max_length, max_frequency = 0, 0, 0

        # loop through s 
        for right in range(length):

            # get count of chars
            count[s[right]] = 1 + count.get(s[right], 0)
            max_frequency = max(max_frequency, count[s[right]])

            # check if window is valid, decrement count of char, and move left pointer 
            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1

            # update max_length 
            max_length = max(max_length, right - left + 1)

        return max_length 

# Time comp: O(n)
# Space comp: O(n)