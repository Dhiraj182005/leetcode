class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        answer = [[] for _ in range(r)]

        row_size = len(mat)
        col_size = len(mat[0])
        k = 0
        if (row_size * col_size) == (r * c):
            for i in range(row_size):
                for j in range(col_size):
                    newRow= k // c
                    answer[newRow].append(mat[i][j])
                    k+=1
        else:
            return mat   
        return answer                      
        