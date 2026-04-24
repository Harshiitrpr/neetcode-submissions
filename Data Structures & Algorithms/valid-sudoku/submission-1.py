class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check rows
        for i in range(9):
            bitmask_row = [False] * 9
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if bitmask_row[int(board[i][j]) - 1]:
                        return False
                    else:
                        bitmask_row[int(board[i][j]) - 1] = True
            
            bitmask_col = [False] * 9
            for j in range(9):
                if board[j][i] == '.':
                    continue
                else:
                    if bitmask_col[int(board[j][i]) - 1]:
                        return False
                    else:
                        bitmask_col[int(board[j][i]) - 1] = True
            diff = [0, 3, 6]

            
        for di in diff:
            for dj in diff:
                bitmask = [False] * 9
                for i in range(3):
                    for j in range(3):
                        if board[i + di][j + dj] == '.':
                            continue
                        else:
                            if bitmask[int(board[i + di][j + dj]) - 1]:
                                return False
                            else:
                                bitmask[int(board[i + di][j + dj]) - 1] = True
        return True
                

                
        