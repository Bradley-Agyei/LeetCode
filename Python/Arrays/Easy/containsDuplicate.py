#Problem: Given a list of integers, return True if an integer appears at least twice in list
#Input: [1,2,3,1] output: True 
#Approach: Use hashset 

class Solution(object):
    def containsDuplicate(nums):
        #define hashset 
        hashset = set() 

        #loop through nums and see if num is already in set, if so return true
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 

    #Driver code 
    if __name__ == "__main__":
        test_case = [1,2,3,5,9,32,3]
        print(containsDuplicate(test_case))


#Time comp: O(n)
#Space comp: O(n)