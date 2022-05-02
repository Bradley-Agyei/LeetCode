class Solution(object):
    def rotateImage(self, matrix):
        self.transpose(matrix)
        self.reverse(matrix)


    # transpose function
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    # reverse function or reverse method can be called 
    def reverse(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

#Time comp: O(M)
#Space comp: O(1) - done in-place 
