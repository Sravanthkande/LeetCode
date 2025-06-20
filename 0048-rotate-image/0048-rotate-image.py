class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Optimal approach using three steps
        #transpose entire matrix
        #reverse each row in matrix

        N = len(matrix)

        for i in range(N):
            for j in range(i+1,N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        for row in matrix:
            row.reverse()
        
        return matrix