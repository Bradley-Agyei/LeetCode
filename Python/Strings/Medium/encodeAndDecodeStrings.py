class Solution(object):
    def encode(self, strs):
        # init result string 
        result = ""

        # loop through list of strings 
        for s in strs:
            # add length of string, delimiter, and string itself to result 
            result += str(len(s)) + "#" + s

        # return result
        return result 


    def decode(self, s):
        # init result list, starting pointer, i
        result, i = [], 0

        # ensure inbounds 
        while i < len(s):
            # set second pointer, j = i
            j = i

            # condition to check if j is delimiter "#"
            while s[j] != "#":
                j += 1
            # init length of string
            length = int(s[i:j])
            
            # append to result list and move pointer i
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length 

        # return result 
        return result 

#Time comp: O(n)
#Space comp: O(n)