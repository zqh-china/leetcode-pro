class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 上下翻转
        for i in range(len(matrix)//2):
            matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]
        # 对角线翻转
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i > j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def showMatrix(mat):
    for i in range(len(mat)):
        print(mat[i])

if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7 ,8, 9]]
    showMatrix(matrix)
    s.rotate(matrix)
    showMatrix(matrix)
