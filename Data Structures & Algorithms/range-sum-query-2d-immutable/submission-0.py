class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix_with_prefix_sum = [[0]*len(row) for row in matrix]
        row_len, col_len = len(matrix), len(matrix[0])

        # for i in range(0, row_len):
        #     current_row_sum = 0
        #     for j in range(0, col_len):
        #         if i == 0:
        #             if j==0:
        #                 self.matrix_with_prefix_sum[i][j] = matrix[i][j]
        #             else:
        #                 self.matrix_with_prefix_sum[i][j] = matrix[i][j] + self.matrix_with_prefix_sum[i][j-1]
        #         else:
        #             current_row_sum += matrix[i][j]
        #             # row_prefix_sum = matrix[i][j] + self.matrix_with_prefix_sum[i][j-1] if j>0 else matrix[i][j]
        #             self.matrix_with_prefix_sum[i][j] = current_row_sum + self.matrix_with_prefix_sum[i-1][j]

        for i in range(0, row_len):
            current_row_sum = 0
            for j in range(0, col_len):
                current_row_sum += matrix[i][j]
                if i == 0:
                    self.matrix_with_prefix_sum[i][j] = current_row_sum
                else:
                    self.matrix_with_prefix_sum[i][j] = current_row_sum + self.matrix_with_prefix_sum[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        sum = self.matrix_with_prefix_sum[row2][col2]
        right_top_corr = (row1 -1, col2)
        left_bottom_corr = (row2, col1 - 1)

        if row1 > 0:
            sum -= self.matrix_with_prefix_sum[right_top_corr[0]][right_top_corr[1]]

        if col1>0:
            sum -= self.matrix_with_prefix_sum[left_bottom_corr[0]][left_bottom_corr[1]]

        if row1 > 0 and  col1>0:
            sum+= self.matrix_with_prefix_sum[row1-1][col1-1]

        return sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)