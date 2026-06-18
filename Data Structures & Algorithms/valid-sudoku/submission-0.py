class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_sets = {
        "row0" : set(),
        "col0" : set(),
        "box0" : set(),        
        "row1" : set(),
        "col1" : set(),
        "box1" : set(),
        "row2" : set(),
        "col2" : set(),
        "box2" : set(),
        "row3" : set(),
        "col3" : set(),
        "box3" : set(),
        "row4" : set(),
        "col4" : set(),
        "box4" : set(),
        "row5" : set(),
        "col5" : set(),
        "box5" : set(),
        "row6" : set(),
        "col6" : set(),
        "box6" : set(),
        "row7" : set(),
        "col7" : set(),
        "box7" : set(),
        "row8" : set(),
        "col8" : set(),
        "box8" : set(),
        }

        def get_box_num(i, j):
            return (i // 3) * 3 + (j // 3)


        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    continue

                if board[i][j] in sudoku_sets[f"row{i}"]:
                    return False
                else:
                    sudoku_sets[f"row{i}"].add(board[i][j])

                if board[i][j] in sudoku_sets[f"col{j}"]:
                    return False
                else:
                    sudoku_sets[f"col{j}"].add(board[i][j])

                box_num = get_box_num(i,j)
                if board[i][j] in sudoku_sets[f"box{box_num}"]:
                    return False
                else:
                    sudoku_sets[f"box{box_num}"].add(board[i][j])
        
        return True
